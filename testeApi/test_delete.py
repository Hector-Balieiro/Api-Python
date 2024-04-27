import requests

def test_delete():
    url = 'http://localhost:8080/livros/'

    delete_id = "awdjbsajkd"
    resposta = requests.delete(url+str(delete_id))

    assert resposta.status_code == 200
    

test_delete()
   