import random
from Enemies.Inimigo import Inimigo

class ProfPOO(Inimigo):
    def __init__(self, nome: str):
        # Inicializa o professor de POO com um nome específico
        super().__init__(nome)
        self.__vida = 45  # Define a vida inicial do professor
        self._ataque = 12  # Define o valor de ataque do professor

    @property
    def vida(self):
        # Retorna a vida atual do professor
        return self.__vida

    @vida.setter
    def vida(self, novo_valor):
        # Define um novo valor para a vida, garantindo que não seja menor que 0
        if novo_valor < 0:
            self.__vida = 0
        else:
            self.__vida = novo_valor

    def recebe_dano(self, dano: int) -> None:
        # Reduz a vida do professor com base no dano recebido
        self.vida -= dano

    def esta_vivo(self) -> bool:
        # Verifica se o professor ainda está vivo (vida > 0)
        return self.vida > 0

    def print_info(self) -> None:
        # Imprime informações sobre o professor, incluindo seu nome e vida atual
        print("------------------------------------------------------------")
        print(f"{self.get_nome()} | Dificuldade (vida): {self.vida}")
        print("------------------------------------------------------------\n")

    def ataca(self) -> int:
        # Retorna o valor de ataque do professor
        return self._ataque

    def falar(self) -> str:
        # Retorna uma fala aleatória relacionada à POO
        fala = self.numero_aleatorio()
        if fala == 1:
            return "Encapsulamento!\n"
        elif fala == 2:
            return "Herança!\n"
        else:
            return "Polimorfismo!\n"

    def get_ataque(self) -> int:
        # Retorna o valor de ataque do professor
        return self._ataque
