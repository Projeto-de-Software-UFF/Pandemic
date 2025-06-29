from domain.carta.carta import Carta
from domain.cidade.cidade import Cidade
from domain.jogador.jogador import Jogador

class Teletransporte(Carta):
    def __init__(self, cidade: Cidade, jogador: Jogador):
        super().__init__(cidade, jogador)

    def efeito(self) -> None:
        print(f"AÇÃO: {self._jogador} teletransporta para a cidade {self._cidade}.")

    def __str__(self) -> str:
        return f"Carta de Teletransporte"