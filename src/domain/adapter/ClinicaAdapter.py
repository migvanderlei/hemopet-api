from datetime import date
from typing import List
from src.domain.entity.Clinica import Clinica
from src.domain.entity.Doacao import Doacao
from src.domain.entity.Endereco import Endereco
from src.domain.entity.Veterinario import Veterinario


class ClinicaAdapter:

    def __init__(self):
        pass

    def from_json(self, raw_data) -> Clinica:

        if not raw_data:
            return {}
        else:
            return Clinica(
                raw_data.get("id"),
                raw_data.get("nome"),
                raw_data.get("cnpj"),
                raw_data.get("telefone"),
                self.__adapt_endereco(
                    raw_data.get("endereco")
                ),
                self.__adapt_veterinarios(
                    raw_data.get("veterinarios")
                ),
            )

    def __adapt_endereco(self, raw_endereco) -> Endereco:
        if not raw_endereco:
            return {}
        else:
            return Endereco(
                raw_endereco.get("cep"),
                raw_endereco.get("pais"),
                raw_endereco.get("estado"),
                raw_endereco.get("cidade"),
                raw_endereco.get("bairro"),
                raw_endereco.get("rua"),
                raw_endereco.get("numero"),
                raw_endereco.get("referencia"),
                raw_endereco.get("complemento")
            )

    def __adapt_veterinario(self, raw_veterinario) -> Veterinario:
        if not raw_veterinario:
            return {}
        else:
            return Veterinario(
                raw_veterinario.get("nome"),
                raw_veterinario.get("cpf"),
                raw_veterinario.get("cnoj"),
                date.fromisoformat(
                    raw_veterinario.get("data_nascimento")
                ),
                raw_veterinario.get("telefone"),
                raw_veterinario.get("sexo"),
                self.__adapt_endereco(
                    raw_veterinario.get("endereco")
                )
            )

    def __adapt_veterinarios(self, raw_veterinarios) -> List[Veterinario]:
        if not raw_veterinarios:
            return []
        else:
            return [
                self.__adapt_veterinario(veterinario)
                for veterinario in raw_veterinarios
            ]
