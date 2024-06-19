import random
from Character.Personagem import Personagem
from Enemies.ProfCalculo3 import ProfCalculo3
from Enemies.ProfPOO import ProfPOO
from Enemies.ProfFundEletromag import ProfFundEletromag
from Enemies.ProfFundMecFlu import ProfFundMecFlu
from Enemies.ProfLabSistemasDigitais import ProfLabSD
from Enemies.ProfEDA import ProfEDA
from Batalha import Batalha
from Inventário.Item import itens
from Extra import Extra
from Exceptions import letra_invalida, numero_invalido




def ler_int() -> int:
    while True:
        try:
            return int(input())
        except ValueError:
            print(letra_invalida())

def escolha_menu() -> int:
    while True:
        try:
            print("Escolha uma opcao:")
            print("1. Primeiro dia de aula (inicia o jogo)")
            print("2. Creditos")
            print("3. Trancar o curso (sair)\n")
            escolha = ler_int()
            if 1 <= escolha <= 3:
                return escolha
            else:
                raise numero_invalido()
        except numero_invalido as e:
            print(e)

def vitoria(vida: int):
    print("------------------------------------------------------------- \n")
    print("Uauu! Parece que voce conseguiu passar do terceiro semestre\n")
    print(f"Seu NSG final é de {vida}, o que significa que no boletim voce tem um: ")

    if vida >= 90:
        Extra.print_a()
    elif 80 <= vida < 90:
        Extra.print_b()
    elif 70 <= vida < 80:
        Extra.print_c()
    elif 60 <= vida < 70:
        Extra.print_d()
    elif 50 <= vida < 60:
        print("Parece que mesmo passando, seu NSG ficou abaixo de 60, mas por misericordia os professores arredondaram, agradeca\n")
        Extra.print_d()
    else:
        Extra.print_e()
        print("Parece que mesmo passando, seu NSG ficou abaixo de 50, ou seja, sua média ficou abaixo do ideal, JOGUE novamente!\n")

def iniciar_jogo() -> None:
    while True:
        nome = input("Antes de começar, me diga seu nome: \n")
        if nome.isalpha():
            break
        else:
            print(letra_invalida())

    personagem = Personagem(nome)

    inimigos = [
        ProfCalculo3("Professor de Calculo3"),
        ProfFundMecFlu("Professor de Fundamentos de Mecanica dos Fluidos"),
        ProfLabSD("Professor de Laboratorio de Sistemas Digitais"),
        ProfFundEletromag("Professor de Fundamentos de Eletromagnetismo"),
        ProfEDA("Professor de Equações Diferenciais A"),
        ProfPOO("Professor de Programação Orientada a Objetos"),
    ]

    for i in range(len(inimigos)):
        print(f"Voce entrou na sala do {inimigos[i].get_nome()}\n")
        batalha = Batalha(personagem, inimigos[i])

        while not batalha.terminou():
            personagem.print_info()
            inimigos[i].print_info()
            print("O que voce quer fazer?\n1. Fazer pergunta\n2. Sentar na primeira cadeira\n3. Usar um item especial\n4. Trancar o curso")
            escolha = ler_int()

            if escolha == 3:
                personagem.exibir_inventario()
                if personagem.get_inventario():
                    print("Escolha um item para usar: ")
                    item_escolhido = ler_int()
                    personagem.usar_item(item_escolhido)
                batalha.executa_turno_inimigo()
            elif escolha in [1, 2]:
                batalha.executa_turno(escolha)
            elif escolha == 4:
                print("Ja no terceiro semestre? ok, nao vou te impedir, adeus!")
                exit(0)
            else:
                print("Escolha um numero dentro das opcoes, nem vem...")

        if not personagem.esta_vivo():
            print("Voce reprovou na materia...\n")
            Extra.reprovacao()
            break
        else:
            if i != len(inimigos) - 1:
                print("Parabens!\n")
            if i < len(inimigos) - 1:
                print("O que voce quer fazer agora?\n1. Ir para a proxima aula\n2. Dar uma passadinha no DA\n3. Trancar o curso\n")
                escolha = ler_int()
                if escolha == 1:
                    continue
                elif escolha == 2:
                    item_aleatorio = random.choice(itens)
                    personagem.add_item(item_aleatorio)
                    print(f"Na sua passadinha pelo hall da engenharia voce adquiriu {item_aleatorio.get_nome()}!\n")
                    print("Mas agora voce esta super atrasado pra sua aula entao voce correu e...\n")
                elif escolha == 3:
                    print("Ja no terceiro semestre? ok, nao vou te impedir, adeus!")
                    exit(0)
                else:
                    print("Escolha um numero dentro das opcoes, nem vem...")
            else:
                vitoria(personagem.get_vida())
                exit(0)

    if personagem.esta_vivo():
        print("Vitoria! Voce derrotou todos os inimigos!\n")

def main() -> None:
    Extra.iniciar()
    sair_do_jogo = False

    while not sair_do_jogo:
        escolha_menu_inicial = escolha_menu()
        if escolha_menu_inicial == 1:
            iniciar_jogo()
        elif escolha_menu_inicial == 2:
            Extra.creditos()
            while True:
                print("Agora que voce viu nossos nomes, decida:\n1. Primeiro dia de aula (inicia o jogo)\n2. Trancar o curso (sair)\n")
                escolha_alunos = ler_int()
                if escolha_alunos == 1:
                    iniciar_jogo()
                elif escolha_alunos == 2:
                    sair_do_jogo = True
                    print("Ja no terceiro semestre? ok, nao vou te impedir, adeus!")
                    break
                else:
                    print("Vou te mostrar nossos nomes de novo, mas escolha 1 ou 2 e pare de inventar hein..\n")
        elif escolha_menu_inicial == 3:
            print("Ja no terceiro semestre? ok, nao vou te impedir, adeus!")
            sair_do_jogo = True

if __name__ == "__main__":
    main()
