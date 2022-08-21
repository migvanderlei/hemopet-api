import json
from datetime import date
from time import sleep

from src.domain.entity.Endereco import Endereco


class Veterinario():
    def __init__(
        self,
        nome: str,
        cpf: str,
        crmv: str,
        data_nascimento: date,
        telefone: str,
        sexo: str,
        endereco: Endereco
    ):
        self.nome = nome
        self.cpf = cpf
        self.crmv = crmv
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.sexo = sexo
        self.endereco = endereco

    def reprJSON(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "crmv": self.crmv,
            "data_nascimento": self.data_nascimento.isoformat(),
            "telefone": self.telefone,
            "sexo": self.sexo,
            "endereco": self.endereco.reprJSON()
        }
