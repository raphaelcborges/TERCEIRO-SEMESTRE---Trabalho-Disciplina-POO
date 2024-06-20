class Batalha:
    def __init__(self, personagem, inimigo):
        # Inicializa a batalha com um personagem e um inimigo
        self.personagem = personagem
        self.inimigo = inimigo

    def executa_turno(self, escolha: int) -> None:
        # Executa o turno de ataque do personagem
        dano: int = self.personagem.ataca(escolha)  # O personagem ataca baseado na escolha
        self.inimigo.recebe_dano(dano)  # O inimigo recebe dano
        print(f"Voce foi um bom aluno e a aula do professor ficou {dano} vezes mais facil!\n")

        # Verifica se o inimigo ainda está vivo
        if not self.inimigo.esta_vivo():
            self.personagem.print_info()  # Imprime informações do personagem
            self.inimigo.print_info()  # Imprime informações do inimigo
            print("Voce passou nessa materia!\n")
            return

        # Executa o turno de ataque do inimigo
        dano = self.inimigo.ataca()  # O inimigo ataca
        self.inimigo.falar()  # O inimigo fala
        self.personagem.recebe_dano(dano)  # O personagem recebe dano
        print(f"Mas o professor nao facilitou e voce perdeu {dano} de NSG!\n")

        # Verifica se o personagem ainda está vivo
        if not self.personagem.esta_vivo():
            self.personagem.print_info()  # Imprime informações do personagem
            self.inimigo.print_info()  # Imprime informações do inimigo

    def terminou(self) -> bool:
        # Verifica se a batalha terminou
        return not self.personagem.esta_vivo() or not self.inimigo.esta_vivo()

    def executa_turno_inimigo(self) -> None:
        # Executa o turno de ataque do inimigo, se ambos estiverem vivos
        if not self.personagem.esta_vivo() or not self.inimigo.esta_vivo():
            return

        ataque_inimigo: int = self.inimigo.ataca()  # O inimigo ataca
        self.personagem.recebe_dano(ataque_inimigo)  # O personagem recebe dano
        self.inimigo.falar()  # O inimigo fala
        print(f"O professor não foi legal e você perdeu {ataque_inimigo} de NSG")
