import requests 
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json" # URL da API

response = requests.get(url) #resposta da requisição \ get (URL) é o endpoint

print (response.status_code) #código de status da resposta

if response.status_code == 200: #se o resultado do código de status for 200 (requisição bem sucedida)
    dados_json = response.json() #armazenar os dados em formato JSON na variável dados_json
    dados_restaurante = {}
    for item in dados_json: 
        nome_do_restaurante = item ['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            "item": item ['Item'],
            "price": item ['price'],
            "description": item ['description']
        })
else:
    print (f"O Erro foi: ", {response.status_code})

for nome_do_restaurante, dados in dados_restaurante.items():
    #Salvar os dados em arquivos JSON separados por restaurante
    nome_do_arquivo = f'{nome_do_restaurante}.json' 
    #Criar e abrir o arquivo JSON para escrita 
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, ensure_ascii=False, indent=4)
