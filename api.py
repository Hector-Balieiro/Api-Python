from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {'id': 1, 'titulo': 'Senhor dos aneis', 'autor': 'J.R.R Tolkien'},
    {'id': 2, 'titulo': 'O poder do habito', 'autor': 'Não sei'},
    {'id': 3, 'titulo': 'O diário de anne Frank', 'autor': 'Não sei'},
    {'id': 4, 'titulo': 'Harry Potter', 'autor': 'J.K Rowling'},
    {'id': 5, 'titulo': 'O manifesto comunista', 'autor': 'Karl Marx'},
    {'id': 6, 'titulo': 'Negócio do Século XXI', 'autor': 'Robert Kiosak'},
    {'id': 7, 'titulo': 'Pai rico, Pai pobre', 'autor': 'Robert Kiosak'},
]


@app.errorhandler(404)
def invalid_route(e):
 return jsonify({'errorCode': 404, 'message': 'Invalid route'})


@app.route('/livros', methods = ['GET'])
def mostrar_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods = ['GET'])
def livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        else:
            return jsonify({'message':'ID não encontrado'})



@app.route('/livros/<int:id>', methods = ['PUT'])
def alterar(id):
    alterado = request.get_json()

    try:
        valor_id = alterado['id']
        valor_autor = alterado['autor']
        valor_titulo = alterado['titulo']
    except KeyError:
        return jsonify({'message': 'está faltando uma chave no novo valor adicionado'})

    if type(valor_id) == int and type(valor_autor) == str and type(valor_titulo) == str:
        for i, livro in enumerate(livros):
            if livro.get('id') == id:
                livros[i].update(alterado)
                return jsonify(livro)
    else:
        return jsonify({'message': 'Os tipos de valores das chaves "id","autor","titulo" tem que ser respectivamente: inteiro, string, string'})



@app.route('/livros', methods = ['POST'])
def adicionar():
    novo_valor = request.get_json()
    try:
        valor_id = novo_valor['id']
        valor_autor = novo_valor['autor']
        valor_titulo = novo_valor['titulo']
    
    except KeyError:
        return jsonify({'message': 'está faltando uma chave no novo valor adicionado'})

    if type(valor_id) == int and type(valor_autor) == str and type(valor_titulo) == str:
        for i in livros:
            if i['id'] == valor_id:
               return jsonify({'message': 'o id adicionado ja existe'})
            
        else:
                livros.append(novo_valor)
                print(novo_valor['id'])
                return jsonify(livros)
        
    elif valor_id == None or valor_autor == None or valor_titulo == None:
        return jsonify({'message':'os valores id, autor ou titulo não podem ser nulos'})
    else :
        return jsonify({'message': 'Os tipos de valores das chaves "id","autor","titulo" tem que ser respectivamente: inteiro, string, string'})
        

@app.route('/livros/<int:id>', methods = ['DELETE'])
def remover(id):
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            del(livros[i])
            return jsonify(livros)
        else:
            return jsonify({'message':'ID não encontrado para excluir'})
app.run(port = 8080, host = 'localhost', debug = True)