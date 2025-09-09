# pip install flask
from flask import Flask, request, make_response, jsonify

# Importação da base de dados
from bd import Carros


# Esse módulo do Flask vai subir a nossa API localmente
# Vamos instanciar o modulo Flask na nossa variavel app
app = Flask ('carros')

# METODO 1 - VIZUALIZAÇÃO DE DADOS (GET)
# 1 - O QUE ESSE METODO VAI FAZER?
# 2 - ONDE ELE VAI FAZER?

@app.route('/carro', methods = ['GET'])
def get_carros():
    return Carros

# METODO 1 PARTE 2 - VIZUALIZAÇÃO DE DADOS POR ID(GET)
@app.route('/carro/<int:id_p>', methods = ['GET'])
def get_carros_id(id_p):
    for carro in Carros:
        if carro.get('id') == id_p:
            return jsonify(carro)

# METODO 2 - CRIAR NOVOS REGISTROS (POST)
# Verificar os dados que estão passados na requisição e armazenar na nossa base
@app.route('/carro', methods=['POST'])
def criar_carro():
    car = request.json
    Carros.append(car)
    return make_response(
        jsonify(
            mensagem = 'Carro cadastrado com sucesso!!',
            carro = car
        )
    )

# METODO 3 - DELETAR REGISTROS (DELETE)
@app.route('/carro/int:id', methods = ['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate (Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return make_response(
                jsonify(
                    mensagem = "Carro Excluído")
            )
        
# METODO 4 -  EDITAR OS REGISTROS (PUT)
@app.route('/carro/int:id', methods = ['PUT'])
def editar_carro(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate (Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(
                Carros[indice]
                )

app.run(port = 5000, host = 'localhost', debug = True)


