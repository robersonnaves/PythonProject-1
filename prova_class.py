import uuid

from marshmallow import Schema, fields


class ProvaSchema(Schema):
    id = fields.UUID()
    materia = fields.Str()
    nota = fields.Float()


class Prova:
    def __init__(self, materia, nota):
        self.id = uuid.uuid4()
        self._materia = str(materia)
        self._nota = self._validate_nota(nota)
        self.resultado = self.resultado()

    @property
    def materia(self):
        return self._materia

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, value):
        self._nota = self._validate_nota(value)

    def resultado(self):
        if self._nota >= 9:
            return "Quadro de Honra"
        elif self._nota >= 7:
            return "Aprovado"
        elif self._nota >= 5:
            return "Recuperação"
        elif self._nota >= 3:
            return "Recuperação + Trabalho"
        else:
            return "Reprovado"

    @staticmethod
    def _validate_nota(nota):
        if not isinstance(nota, float):
            raise ValueError("A nota deve ser um número real.")
        if nota < 0 or nota > 10:
            raise ValueError("A nota deve ser um número entre 0 e 10.")
        return nota
