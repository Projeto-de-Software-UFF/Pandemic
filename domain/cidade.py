from typing import List
from domain.carta.construircentropesquisa import Construircentropesquisa
from domain.carta.eventodoenca import Eventodoenca
from domain.carta.bloquearinfeccao import Bloquearinfeccao
from domain.carta.carta import Carta

class Cidade:
    def __init__(self, nome: str):
        self.nome = nome
        self.vizinhacidade: List["Cidade"] = []
        self.centropesquisa: "Construircentropesquisa" = None
        self.eventodoenca: List["Eventodoenca"] = []
        self.bloquearinfeccao: "Bloquearinfeccao" = None

    def adicionarCidadeVizinha(self, vizinhacidade: List["Cidade"]) -> None:
        self.vizinhacidade = vizinhacidade

    def centropesquisa_existe(self) -> bool:
        return self.centropesquisa is not None

    def adicionardoenca(self, eventodoenca: "Eventodoenca") -> None:
        self.eventodoenca.append(eventodoenca)

    def acaoCartaCidade(self, carta: "Carta") -> None:
        pass
        