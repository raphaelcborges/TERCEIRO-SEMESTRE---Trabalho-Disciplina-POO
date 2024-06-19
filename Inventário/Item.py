from typing import List

class Item:
    def __init__(self, nome: str, valor_de_regeneracao: int):
        self.nome: str = nome
        self.valor_de_regeneracao: int = valor_de_regeneracao

    def get_nome(self) -> str:
        return self.nome

    def get_valor_de_regeneracao(self) -> int:
        return self.valor_de_regeneracao

itens: List[Item] = [
    Item("Calculadora", 10),
    Item("Video aula no youtube", 15),
    Item("Cafezinho", 20),
    Item("Pao de queijo", 25),
    Item("Dica de veterano", 30),
    Item("Monitoria", 35),
    Item("Calculadora cientifica", 45),
    Item("Pao de queijo recheado", 45),
    Item("Abraco da mamae", 50),
    Item("Listas do professor", 30)
]
