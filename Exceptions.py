class numero_invalido(Exception):
    def __init__(self):
        super().__init__("Parece que voce ainda nao aprendeu os numeros direitinho, escolha um numero valido")


class letra_invalida(Exception):
    def __init__(self):
        super().__init__("Ops, parece que voce nao sabe a diferenca entre numeros, letras e caracteres especiais, tudo bem! Tente de novo\n")
