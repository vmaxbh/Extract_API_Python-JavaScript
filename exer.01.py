import os
import requests
import json

# Caminho da pasta exer.01
folder_path = r"C:\Estudos\Python_API_udemy\pokemon\exer.01"

# Remove todos os arquivos na pasta exer.01
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
            print(f"Arquivo removido: {file_path}")
    except Exception as e:
        print(f"Erro ao remover arquivo {file_path}: {e}")

url = "https://jsonplaceholder.typicode.com/posts"

counter = 1
while url != None:
    payload = {}
    headers = {}

    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)

    for post in response:
        info = {
            "userID": post["userId"],
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        }

        print(post["id"])

        # Aqui, mudamos o caminho do arquivo para incluir o ID do post no nome do arquivo
        file_path = os.path.join(folder_path, f"post_{post['id']}.json")

        # Salvamos cada post individualmente em um arquivo separado
        with open(file_path, "w") as outfile:
            print(f"Salvando arquivo em: {file_path}")
            json.dump(info, outfile)

    # Atualizamos a URL para a próxima página de resultados
    url = response[-1]["id"] + 1 if response else None
    counter += 1
