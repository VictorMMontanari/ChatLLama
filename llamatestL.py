from qdrant_client import QdrantClient
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
urlQdrant=os.getenv('DATABASE_URL')
apiQdrant=os.getenv('CHAVE_QDRANT')
apillama=os.getenv('CHAVE_LLAMA')
# Inicializando o cliente do Qdrant
qdrant_client = QdrantClient(
    url=urlQdrant,  # Substitua pelo seu endpoint do Qdrant
    api_key=apiQdrant  # Substitua pela sua chave de API do Qdrant
)


# Função para gerar resposta do LLaMA diretamente
def gerar_resposta_llama(query, contexto):
    headers = {
        "Authorization": apillama,  # Substitua pelo seu token do OpenRouter
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",  # Substitua pelo modelo correto
        "messages": [
            {
                "role": "system",
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
        print(f"Erro na requisição para gerar resposta: {response.status_code}")
        print(response.text)
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

# Função principal que une tudo
def main():
    pergunta = input("Faça sua pergunta: ")

    # Para esta versão ajustada, vamos usar uma pergunta genérica e contexto predefinido
    contexto = "Informações gerais sobre sintomas e doenças."

    # Gerar resposta usando o LLaMA com o contexto adicional
    resposta = gerar_resposta_llama(pergunta, contexto)
    
    if resposta:
        print("Resposta do LLaMA:")
        print(resposta)
    else:
        print("Não foi possível gerar uma resposta.")

# Executa a função principal
if __name__ == "__main__":
    main()
