import uuid


class Aluno:
    def __init__(self, nome, sobrenome, idade, email):
        self.id = uuid.uuid4()
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = int(idade)
        self.email = email

    def nome_completo(self):
        return self.nome + " " + self.sobrenome
