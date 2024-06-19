class Batalha:
    def __init__(self, personagem, inimigo):
        self.personagem = personagem
        self.inimigo = inimigo


    def executa_turno(self, escolha: int) -> None:
        dano: int = self.personagem.ataca(escolha)
        self.inimigo.recebe_dano(dano)
        print(f"Voce foi um bom aluno e a aula do professor ficou {dano} vezes mais facil!\n")

        if not self.inimigo.esta_vivo():
            self.personagem.print_info()
            self.inimigo.print_info()
            print("Voce passou nessa materia!\n")
            return

        dano = self.inimigo.ataca()
        self.inimigo.falar()
        self.personagem.recebe_dano(dano)
        print(f"Mas o professor nao facilitou e voce perdeu {dano} de NSG!\n")

        if not self.personagem.esta_vivo():
            self.personagem.print_info()
            self.inimigo.print_info()

    def terminou(self) -> bool:
        return not self.personagem.esta_vivo() or not self.inimigo.esta_vivo()

    def executa_turno_inimigo(self) -> None:
        if not self.personagem.esta_vivo() or not self.inimigo.esta_vivo():
            return

        ataque_inimigo: int = self.inimigo.ataca()
        self.personagem.recebe_dano(ataque_inimigo)
        self.inimigo.falar()
        print(f"O professor não foi legal e você perdeu {ataque_inimigo} de NSG")
