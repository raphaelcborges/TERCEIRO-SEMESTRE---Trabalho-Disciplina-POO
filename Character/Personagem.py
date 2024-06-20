from typing import List
from Inventário.Item import Item, itens  
from Exceptions import numero_invalido  

class Personagem:
    def __init__(self, nome: str):
        self._nome: str = nome  # Nome do personagem
        self._vida: int = 100  # Vida inicial do personagem
        self._vida_maxima: int = 100  # Vida máxima do personagem
        self._ataque1: int = 27  # Valor de ataque 1 do personagem
        self._ataque2: int = 25  # Valor de ataque 2 do personagem
        self.inventario: List[Item] = []  # Lista de itens do inventário do personagem

    def recebe_dano(self, dano: int) -> None:
        """ Método para reduzir a vida do personagem após receber um dano """
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0  # Garante que a vida não seja negativa

    def print_info(self) -> None:
        """ Método para imprimir informações do personagem """
        print("------------------------------------------------------------")
        print(f"{self._nome} | seu NSG: {self._vida} / {self._vida_maxima}")
        print("------------------------------------------------------------")

    def ataca(self, tipo: int) -> int:
        """ Método para determinar o valor de ataque do personagem com base no tipo """
        return self._ataque1 if tipo == 1 else self._ataque2

    def esta_vivo(self) -> bool:
        """ Método para verificar se o personagem está vivo """
        return self._vida > 0

    def definir_nome(self, nome: str) -> None:
        """ Método para definir o nome do personagem """
        self._nome = nome

    def get_nome(self) -> str:
        """ Método para obter o nome do personagem """
        return self._nome

    def usar_item(self, indice_item: int) -> None:
        """ Método para usar um item do inventário """
        if not isinstance(indice_item, int):
            raise TypeError("O índice do item deve ser um número inteiro")  # Verifica se o índice do item é um inteiro

        if indice_item < 0 or indice_item >= len(self.inventario):
            raise numero_invalido()  # Lança a exceção numero_invalido se o índice do item for inválido

        # Regenera a vida do personagem com o valor do item e limita à vida máxima
        self._vida += self.inventario[indice_item].get_valor_de_regeneracao()
        if self._vida > self._vida_maxima:
            self._vida = self._vida_maxima

        # Exibe mensagem informando quanto foi regenerado e imprime as informações do personagem
        print(f"O item regenerou {self.inventario[indice_item].get_valor_de_regeneracao()} do seu NSG\n")
        self.print_info()

        # Remove o item do inventário após ser utilizado
        del self.inventario[indice_item]

    def add_item(self, item: Item) -> None:
        """ Método para adicionar um item ao inventário do personagem """
        self.inventario.append(item)

    def get_inventario(self) -> List[Item]:
        """ Método para obter o inventário completo do personagem """
        return self.inventario

    def exibir_inventario(self) -> None:
        """ Método para exibir todos os itens do inventário do personagem """
        if not self.inventario:
            # Se o inventário estiver vazio, solicita que o usuário pressione 1 para voltar
            print("Voce abriu sua mochila, mas ela estava vazia :( , nesse tempo o professor escreveu no quadro! Isso vai ser descontado no seu NSG!!! (aperte 1 para voltar)")
            escolha = input()
            while escolha != "1":
                escolha = input()
            return

        # Caso contrário, exibe todos os itens do inventário com seus respectivos valores de regeneração
        print("Inventário:")
        for i, item in enumerate(self.inventario):
            print(f"{i}. {item.get_nome()} (Regenera {item.get_valor_de_regeneracao()} de NSG)")

    def get_vida(self) -> int:
        """ Método para obter o valor atual de vida do personagem """
        return self._vida
