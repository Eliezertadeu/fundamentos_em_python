import requests
def returnCep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())
    print(type(response.text))

    dados_cep = response.json()
    print(dados_cep['logradouro'])

def returnPoke(poke):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(poke))
    print(response.json())

if __name__ == '__main__':
    returnCep(13720000)
    returnPoke('ditto')