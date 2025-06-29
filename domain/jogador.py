class Jogador:   
    def __init__(self, posicao):
        self.posicao = posicao

    def moverJogador(self, cidade):
        if cidade in self.posicao.vizinhacidade:
            self.posicao = cidade
            print(f"Jogador agora está em {self.posicao.nome}.")
        else:
            print(f"A cidade {cidade.nome} não é vizinha de {self.posicao.nome}.")
        
    def teletransportar(self, cidade):
        self.posicao = cidade
        print(f"Jogador teletransportado para {cidade.nome}")
        