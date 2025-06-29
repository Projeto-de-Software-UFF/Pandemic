from abc import ABC, abstractmethod

class TipoCarta(ABC):
    @abstractmethod
    def efeito(self) -> None:
        pass