from Classes import Jogo
from Classes import Jogador
import os

#Para limpar console os.system('clear')

print("Olá, você está participando da casa mais vigiada do Brasil.")
print("A primeira coisa que precisamos saber é qual o seu nome.")
nome = input("Informe o seu nome e sobrenome? Ex: Thiago Leifert :)\n")

nome = nome.lower().title()
jogador_principal = Jogador(nome)
jogo = Jogo(jogador_principal.nome)

print(f"Tudo certo, {jogador_principal}. Agora vamos começar!")
print("A seguir você iniciará o jogo.\n São 16 rodadas que você deverá tentar sobreviver.")

acao = -1
rodada = 16

print("O jogo vai começar")
while 0 <= acao >= 8:
    print("Selecione uma das opções\n[1]Seguir jogo.\n[2]Status de jogo.")
    if 1:
        print(f"Rodada: {rodada}")
        jogo.definir_lider()
        print(f"O ganhador da liderança foi {jogo.lider}")
        jogo.definir_anjo()
        print(f"O ganhador do anjo foi {jogo.anjo}. O jogador está imune da votação.")



    if 2:
        print(jogo)