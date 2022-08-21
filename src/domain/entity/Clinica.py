from datetime import date
from typing import List

from src.domain.entity.Endereco import Endereco
from src.domain.entity.Veterinario import Veterinario


class Clinica():
    def __init__(
        self,
        id: str,
        nome: str,
        cnpj: str,
        telefone: str,
        endereco: Endereco,
        veterinarios: List[Veterinario] = [],
    ):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.endereco = endereco
        self.veterinarios = veterinarios

    def reprJSON(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cnpj": self.cnpj,
            "telefone": self.telefone,
            "endereco": self.endereco.reprJSON()
        }