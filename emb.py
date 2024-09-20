from transformers import AutoTokenizer, AutoModel
import torch
from datasets import dataset

# Configuração do modelo
model_name = "sentence-transformers/paraphrase-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Função para gerar embeddings
def get_embedding(text):
    tokens = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**tokens)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

# Exemplo: gerar embedding para o primeiro sintoma
example_symptom = dataset[0]['Symptoms']
embedding = get_embedding(example_symptom)
print(embedding)
