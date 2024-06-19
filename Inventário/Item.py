from typing import List

class Item:
    def __init__(self, nome: str, valor_de_regeneracao: int):
        # Inicializa o item com um nome e um valor de regeneração
        self.nome: str = nome
        self.valor_de_regeneracao: int = valor_de_regeneracao

    def get_nome(self) -> str:
        # Retorna o nome do item
        return self.nome

    def get_valor_de_regeneracao(self) -> int:
        # Retorna o valor de regeneração do item
        return self.valor_de_regeneracao

# Lista de itens disponíveis no jogo
itens: List[Item] = [
    Item("Calculadora", 10),  # Item: Calculadora, valor de regeneração: 10
    Item("Video aula no youtube", 15),  # Item: Video aula no youtube, valor de regeneração: 15
    Item("Cafezinho", 20),  # Item: Cafezinho, valor de regeneração: 20
    Item("Pao de queijo", 25),  # Item: Pao de queijo, valor de regeneração: 25
    Item("Dica de veterano", 30),  # Item: Dica de veterano, valor de regeneração: 30
    Item("Monitoria", 35),  # Item: Monitoria, valor de regeneração: 35
    Item("Calculadora cientifica", 45),  # Item: Calculadora cientifica, valor de regeneração: 45
    Item("Pao de queijo recheado", 45),  # Item: Pao de queijo recheado, valor de regeneração: 45
    Item("Abraco da mamae", 50),  # Item: Abraco da mamae, valor de regeneração: 50
    Item("Listas do professor", 30)  # Item: Listas do professor, valor de regeneração: 30
]
