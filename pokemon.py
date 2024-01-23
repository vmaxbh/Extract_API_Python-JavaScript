import os
import requests
import json

# Caminho da pasta pokemon_files
folder_path = os.getenv("POKEMON_FILES_PATH", "pokemon_files")

# Remove todos os arquivos na pasta pokemon_files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
            print(f"Arquivo removido: {file_path}")
    except Exception as e:
        print(f"Erro ao remover arquivo {file_path}: {e}")

# Definindo a URL base da API
url = "https://pokeapi.co/api/v2/pokemon/"

# Inicializando a lista de pokémons e o contador
pokemon_list = list()
counter = 1

# Loop infinito até que a URL seja None
while url != None:
    # Definindo o payload e os headers para a requisição
    payload = {}
    headers = {}

    # Fazendo a requisição GET para a URL e convertendo a resposta para JSON
    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)
    
    # Atualizando a URL para a próxima página de resultados
    url = response["next"]

    # Iterando sobre cada resultado na resposta
    for item in response["results"]:
        # Extraindo o nome do pokémon
        pokemon_name = item["name"]
        
        # Construindo a URL para obter detalhes do pokémon
        url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        
        # Fazendo a requisição GET para a URL do pokémon e convertendo a resposta para JSON
        response_pokemon = json.loads(requests.request("GET", url_pokemon, headers=headers, data=payload).text)
        
        # Criando um dicionário com as informações do pokémon
        infos = {
            "name": pokemon_name,
            "id": response_pokemon["id"],
            "height": response_pokemon["height"],
            "weight": response_pokemon["weight"],
            "is_default": response_pokemon["is_default"]
        }
        
        # Adicionando as informações do pokémon à lista
        pokemon_list.append(infos)
        
        # Imprimindo o ID do pokémon
        print(response_pokemon["id"])

    # Construindo o caminho do arquivo para salvar os dados
    file_path = os.path.join(folder_path, f"pokemon_file_{counter}.json")

    # Abrindo o arquivo no modo de escrita
    with open(file_path, "w") as outfile:
        # Imprimindo a mensagem de salvamento
        print(f"Salvando arquivo em: {file_path}")
        
        # Escrevendo os dados da lista no arquivo
        json.dump(pokemon_list, outfile)     
    
    # Incrementando o contador
    counter = counter + 1
    
    # Limpar a lista de pokémons para a próxima página
    pokemon_list = list()

# Imprimindo a lista vazia de pokémons
print(pokemon_list)
