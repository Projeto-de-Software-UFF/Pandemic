from domain.carta.carta import Carta
from domain.cidade.cidade import Cidade
from domain.jogador.jogador import Jogador

class Bloquearinfeccao(Carta):
    def __init__(self, cidade: Cidade, jogador: Jogador):
        super().__init__(cidade, jogador)

    def efeito(self) -> None:
        """Efeito específico de bloquear infecção."""
        print(f"AÇÃO: {self._jogador} bloqueou a infecção na cidade {self._cidade}.")

    def __str__(self) -> str:
        return f"Carta de Bloquear Infecção"