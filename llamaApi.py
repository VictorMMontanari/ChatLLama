import requests
import json

pergunta = input()

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer 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",
  },
   data=json.dumps({
        "model": "meta-llama/llama-3.1-8b-instruct:free",  # Optional
        "transforms": [''],
        "messages": [
            #{"role": "system", "content": "Você é um agente da area da saúde"},
            {
                "role": "user",
                "content": f"{pergunta}"
            }
        ]
    })
)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Imprimindo a resposta em formato JSON
    data = response.json()
    print(data['choices'][0]['message']['content'])  # Ou use response.text para o conteúdo bruto
else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)  # Exibe o conteúdo de erro retornado