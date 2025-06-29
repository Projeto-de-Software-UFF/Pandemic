from typing import List
from domain.cidade import Cidade

class GameMap:
    def __init__(self):
        self.map: List["Cidade"] = []
        self.cidadesNomes: List[str] = [
            'Rio de Janeiro',
            'São Paulo',
            'Baia']
        
        self.criarMapa()

    def criarMapa(self) -> None:
        for nome in self.cidadesNomes:
            cidade = Cidade(nome)
            self.map.append(cidade)

    def getMap(self) -> List["Cidade"]:
        return self.map