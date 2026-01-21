from fastapi import FastAPI, Query #Query é utilizado para definir parâmetros de consulta, que são passados na URl como por 
#exemplo: ?restaurante=NomeDoRestaurante
import requests
app = FastAPI() # create a FastAPI instance

@app.get('/api/hello')

def hello_world():
    ''' Endpoint que exibe o famoso "Hello, World!" na tela
    '''
    
    return {"message": "Hello, World!"}

#para esse projeto rodar na interface web, utilize o comando: uvicorn main:app --reload 

@app.get('/api/restaurantes/')
def restaurantes(restaurante:str = Query (None)):
    ''' Endpoint que busca o cardápio dos restaurantes disponíveis na API externa.'''
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json" # URL da API
    response = requests.get(url) #resposta da requisição \ get (URL) é o endpoint
    print (response.status_code) #código de status da resposta

    if response.status_code == 200: #se o resultado do código de status for 200 (requisição bem sucedida)
        dados_json = response.json() #armazenar os dados em formato JSON na variável dados_json
        
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurante = []
        for item in dados_json: 
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item ['Item'],
                    "price": item ['price'],
                    "description": item ['description']
                })
        
        return {"Restaurante": restaurante, 
                "Cardapio": dados_restaurante}
    
    else:
       return {
            "erro": response.status_code,
            "mensagem": response.reason
    }

#se vc digitar o docs na URL, ele te leva para a documentação automática gerada pelo FastAPI