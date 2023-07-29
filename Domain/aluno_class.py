import uuid

from marshmallow import Schema, fields

from Domain.prova_class import ProvaSchema


class AlunoSchema(Schema):
    id = fields.UUID(required=True)
    nome = fields.Str()
    sobrenome = fields.Str()
    idade = fields.Int()
    email = fields.Email()
    prova = fields.Nested(ProvaSchema(), many=False)


class Aluno:
    def __init__(self, _id, nome, sobrenome, idade, email, prova):
        self.id = uuid.UUID(_id)
        self.nome = str(nome)
        self.sobrenome = str(sobrenome)
        self.idade = int(idade)
        self.email = str(email)
        self.prova = prova

    def nome_completo(self):
        return self.nome + " " + self.sobrenome
