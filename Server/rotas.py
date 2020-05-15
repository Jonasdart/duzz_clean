# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request

app = Flask(__name__)

motoristas = [
    {
        'nome': 'Joao Pablo',
        'placa': '123',
        'ultima_limpeza': '20-10',
        'limpezas_recusadas': 3,

        'nova_manutencao':{
            'dia': '10-89',
            'km': '15000'
        }
    },
    {
        'nome': 'Jonas',
        'placa': '1234',
        'ultima_limpeza': '21-10',
        'limpezas_recusadas': 8,

        'nova_manutencao':{
            'dia': '17-9',
            'km': '250'
        }
    }, 
    {
        'nome': 'Matheus',
        'placa': '12345',
        'ultima_limpeza': '20-10',
        'limpezas_recusadas': 2,

        'nova_manutencao':{
            'dia': '7-01',
            'km': '58795'
        }
    }
]

usuarios = [
    {
        'nome': 'diego',
        'cpf': 1
    },
    {
        'nome': 'usuario2',
        'cpf': 2
    }
]

nova_limpeza = [
    {
        'usuario': 1, #cpf do usuario que ta solicitando nova limpeza
        'carro': '123ijk', #placa do carro que ta recebendo a solicitação
        'aceito': 'true' #boolen no bd pra aceitar ou nao a limpeza <3
    },
    {
        'usuario': 2,
        'carro': '584',
        'aceito': 'false'
    }
]

avaliacao_do_usuario = [ #avaliação do usuario a respeito de UM UNICO carro
    {
        'usuario': 2, #cpf usuario ou algo q o identifica
        'carro': '4897s', #placa do carro ou algo q o identifica
        'avaliacao': 'UMA BOSTA' #avaliacao do cliente
    }
]


#mostrar json de motoristas - FUNCIONANDO
@app.route('/motoristas', methods=['GET'])
def home_motoristas():
    return jsonify(motoristas), 200

#mostrar json de usuarios - FUNCIONANDO
@app.route('/usuarios', methods=['GET'])
def home_usuarios():
    return jsonify(usuarios), 200

#mostrar json de limpezas solicitadas - FUNCIONANDO
@app.route('/nova_limpeza', methods=['GET'])
def home_nova_limpeza():
    return jsonify(nova_limpeza), 200

#mostrar json de avaliacao do usuario a respeito de UM UNIICO carro - FUNCIONANDO 
@app.route('/avaliacao_do_usuario', methods=['GET'])
def home_avalicao():
    return jsonify(avaliacao_do_usuario), 200

    
#excluir carro - FUNCIONANDO
@app.route('/motoristas/<string:placa>', methods=['DELETE'])
def excluir_carro(placa):
   aux = [motorista for motorista in motoristas if motorista['placa'] == placa]
   motoristas.remove (aux[0])
   return jsonify({'mensage': 'carro excluido com sucesso'}), 200


#excluir usuario - FUNCIONANDO
@app.route('/usuarios/<int:cpf>', methods=['DELETE'])
def excluir_usuario(cpf):
    aux = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    usuarios.remove (aux[0])
    return jsonify({'mensage': 'usuario excluido com sucesso'}), 200



#adicionar novo motorista - FUNCIONANDO
@app.route('/motoristas', methods=['POST'])
def save_motorista():
    data = request.get_json()
    motoristas.append(data)
    return jsonify(data), 201


#adicionar novo usuario - FUNCIONANDO
@app.route('/usuarios', methods=['POST'])
def save_usuario():
    data = request.get_json()
    usuarios.append(data)
    return jsonify(data), 201



#pesquisar por placa - FUNCIONANDO
@app.route('/motoristas/<string:placa>', methods=['GET'])
def por_placa(placa):
    for motorista in motoristas:
        if motorista['placa'] == placa:
            return jsonify(motorista), 200
    return jsonify({'error': 'carro nao encontrado'}), 404

#pesquisar por ultima limpeza - ACHO QUE NÃO TEM NECESSIDADE, PQ QUANDO PESQUISAR POR PLACA JÁ VAI TER ESSE DADO (FUNCIONANDO)
@app.route('/motoristas/ultima_limpeza/<string:ultima_limpeza>', methods=['GET'])
def ultimalimpeza(ultima_limpeza):
    ultimalimpeza = [motorista for motorista in motoristas if motorista['ultima_limpeza'] == ultima_limpeza]
    return jsonify(ultimalimpeza),200


#usuario solicita nova limpeza - FUNCIONANDO
@app.route('/nova_limpeza', methods=['POST'])
def solicitacao_limpeza():
    data = request.get_json()
    nova_limpeza.append(data)
    return jsonify(data), 201


#avalicao do cliente a respeito de UM carro(QRcode) - FUNCIONANDO
@app.route('/avaliacao_do_usuario', methods=['POST'])
def avaliacao():
    data = request.get_json()
    avaliacao_do_usuario.append(data)
    return jsonify (data), 201


#pesquisar situação do carro, e sua proxima manutenção.
@app.route('/motoristas/nova_manutencao/<string:placa>', methods=['GET'])
def nova_manutencao(placa):
    for motorista in motoristas:
        if motorista['placa'] == placa:
            return jsonify(motorista), 200
    return jsonify({'error': 'carro nao encontrado'}), 404

if __name__ == "__main__":
    app.run(debug=True)