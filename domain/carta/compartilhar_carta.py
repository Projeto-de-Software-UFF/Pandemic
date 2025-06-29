from domain.carta.carta import Carta
from domain.cidade.cidade import Cidade
from domain.jogador.jogador import Jogador

class CompartilharCarta(Carta):
    def __init__(self, cidade: Cidade, jogador: Jogador):
        super().__init__(cidade, jogador)

    def efeito(self) -> None:
        # Necessário referência a outro jogador
        print(f"AÇÃO: {self._jogador} está compartilhando conhecimento com outro jogador na {self._cidade}.")

    def __str__(self) -> str:
        return f"Carta de Compartilhar"