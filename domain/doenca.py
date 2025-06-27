from enuns.cor import Cor
from domain.carta.eventodoenca import Eventodoenca

class Doenca:
    def __init__(self, cor: "Cor"):
        self.cor = cor

    def aumentarnivel(self, eventodoenca: "Eventodoenca") -> None:
        eventodoenca.niveldoenca += 1

    def reduzirnivel(self, eventodoenca: "Eventodoenca") -> None:
        if eventodoenca.niveldoenca > 0:
            eventodoenca.niveldoenca -= 1
