from flask import Flask, request, jsonify
from qdrant_client import QdrantClient
import requests
import json
from dotenv import load_dotenv
import os

from flask_cors import CORS  # Importa CORS

app = Flask(__name__)
CORS(app)  # Permite CORS para todas as rotas


# Carregar variáveis de ambiente
load_dotenv()
urlQdrant = os.getenv('DATABASE_URL')
apiQdrant = os.getenv('CHAVE_QDRANT')
apillama = os.getenv('CHAVE_LLAMA')

# Inicializando o cliente do Qdrant
qdrant_client = QdrantClient(
    url=urlQdrant,
    api_key=apiQdrant
)

# Função para gerar resposta do LLaMA diretamente
def gerar_resposta_llama(query, contexto):
    headers = {
        "Authorization": apillama,  # Token do OpenRouter
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",  # Modelo a ser utilizado
        "messages": [
            # {
            #     "role": "system", 
            #     "content": "Você é um agente da area da saúde"
            #  },
            {
                "role": "user",
                "content": f"Contexto: {contexto}"  # Contexto extraído do Qdrant
            },
            {
                "role": "user",
                "content": query  # Pergunta do usuário
            }
        ]
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        data = response.json()
        return data['choices'][0]['message']['content']
    else:
        return None

# Função para buscar o contexto no Qdrant baseado nos embeddings
def buscar_contexto_qdrant(query_embedding):
    search_result = qdrant_client.search(
        collection_name="Teste_Boock",  # Substitua pelo nome da sua coleção no Qdrant
        query_vector=query_embedding,
        limit=3  # Limite de documentos mais próximos
    )
    # Combine os textos dos resultados para usar como contexto
    contexto = " ".join([res.payload.get('text', '') for res in search_result])
    return contexto

# Endpoint para o chat
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    pergunta = data.get("mensagem_usuario")
    
    if not pergunta:
        return jsonify({"error": "Pergunta não fornecida"}), 400
    
    # Para esta versão ajustada, vamos usar um contexto genérico por enquanto
    contexto = "Você é um agente da area da saúde"
    
    # Gerar resposta usando o LLaMA com o contexto adicional
    resposta = gerar_resposta_llama(pergunta, contexto)
    
    if resposta:
        return jsonify({"resposta": resposta}), 200
    else:
        return jsonify({"error": "Não foi possível gerar uma resposta."}), 500

# Executa a aplicação Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)