class Endereco():
    def __init__(
        self,
        cep: int,
        pais: str,
        estado: str,
        cidade: str,
        bairro: str,
        rua: str,
        numero: str,
        complemento: str = None,
        referencia: str = None
    ):
        self.cep = cep
        self.pais = pais
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.referencia = referencia

    def reprJSON(self):
        return {
            "cep": self.cep,
            "pais": self.pais,
            "estado": self.estado,
            "cidade": self.cidade,
            "bairro": self.bairro,
            "rua": self.rua,
            "numero": self.numero,
            "complemento": self.complemento,
            "referencia": self.referencia
        }
