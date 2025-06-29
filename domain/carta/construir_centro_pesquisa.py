from domain.carta.carta import Carta
from domain.cidade.cidade import Cidade
from domain.jogador.jogador import Jogador

class ConstruirCentroPesquisa(Carta):
    def __init__(self, cidade: Cidade, jogador: Jogador):
        super().__init__(cidade, jogador)

    def efeito(self) -> None:
        print(f"AÇÃO: {self._jogador} construiu um centro de pesquisa na cidade{self._cidade}.")

    def __str__(self) -> str:
        return f"Carta de Centro de Pesquisa"