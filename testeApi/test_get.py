import requests

def test_get():

    

    resposta = requests.get('http://localhost:8080/livros')
    resposta_dict = resposta.json()

    tamanho_lista = len(resposta_dict)

    assert resposta.status_code == 200 and tamanho_lista > 0