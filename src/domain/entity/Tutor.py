from datetime import date
import json

from src.domain.entity.Endereco import Endereco


class Tutor():
    def __init__(
        self,
        nome: str,
        cpf: str,
        data_nascimento: date,
        telefone: str,
        endereco: Endereco
    ):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.endereco = endereco

    def reprJSON(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "data_nascimento": self.data_nascimento.isoformat(),
            "telefone": self.nome,
            "endereco": self.endereco.reprJSON()
        }