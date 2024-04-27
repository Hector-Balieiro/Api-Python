import requests

def test_post():
    create = {
        "titulo":"teste",
        "autor": "teste"
    }

    resposta = requests.post('http://localhost:8080/livros', json=create)
    resposta_dict = resposta.json()
    novo_objeto = resposta_dict[-1]

    assert resposta.status_code == 200 and novo_objeto['id'] is not None

 