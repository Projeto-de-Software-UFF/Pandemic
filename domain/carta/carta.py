from enum import Enum

class TipoCarta(Enum):
    CIDADE = "Cidade"
    EVENTO = "Evento"
    EPIDEMIA = "Epidemia"

class Carta:
    def __init__(self, nome: str, tipo: TipoCarta):
        self.nome = nome
        self.tipo = tipo

    def __repr__(self):
        return f"{self.tipo.value}: {self.nome}"


