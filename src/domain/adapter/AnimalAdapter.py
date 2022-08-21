from datetime import date
from typing import List
from src.domain.entity.Animal import Animal
from src.domain.entity.Doacao import Doacao
from src.domain.entity.Endereco import Endereco
from src.domain.entity.Exame import Exame
from src.domain.entity.Tutor import Tutor


class AnimalAdapter:

    def __init__(self):
        pass

    # def to_json(self, artist: Artist):
    #     return {
    #         "id": artist.id_,
    #         "name": artist.artist_name,
    #         "birthDate": artist.date_of_birth,
    #         "origin": artist.origin,
    #         "imageUrl": artist.image_url,
    #         "description": artist.text
    #     }

    # def to_json_no_text(self, artist: Artist):
    #     return {
    #         "id": artist.id_,
    #         "name": artist.artist_name,
    #         "birthDate": artist.date_of_birth,
    #         "origin": artist.origin,
    #         "imageUrl": artist.image_url,
    #     }

    # def to_json_only_name(self, artist: Artist):
    #     return {
    #         "id": artist.id_,
    #         "name": artist.artist_name
    #     }

    def from_json(self, raw_data) -> Animal:

        if not raw_data:
            return {}
        else:
            return Animal(
                raw_data.get("id"),
                raw_data.get("nome"),
                raw_data.get("sexo"),
                raw_data.get("raca"),
                raw_data.get("tipo_sanguineo"),
                date.fromisoformat(
                    raw_data.get("data_nascimento")
                ),
                raw_data.get("status"),
                self.__adapt_tutor(
                    raw_data.get("tutor")
                ),
                raw_data.get("clinica"),
                self.__adapt_exames(
                    raw_data.get("exames")
                ),
                self.__adapt_doacoes(
                    raw_data.get("doacoes")
                )
            )

    def __adapt_tutor(self, raw_tutor) -> Tutor:
        if not raw_tutor:
            return {}
        else:
            return Tutor(
                raw_tutor.get("nome"),
                raw_tutor.get("cpf"),
                date.fromisoformat(
                    raw_tutor.get("data_nascimento")
                ),
                raw_tutor.get("telefone"),
                self.__adapt_endereco(
                    raw_tutor.get("endereco")
                )
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

    def __adapt_exames(self, raw_exames) -> List[Exame]:
        if not raw_exames:
            return []
        else:
            return [
                Exame(
                    date.fromisoformat(raw_exame.get("data")),
                    raw_exame.get("url")
                )
                for raw_exame in raw_exames
            ]

    def __adapt_doacoes(self, raw_doacoes) -> List[Doacao]:
        if not raw_doacoes:
            return []
        else:
            return [
                Doacao(
                    date.fromisoformat(raw_doacao.get("data")),
                )
                for raw_doacao in raw_doacoes
            ]
