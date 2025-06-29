from domain.carta.carta import Carta, TipoCarta

class EventoDoenca(Carta):
    def __init__(self, cor: str):
        super().__init__("Evento de Doença", TipoCarta.EPIDEMIA)  # passe nome e tipo para Carta
        self.cor = cor
        self.cubos = []  # Armazena cubos de doença nesta carta (lista de cores, por exemplo)

    def ativar(self, jogo):
        print("⚠️ Evento de doença ativado: uma cidade aleatória sofrerá infecção extra.")
        jogo.aplicar_infeccao_extra()

    def tratar_doenca(self, cor: str, curada: bool = False) -> str:
        cubos_cor = [c for c in self.cubos if c == cor]

        if not cubos_cor:
            return f"Não há cubos da doença {cor} em {self.nome}."

        if curada:
            # Remove todos os cubos da cor
            self.cubos = [c for c in self.cubos if c != cor]
            return f"Todos os cubos da doença {cor} foram removidos de {self.nome}."
        else:
            # Remove apenas um cubo da cor
            for i, c in enumerate(self.cubos):
                if c == cor:
                    del self.cubos[i]
                    break
            return f"Um cubo da doença {cor} foi removido de {self.nome}."
