from aluno_class import Aluno

aluno1 = Aluno("João", "da Silva", 23, "joao@a.com.br")
aluno2 = Aluno("Maria", "da Silva", 23, "maria@b.com.br")

if __name__ == '__main__':
    print(aluno1.id)
    print(aluno2.id)
    print(aluno1.nome_completo())
    print(aluno2.nome_completo())
    print(len(aluno1.nome_completo()))
    print(len(aluno2.nome_completo()))
