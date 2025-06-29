from tipo_carta import TipoCarta
from domain.cidade.cidade import Cidade
from domain.jogador.jogador import Jogador

class Carta(TipoCarta):
    # Note que os type hints (Cidade, Jogador) agora se referem às classes importadas.
    def __init__(self, cidade: Cidade, jogador: Jogador):
        self._cidade = cidade
        self._jogador = jogador

    def efeito(self) -> None:
        print(f"Efeito genérico da carta ativado por {self._jogador} na {self._cidade}.")

    def __str__(self) -> str:
        return f"Carta Genérica"