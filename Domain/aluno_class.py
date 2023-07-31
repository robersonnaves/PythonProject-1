import uuid

from marshmallow import Schema, fields, post_load

from Domain.prova_class import ProvaSchema


class AlunoSchema(Schema):
    _id = fields.Str(required=True)
    nome = fields.Str(required=True)
    sobrenome = fields.Str(required=True)
    idade = fields.Int(required=True)
    email = fields.Email(required=True)
    prova = fields.Nested(ProvaSchema(), required=True, many=False)

    @post_load
    def make_aluno(self, data, **kwargs):
        return Aluno(**data)


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
