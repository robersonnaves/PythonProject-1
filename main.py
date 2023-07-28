from flask import Flask, request, jsonify

from aluno_class import Aluno, AlunoSchema
from prova_class import Prova, ProvaSchema

app = Flask(__name__)

try:
    provaAluno1 = Prova("Matemática", 10.0)
    provaAluno2 = Prova("Português", 8.0)
    provaAluno3 = Prova("História", 6.0)
    provaAluno4 = Prova("Geografia", 4.0)
except ValueError as e:
    print(f"Erro: {e}")
    exit(1)

aluno1 = Aluno("João", "da Silva", 23, "joao@a.com.br", provaAluno1)
aluno2 = Aluno("Maria", "da Silva", 23, "maria@b.com.br", provaAluno2)
aluno3 = Aluno("José", "da Souza", 23, "jose@c.com.br", provaAluno3)
aluno4 = Aluno("Ana", "da Souza", 23, "ana@d.com.br", provaAluno4)

list_alunos = [aluno1, aluno2, aluno3, aluno4]

prova_schema = ProvaSchema()
aluno_schema = AlunoSchema()


@app.route('/alunos', methods=['GET'])
def get_alunos():
    result = aluno_schema.dump(list_alunos, many=True)
    response = jsonify(result)
    response.headers.add('Content-Type', 'application/json; charset=utf-8')
    return response


@app.route('/alunos/<uuid:_id>', methods=['GET'])
def get_aluno(_id):
    for _aluno in list_alunos:
        if _aluno.id == _id:
            result = aluno_schema.dump(_aluno)
            response = jsonify(result)
            response.headers.add('Content-Type', 'application/json; charset=utf-8')
            return response
    return jsonify({"message": "Aluno não encontrado."}), 404


@app.route('/alunos/<uuid:_id>', methods=['DELETE'])
def delete_aluno(_id):
    for _aluno in list_alunos:
        if _aluno.id == _id:
            list_alunos.remove(_aluno)
            return jsonify({"message": "Aluno removido com sucesso."}), 200
    return jsonify({"message": "Aluno não encontrado."}), 404


@app.route('/alunos/', methods=['POST'])
def post_aluno():
    data = request.json
    if 'nome' not in data or 'prova' not in data:
        return jsonify({'message': 'Dados incompletos'}), 400
    novo_aluno = Aluno(data['nome'], data['sobrenome'], data['idade'], data['email'], data['prova'])
    list_alunos.append(novo_aluno)
    result = aluno_schema.dump(novo_aluno)
    return jsonify({"message": "Aluno criado com sucesso.", 'aluno': result}), 201


if __name__ == '__main__':
    for aluno in list_alunos:
        print(aluno.id)
    app.run(debug=True)
