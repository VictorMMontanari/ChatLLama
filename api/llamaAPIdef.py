from flask import Flask, request, jsonify
from qdrant_client import QdrantClient
import requests
import json
from dotenv import load_dotenv
import os
from sentence_transformers import SentenceTransformer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Carregar variáveis de ambiente
load_dotenv()
urlQdrant = os.getenv('DATABASE_URL')
apiQdrant = os.getenv('CHAVE_QDRANT')
apillama = os.getenv('CHAVE_LLAMA')

# Verificar se as variáveis de ambiente estão definidas
if not urlQdrant or not apiQdrant or not apillama:
    raise ValueError("As variáveis de ambiente estão ausentes ou incorretas.")

# Inicializando o cliente do Qdrant
qdrant_client = QdrantClient(
    url=urlQdrant,
    api_key=apiQdrant
)

# Carregar o modelo de embeddings
modelo_embeddings = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Função para gerar o embedding da pergunta
def gerar_embedding(texto):
    return modelo_embeddings.encode(texto).tolist()

# Função para buscar o contexto no Qdrant baseado nos embeddings
def buscar_contexto_qdrant(query_embedding):
    try:
        search_result = qdrant_client.search(
            collection_name="Teste_Boock",
            query_vector=query_embedding,
            limit=3
        )
        contexto = " ".join([res.payload.get('text', '') for res in search_result])
        print("TESTESTES",contexto)
        return contexto
    except Exception as e:
        print(f"Erro ao buscar contexto no Qdrant: {e}")
        return ""

# Função para gerar resposta do LLaMA diretamente
def gerar_resposta_llama(query, contexto):
    headers = {
        "Authorization": apillama,
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {"role": "system", "content": f"Contexto: {contexto}. Você é um agente da saúde e apenas pode responder coisas da área."},
            {"role": "user", "content": query}
        ]
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(data))
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        print(f"Erro na API do LLaMA: {e}")
        return None

# Endpoint para o chat
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    pergunta = data.get("mensagem_usuario")
    
    if not pergunta:
        return jsonify({"error": "Pergunta não fornecida"}), 400
    
    query_embedding = gerar_embedding(pergunta)
    contexto = buscar_contexto_qdrant(query_embedding)
    
    resposta = gerar_resposta_llama(pergunta, contexto)
    
    if resposta:
        return jsonify({"resposta": resposta}), 200
    else:
        return jsonify({"error": "Não foi possível gerar uma resposta."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
