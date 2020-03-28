from Jogo import Jogo
import os

#Para limpar console os.system('clear')
os.system('cls')
print("Olá, você está participando da casa mais vigiada do Brasil.\n")
print("A primeira coisa que precisamos saber é qual o seu nome.\n")
nome = input("Informe o seu nome e sobrenome. Ex: Thiago Leifert :)\n-> ")

nome = nome.lower().title()
jogo = Jogo(nome)
os.system('cls')

print(f"Tudo certo, {nome}. Agora vamos começar!\n")
print("O jogo funciona da seguinte forma, um lider e um anjo são selecionados entre os participantes e então")
print("haverá uma votação para eliminar um participante.")
print("A seguir você iniciará no jogo.\n\nSão 13 rodadas que você deverá tentar sobreviver. BOA SORTE!")
input("\nPressione Enter para continuar.")
os.system('cls')

rodada = 1

while True:
    print(f"Rodada: {rodada}")
    input("Aperte Enter para prosseguir")
    jogo.definir_lider()
    print(f"\nO ganhador da liderança foi {jogo.lider}. O jogador poderá indicar alguém ao paredão e está imune.")
    input("Pressione Enter para prosseguir")
    jogo.definir_anjo()
    print(f"\nO ganhador do anjo foi {jogo.anjo}. O jogador está imune da votação.")
    input("Pressione Enter para prosseguir")
    print("\n")
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
    input("Pressione Enter para a verificar o status do jogo.")
    os.system('cls')
    print(jogo)
    input("\nPressione Enter para ir para próxima rodada.")
    os.system('cls')

input("Aperte enter para encerrar!")