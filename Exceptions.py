class numero_invalido(Exception):
    # Exceção personalizada para números inválidos
    def __init__(self):
        # Chama o inicializador da superclasse com uma mensagem específica
        super().__init__("Parece que voce ainda nao aprendeu os numeros direitinho, escolha um numero valido")


class letra_invalida(Exception):
    # Exceção personalizada para letras inválidas
    def __init__(self):
        # Chama o inicializador da superclasse com uma mensagem específica
        super().__init__("Ops, parece que voce nao sabe a diferenca entre numeros, letras e caracteres especiais, tudo bem! Tente de novo\n")
