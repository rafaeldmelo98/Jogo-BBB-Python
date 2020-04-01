from Jogo import Jogo
from Jogador import JogadorPrincipal
import os

#Para limpar console os.system('clear')
os.system('cls')
print("Olá, você está participando da casa mais vigiada do Brasil.\n")
print("Mas antes de você iniciar precisamos saber algumas informações sobre você.\n")
nome = input("Informe o seu nome e sobrenome. Ex: Thiago Leifert :)\n-> ")
nome = nome.lower().title()
peso = int(input("Informe o seu peso em Kg. Ex: 68\n-> "))
altura = int(input("Informe a sua altura em cm. Ex: 177\n-> "))
jogador_principal = JogadorPrincipal(nome, peso, altura)
jogador_principal.definir_valores_iniciais()

jogo = Jogo(jogador_principal)
os.system('cls')

print(f"Tudo certo, {jogador_principal.nome}. Agora vamos começar!\n")
print("O jogo funciona da seguinte forma, um lider e um anjo são selecionados entre os participantes e então")
print("haverá uma votação para eliminar um participante.")
print("A seguir você iniciará no jogo.\n\nSão 13 rodadas que você deverá tentar sobreviver. BOA SORTE!")
print("\nEsses são todos os jogadores que participarão.")
jogo.lista_jogadores()
input("\nPressione Enter para continuar.")

rodada = 1
selecao = 0
while selecao != 9:
    os.system('cls')
    print("MENU")
    print("[1] Jogar / Próxima Rodada\n[2] Status de Jogo\n[9] Abandonar Jogo")
    selecao = input("-> ")


    if not selecao != "" and int(selecao) != (1 or 2 or 9):
        input("Por favor, informe um valor válido.")
    else:
        selecao = int(selecao)
    if selecao == 1:
        if len(jogo.jogadores_atuais) == 3 and jogador_principal in jogo.jogadores_atuais:
            os.system('cls')
            print("VOCÊ CHEGOU AOS TRÊS FINALISTAS!")
            print(f"{jogo.jogadores_atuais[0].nome},{jogo.jogadores_atuais[1].nome},{jogo.jogadores_atuais[2].nome}. O público já decidiu quem de vocês merece ser o campeão.")
            input("Pressione Enter para prosseguir.")
            campeao = jogo.campeao_jogo()
            input("\nE O CAMPEÃO DO JOGO FOI......\nPressione Enter para descobrir quem foi o campeão.")
            print(f"PARABÉNS {campeao.nome}!!!! VOCÊ É O CAMPEÃO DO GAME!")
            input()
            break
        os.system('cls')
        print(f"Rodada: {rodada}")
        jogo.proxima_rodada()
        input("Aperte Enter para prosseguir")
        os.system('cls')
        jogo.definir_lider()
        os.system('cls')
        jogo.definir_anjo()
        os.system('cls')
        print(f"O lider {jogo.lider.nome} poderá indicar alguém ao paredão e está imune da votação.")
        print(f"\nO anjo {jogo.anjo.nome} está imune da votação.")
        input("\nPressione Enter para continuar")
        print("\n")
        print("VOTAÇÃO:")
        jogo.paredao_eliminacao()
        if jogo.verifica_jogador_eliminado():
            print("FIM DE JOGO")
            input()
            break

        rodada = rodada + 1
        input("Pressione Enter para a verificar o status do jogo.")
        os.system('cls')
        print(jogo)
        input("\nPressione Enter para continuar")
    if selecao == 2:
        print(jogo)
        input("\nPressione Enter para prosseguir")

input("Aperte enter para encerrar!")