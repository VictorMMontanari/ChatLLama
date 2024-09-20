import csv

# Abra o arquivo CSV
with open('Diseases_Symptoms.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Crie a lista de documentos
    documents = []
    
    # Itere sobre as linhas do CSV e crie um dicionário para cada linha
    for row in reader:
        document = {
            "Code": int(row['Code']),
            "name": row['Name'],
            "symptoms": row['Symptoms'],
            "treatments": row['Treatments']
        }
        documents.append(document)

# Agora, vamos salvar isso em um arquivo .py
with open('documentos.py', 'w', encoding='utf-8') as pyfile:
    pyfile.write("documents = [\n")
    for doc in documents:
        pyfile.write("    {\n")
        pyfile.write(f"        \"Code\": {doc['Code']},\n")
        pyfile.write(f"        \"name\": \"{doc['name']}\",\n")
        pyfile.write(f"        \"symptoms\": \"{doc['symptoms']}\",\n")
        pyfile.write(f"        \"treatments\": \"{doc['treatments']}\"\n")
        pyfile.write("    },\n")
    pyfile.write("]\n")
