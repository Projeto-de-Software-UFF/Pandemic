from domain.carta.carta import Carta, TipoCarta

class Construircentropesquisa(Carta):
    def __init__(self, nome: str):
        super().__init__(nome, TipoCarta.CIDADE)

    def ativar(self, jogo):
        cidade = input("🏙️ Digite o nome da cidade para construir o centro de pesquisa: ")
        jogo.construir_centro_pesquisa(cidade)
