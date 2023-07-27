from datetime import datetime

from aluno_class import Aluno
from prova_class import Prova

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

if __name__ == '__main__':
    for obj in list_alunos:
        print("Id: {}".format(obj.id))
        print("Nome: {}".format(obj.nome))
        print("Sobrenome: {}".format(obj.sobrenome))
        print("Idade: {} anos".format(obj.idade))
        print("Email: {}".format(obj.email))
        print("Nome completo {}".format(obj.nome_completo().upper()))
        print("Prova de {}".format(obj.prova.materia))
        print("Nota: {} / Resultado: {}".format(obj.prova.nota, obj.prova.resultado()))
        print("=====================================")

        print("Data: {}".format(datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")))
        print("Dia: {}".format(datetime.strftime(datetime.now(), "%d")))
        print("Mês: {}".format(datetime.strftime(datetime.now(), "%m")))
        print("Ano: {}".format(datetime.strftime(datetime.now(), "%Y")))
