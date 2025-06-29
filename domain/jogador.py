class Jogador:   
    def __init__(self, posicao):
        self.posicao = posicao

    def moverJogador(self, cidade):
        self.posicao = cidade
        print(f"Jogador movido para {cidade.nome}")
        
    def teletransportar(self, cidade):
        self.posicao = cidade
        print(f"Jogador teletransportado para {cidade.nome}")
        