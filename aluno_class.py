import uuid


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
