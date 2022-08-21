from datetime import date
from typing import List
from src.domain.entity.Doacao import Doacao
from src.domain.entity.Exame import Exame

from src.domain.entity.Tutor import Tutor


class Animal():
    def __init__(
        self,
        id: str,
        nome: str,
        sexo: str,
        raca: str,
        tipo_sanguineo: str,
        data_nascimento: date,
        status: bool,
        tutor: Tutor,
        clinica: str,
        exames: List[Exame] = [],
        doacoes: List[Doacao] = []
    ):
        self.id = id
        self.nome = nome
        self.sexo = sexo
        self.raca = raca
        self.tipo_sanguineo = tipo_sanguineo
        self.data_nascimento = data_nascimento
        self.status = status
        self.exames = exames
        self.doacoes = doacoes
        self.tutor = tutor
        self.clinica = clinica

    def reprJSON(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "sexo": self.sexo,
            "raca": self.raca,
            "tipo_sanguineo": self.tipo_sanguineo,
            "data_nascimento": self.data_nascimento.isoformat(),
            "status": self.status,
            "exames": [exame.reprJSON() for exame in self.exames],
            "doacoes": [doacao.reprJSON() for doacao in self.doacoes],
            "tutor": self.tutor.reprJSON(),
            "clinica": self.clinica
        }
