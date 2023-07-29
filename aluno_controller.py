from flask import jsonify
from flask_restful import Resource

from aluno_class import AlunoSchema
from aluno_repository import AlunoRepository


class AlunoController(Resource):
    def __init__(self):
        self.aluno_schema = AlunoSchema()
        self.aluno_repository = AlunoRepository()

    def get(self, _id=None):
        data = []
        if _id is None:
            data = self.aluno_repository.get_all_alunos()
        else:
            data.append(self.aluno_repository.get_aluno_by_id(_id))
            if data is None:
                return "Aluno nao encontrado", 404
        result = self.aluno_schema.dump(data, many=True)
        response = jsonify(result)
        response.headers.add('Content-Type', 'application/json; charset=utf-8')
        return response
