from Exceptions import numero_invalido
from typing import List, Union

class Item:
    def __init__(self, nome: str, valor_de_regeneracao: int):
        self._nome = nome
        self._valor_de_regeneracao = valor_de_regeneracao

    def get_nome(self) -> str:
        return self._nome

    def get_valor_de_regeneracao(self) -> int:
        return self._valor_de_regeneracao

class Personagem:
    def __init__(self, nome: str):
        self._nome: str = nome
        self._vida: int = 100
        self._vida_maxima: int = 100
        self._ataque1: int = 27
        self._ataque2: int = 25
        self.inventario: List[Item] = []

    def recebe_dano(self, dano: int) -> None:
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0

    def print_info(self) -> None:
        print("------------------------------------------------------------")
        print(f"{self._nome} | seu NSG: {self._vida} / {self._vida_maxima}")
        print("------------------------------------------------------------")

    def ataca(self, tipo: int) -> int:
        return self._ataque1 if tipo == 1 else self._ataque2

    def esta_vivo(self) -> bool:
        return self._vida > 0

    def definir_nome(self, nome: str) -> None:
        self._nome = nome

    def get_nome(self) -> str:
        return self._nome

    def usar_item(self, indice_item: int) -> None:
        if not isinstance(indice_item, int):
            raise TypeError("O índice do item deve ser um número inteiro")

        if indice_item < 0 or indice_item >= len(self.inventario):
            raise numero_invalido()

        self._vida += self.inventario[indice_item].get_valor_de_regeneracao()
        if self._vida > self._vida_maxima:
            self._vida = self._vida_maxima
        print(f"O item regenerou {self.inventario[indice_item].get_valor_de_regeneracao()} do seu NSG\n")
        self.print_info()
        del self.inventario[indice_item]

    def add_item(self, item: Item) -> None:
        self.inventario.append(item)

    def get_inventario(self) -> List[Item]:
        return self.inventario

    def exibir_inventario(self) -> None:
        if not self.inventario:
            print("Voce abriu sua mochila, mas ela estava vazia :( , nesse tempo o professor escreveu no quadro! Isso vai ser descontado no seu NSG!!! (aperte 1 para voltar)")
            escolha = input()
            while escolha != "1":
                escolha = input()
            return
        print("Inventário:")
        for i, item in enumerate(self.inventario):
            print(f"{i}. {item.get_nome()} (Regenera {item.get_valor_de_regeneracao()} de NSG)")

    def get_vida(self) -> int:
        return self._vida
