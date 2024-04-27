from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Senhor dos aneis',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'O poder do habito',
        'autor': 'Não sei'
    },
    {
        'id': 3,
        'titulo': 'O diário de anne Frank',
        'autor': 'Não sei'
    },
    {
        'id': 4,
        'titulo': 'Harry Potter',
        'autor': 'J.K Rowling'
    },
    {
        'id': 5,
        'titulo': 'O manifesto comunista',
        'autor': 'Karl Marx'
    },
    {
        'id': 6,
        'titulo': 'Negócio do Século XXI',
        'autor': 'Robert Kiosak'
    },
    {
        'id': 7,
        'titulo': 'Pai rico, Pai pobre',
        'autor': 'Robert Kiosak'
    },
]


@app.errorhandler(404)
def invalid_route(e):
  return jsonify({'errorCode': 404, 'message': 'Invalid route'})


@app.route('/livros', methods=['GET'])
def mostrar_livros():
  return jsonify(livros)


@app.route('/livros/<int:id>', methods=['GET'])
def livro_id(id):
  resultado = None

  for livro in livros:
    if livro.get('id') == id:
      resultado = jsonify(livro)

  if resultado == None:
    return jsonify(errorCode=404, message='Livro não encontrado')
  else:
    return resultado


@app.route('/livros/<int:id>', methods=['PUT'])
def alterar(id):
    alterado = request.get_json()
    
    try:
        valor_autor = alterado['autor']
        valor_titulo = alterado['titulo']
    except KeyError:
        return jsonify({'message': 'está faltando uma chave no valor alterado'})

    if type(valor_autor) == str and type(valor_titulo) == str:
        for i, livro in enumerate(livros):
            if livro.get('id') == id:
                livros[i].update(alterado)
                return jsonify(livro)
            else:
                return jsonify({'message':'Id não encontrado'})
    else:
        return jsonify({'message': 'Os tipos de valores das chaves "autor" e "titulo", tem que ser respectivamente: string, string'})



@app.route('/livros', methods = ['POST'])
def adicionar():

    novo_valor = request.get_json()

    try:
        valor_autor = novo_valor['autor']
        valor_titulo = novo_valor['titulo']
    
    except KeyError:
        return jsonify({'message': 'está faltando uma chave no novo valor adicionado'})
    
    if type(valor_autor) == str and type(valor_titulo) == str:
                novo_id = livros[-1]
                novo_valor['id'] = novo_id['id']+1
                livros.append(novo_valor)

                return jsonify(livros)
        
    elif valor_autor == None or valor_titulo == None:
        return jsonify({'message':'os valores id, autor ou titulo não podem ser nulos'})
    else :
        return jsonify({'message': 'Os tipos de valores das chaves "id","autor","titulo" tem que ser respectivamente: inteiro, string, string'})
        

@app.route('/livros/<int:id>', methods = ['DELETE'])
def remover(id):
    livro_removido = {}
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            livro_removido = livros[i]
            del(livros[i])
            return jsonify({'Livro deletado':livro_removido})

    return jsonify({'message':'ID não encontrado para excluir'})
app.run(port = 8080, host = 'localhost', debug = True)
