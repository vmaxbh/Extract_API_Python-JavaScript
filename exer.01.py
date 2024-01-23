import requests
import json

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
        file_path = fr"C:\Estudos\Python_API_udemy\pokemon\exer.01\post_{post['id']}.json"
        
        # Salvamos cada post individualmente em um arquivo separado
        with open(file_path, "w") as outfile:
            print(f"Salvando arquivo em: {file_path}")
            json.dump(info, outfile)
        
    # Atualizamos a URL para a próxima página de resultados
    url = response[-1]["id"] + 1 if response else None
    counter += 1