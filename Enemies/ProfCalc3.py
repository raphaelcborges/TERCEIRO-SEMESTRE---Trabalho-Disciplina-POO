import random
from Enemies.Inimigo import Inimigo

class ProfCalculo3(Inimigo):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.__vida = 40
        self._ataque = 8

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, novo_valor):
        if novo_valor < 0:
            self.__vida = 0
        else:
            self.__vida = novo_valor

    def recebe_dano(self, dano: int) -> None:
        self.vida -= dano

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def print_info(self) -> None:
        print("------------------------------------------------------------")
        print(f"{self.get_nome()} | Dificuldade (vida): {self.vida}")
        print("------------------------------------------------------------\n")

    def ataca(self) -> int:
        return self._ataque

    def falar(self) -> str:
        fala = self.numero_aleatorio()
        if fala == 1:
            return "Integrais Triplas!\n"
        elif fala == 2:
            return "Teorema de Green!\n"
        else:
            return "Teorema de Gauss!\n"

    def get_ataque(self) -> int:
        return self._ataque



