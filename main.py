from Classes import Jogo
import os

#Para limpar console os.system('clear')

print("Olá, você está participando da casa mais vigiada do Brasil.")
print("A primeira coisa que precisamos saber é qual o seu nome.")
nome = input("Informe o seu nome e sobrenome? Ex: Thiago Leifert :)\n -> ")

nome = nome.lower().title()
jogo = Jogo(nome)
os.system('cls')

print("\n")
print(f"Tudo certo, {nome}. Agora vamos começar!")
print("A seguir você iniciará o jogo.\nSão 16 rodadas que você deverá tentar sobreviver.")
input("Pressione Enter para continuar.")
os.system('cls')

rodada = 1

print("O jogo vai começar")

while rodada <= 16:
    print(f"Rodada: {rodada}")
    jogo.definir_lider()
    print(f"O ganhador da liderança foi {jogo.lider}. O jogador poderá indicar alguém ao paredão e está imune.")
    input("Enter para prosseguir")
    jogo.definir_anjo()
    print(f"O ganhador do anjo foi {jogo.anjo}. O jogador está imune da votação.")
    input("Enter para prosseguir")

    os.system('cls')

    print("VOTAÇÃO:")
    jogo.paredao_eliminacao()

    if jogo.verifica_jogador_eliminado():
        print("FIM DE JOGO")
        input()
        break

    if len(jogo.jogadores_atuais) == 3:
        print("VOCÊ CHEGOU AOS TRÊS FINALISTAS!")
        jogo.campeao_jogo()
        print(f"O ganhador do jogo foi {jogo.campeao_jogo()}")
        input()
        break

    rodada = rodada + 1
    input("Pressione o Enter para a próxima rodada.")
    os.system('clear')

input("Aperte enter para encerrar!")