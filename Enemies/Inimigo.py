import random
from abc import ABC, abstractmethod
from typing import Union

class Inimigo(ABC):
    def __init__(self, nome: str):
        self._nome = nome
        self._vida: Union[int, None] = None
        self._ataque: Union[int, None] = None

    @abstractmethod
    def recebe_dano(self, dano: int) -> None:
        pass

    @abstractmethod
    def esta_vivo(self) -> bool:
        pass

    @abstractmethod
    def print_info(self) -> None:
        pass

    @abstractmethod
    def get_ataque(self) -> Union[int, None]:
        pass

    def get_nome(self) -> str:
        return self._nome

    @abstractmethod
    def ataca(self) -> int:
        pass

    @abstractmethod
    def falar(self) -> str:
        pass

    def numero_aleatorio(self) -> int:
        return random.randint(1, 3)
