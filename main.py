from flask import Flask
from flask_restful import Api

from aluno_controller import AlunoController

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    api.add_resource(AlunoController, "/alunos", "/alunos/<uuid:_id>")
    app.run(port=5000, debug=True)
