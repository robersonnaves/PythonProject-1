from Domain.aluno_class import Aluno
from Domain.prova_class import Prova


class AlunoRepository:
    def __init__(self):
        try:
            prova_aluno1 = Prova("Matemática", 10.0)
            prova_aluno2 = Prova("Português", 8.0)
            prova_aluno3 = Prova("História", 6.0)
            prova_aluno4 = Prova("Geografia", 4.0)
        except ValueError as e:
            print(f"Erro: {e}")
            exit(1)

        aluno1 = Aluno("f0c5574e-0207-481e-9093-e7df31e22531", "João", "da Silva", 23, "joao@a.com.br", prova_aluno1)
        aluno2 = Aluno("f0c5574e-0207-481e-9093-e7df31e22532", "Maria", "da Silva", 23, "maria@b.com.br", prova_aluno2)
        aluno3 = Aluno("f0c5574e-0207-481e-9093-e7df31e22533", "José", "da Souza", 23, "jose@c.com.br", prova_aluno3)
        aluno4 = Aluno("f0c5574e-0207-481e-9093-e7df31e22534", "Ana", "da Souza", 23, "ana@d.com.br", prova_aluno4)

        self.list_alunos = [aluno1, aluno2, aluno3, aluno4]

    def get_all_alunos(self):
        return self.list_alunos

    def get_aluno_by_id(self, _id):
        for aluno in self.list_alunos:
            if aluno.id == _id:
                return aluno
        return None

    def add_aluno(self, aluno):
        self.list_alunos.append(aluno)
        for aluno in self.list_alunos:
            print(aluno.nome)
        return aluno
