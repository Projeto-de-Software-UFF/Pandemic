import random
from typing import List
from domain.cidade import Cidade

NUM_CIDADES = 5  # Pode ser alterado facilmente para ajustar o número de cidades

CAPITAIS_BRASILEIRAS = [
    "Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília",
    "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande", "Belo Horizonte",
    "Belém", "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro",
    "Natal", "Porto Alegre", "Porto Velho", "Boa Vista", "Florianópolis",
    "São Paulo", "Aracaju", "Palmas"
]

class GameMap:
    def __init__(self):
        self.map: List[Cidade] = []
        self.cidadesNomes: List[str] = random.sample(CAPITAIS_BRASILEIRAS, NUM_CIDADES)
        self.criarMapa()

    def criarMapa(self) -> None:
        for nome in self.cidadesNomes:
            cidade = Cidade(nome)
            self.map.append(cidade)
        for cidade in self.map:
            if len(cidade.vizinhacidade) == 0:
                possiveis = [
                    c for c in self.map
                    if c != cidade and len(c.vizinhacidade) < 2 and cidade not in c.vizinhacidade
                ]
                if possiveis:
                    escolhido = random.choice(possiveis)
                    cidade.vizinhacidade.append(escolhido)
                    escolhido.vizinhacidade.append(cidade)
        for cidade in self.map:
            while len(cidade.vizinhacidade) < 2:
                possiveis = [
                    c for c in self.map
                    if c != cidade and len(c.vizinhacidade) < 2 and c not in cidade.vizinhacidade
                ]
                if not possiveis:
                    break
                escolhido = random.choice(possiveis)
                cidade.vizinhacidade.append(escolhido)
                escolhido.vizinhacidade.append(cidade)

    def getMap(self) -> List[Cidade]:
        return self.map