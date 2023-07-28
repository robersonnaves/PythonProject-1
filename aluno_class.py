import uuid

from marshmallow import Schema, fields


class AlunoSchema(Schema):
    id = fields.UUID()
    nome = fields.Str()
    sobrenome = fields.Str()
    idade = fields.Int()
    email = fields.Email()
    prova = fields.Nested('ProvaSchema', many=False)


class Aluno:
    def __init__(self, nome, sobrenome, idade, email, prova):
        self.id = uuid.uuid4()
        self.nome = str(nome)
        self.sobrenome = str(sobrenome)
        self.idade = int(idade)
        self.email = str(email)
        self.prova = prova

    def nome_completo(self):
        return self.nome + " " + self.sobrenome
