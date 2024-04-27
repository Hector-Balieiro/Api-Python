import requests

def test_put():

    url = 'http://localhost:8080/livros/'
    put_id = 3
    put_data = {
        "titulo":"Boss GT-1",
        "autor":"Black Star",
    }

    resposta = requests.put(url+str(put_id), json=put_data)
    resposta_dict = resposta.json()

    assert len(resposta_dict) > 0 

test_put()



