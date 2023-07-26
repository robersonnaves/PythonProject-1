from datetime import datetime

from aluno_class import Aluno

aluno1 = Aluno("João", "da Silva", 23, "joao@a.com.br")
aluno2 = Aluno("Maria", "da Silva", 23, "maria@b.com.br")
aluno3 = Aluno("José", "da Souza", 23, "jose@c.com.br")

listaAlunos = [aluno1, aluno2, aluno3]

if __name__ == '__main__':
    for obj in listaAlunos:
        print(obj.id)
        print(obj.nome)
        print(obj.sobrenome)
        print(obj.idade)
        print(obj.email)
        print(obj.nome_completo().upper())
        print(len(obj.nome_completo()))
        print("=====================================")

print("Data: {}".format(datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")))
print("Dia: {}".format(datetime.strftime(datetime.now(), "%d")))
print("Mês: {}".format(datetime.strftime(datetime.now(), "%m")))
print("Ano: {}".format(datetime.strftime(datetime.now(), "%Y")))
