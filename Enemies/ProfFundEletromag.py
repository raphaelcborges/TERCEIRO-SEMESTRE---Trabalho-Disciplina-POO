import random
from Enemies.Inimigo import Inimigo

class ProfFundEletromag(Inimigo):
    def __init__(self, nome: str):
        # Inicializa o professor de Fundamentos de Eletromagnetismo com um nome específico
        super().__init__(nome)
        self.__vida = 50  # Define a vida inicial do professor
        self._ataque = 15  # Define o valor de ataque do professor

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
        # Retorna uma fala aleatória relacionada ao Eletromagnetismo
        fala = self.numero_aleatorio()
        if fala == 1:
            return "Lei de Gauss!\n"
        elif fala == 2:
            return "Lei de Faraday!\n"
        else:
            return "Equações de Maxwell!\n"

    def get_ataque(self) -> int:
        # Retorna o valor de ataque do professor
        return self._ataque
