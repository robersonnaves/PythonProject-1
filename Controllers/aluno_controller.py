from flask import jsonify, request
from flask_restful import Resource

from Domain.aluno_class import AlunoSchema
from Repositories.aluno_repository import AlunoRepository


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

    def post(self):
        try:
            data = request.get_json()
            if not data:
                return {"message": "Dados de aluno invalidos"}, 400
            else:
                aluno_new = self.aluno_schema.load(data)
                aluno_added = self.aluno_repository.add_aluno(aluno_new)
                result = self.aluno_schema.dump(aluno_added)
                response = jsonify(result)
                response.headers.add('Content-Type', 'application/json; charset=utf-8')
                return response
        except ValueError as e:
            return {"message": str(e)}, 400
