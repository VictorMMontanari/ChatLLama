from flask import Flask, request, jsonify
from qdrant_client import QdrantClient
import requests
import json
from dotenv import load_dotenv
import os
from flask_cors import CORS
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from operator import itemgetter
import uuid

app = Flask(__name__)
CORS(app)

load_dotenv()
urlQdrant = os.getenv("DATABASE_URL")
apiQdrant = os.getenv("CHAVE_QDRANT")
apillama = os.getenv("CHAVE_LLAMA")

qdrant_client = QdrantClient(
    url=urlQdrant,
    api_key=apiQdrant
)

store = {}

def get_session_history(session_id: str) -> ConversationBufferMemory:
    if session_id not in store:
        store[session_id] = ConversationBufferMemory(
            return_messages=True, output_key="answer", input_key="question"
        )
    return store[session_id]

def _get_loaded_memory(x):
    return get_session_history(x["session_id"]).load_memory_variables({"question": x["question"]})

def load_memory_chain():
    return RunnablePassthrough.assign(
        chat_history=RunnableLambda(_get_loaded_memory) | itemgetter("history"),
    )

def gerar_resposta_llama(query, contexto, history):
    headers = {
        "Authorization": f"Bearer {apillama}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {
                "role": "system",
                "content": "Você é um agente da área da saúde"
            },
            {
                "role": "user",
                "content": f"Contexto: {contexto}"
            },
            {
                "role": "user",
                "content": query
            }
        ]
    }

    if history:
        data['messages'].insert(1, {
            "role": "user",
            "content": f"Histórico da conversa: {history}"
        })

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(data))
        response.raise_for_status() 
        data = response.json()
        return data['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

def buscar_contexto_qdrant(query_embedding):
    search_result = qdrant_client.search(
        collection_name="Teste_Boock",
        query_vector=query_embedding,
        limit=3 
    )
  
    contexto = " ".join([res.payload.get('text', '') for res in search_result])
    return contexto


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    pergunta = data.get("mensagem_usuario")
    session_id = data.get("session_id")

    if not pergunta:
        return jsonify({"error": "Pergunta não fornecida"}), 400

    memory = get_session_history(session_id)
    history = memory.load_memory_variables({"question": pergunta}).get("history", '')

    contexto = "Você é um agente da área da saúde"

    resposta = gerar_resposta_llama(pergunta, contexto, history)

    if resposta:

        memory.chat_memory.add_user_message(pergunta)
        memory.chat_memory.add_ai_message(resposta)

        return jsonify({"resposta": resposta}), 200
    else:
        return jsonify({"error": "Não foi possível gerar uma resposta."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
