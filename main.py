from Jogo import Jogo
from Jogador import JogadorPrincipal
import os

#Para limpar console os.system('clear')
os.system('cls')
print("Olá, você está preste a participar da casa mais vigiada do Brasil.\n")
print("Antes de você iniciar precisamos saber algumas informações sobre você.\n")
nome = input("Informe o seu nome e sobrenome. Ex: Thiago Leifert :)\n-> ")
nome = nome.lower().title()
peso = int(input("\nInforme o seu peso em Kg. Ex: 68\n-> "))
altura = int(input("\nInforme a sua altura em cm. Ex: 177\n-> "))
jogador_principal = JogadorPrincipal(nome, peso, altura)
jogador_principal.definir_valores_iniciais()

jogo = Jogo(jogador_principal)
os.system('cls')

print(f"Tudo certo, {jogador_principal.nome}. Agora vamos começar!\n")
print("O jogo funciona da seguinte forma, você deverá tentar sobreviver as 13 semanas dentro da casa.\n"
      "Você participará de provas de lider, provas de anjo, crises internas e do paredão.\n")
print("O resultado das provas, das crises e do paredão irão modificar a dinâmica do jogo.\n")
print("Preste atenção nos atributos de seus adversários e tente estabelecer uma estrátegia para vencer.\n")
print("A seguir, você iniciará no jogo.\n\nSão 13 semanas que você deverá tentar sobreviver. BOA SORTE!")
input("\nPressione Enter para prosseguir.")
print("Esses são seus adversários:\n")
jogo.lista_jogadores()
input("\nPressione Enter para prosseguir.")

semana = 1
selecao = -1
while selecao != 0:
    os.system('cls')
    errado = True

    while errado:
        print("=== MENU ===")
        if semana == 1:
            print("[1] Jogar \n\n[2] Status do Jogo\n\n[4] Versão\n\n[0] Abandonar Jogo")
            selecao = input("-> ")
        if semana > 1:
            print("[1] Próxima Semana\n\n[2] Status do Jogo\n\n[3] Roteiro\n\n[4] Versão\n\n[0] Abandonar Jogo")
            selecao = input("-> ")
        if selecao != "1" and selecao != "2" and selecao != "3" and selecao != "4" and selecao != "0":
            input("Por favor, informe um valor válido.")
            os.system('cls')
        else:
            selecao = int(selecao)
            errado = False

    if selecao == 1:
        if len(jogo.jogadores_atuais) == 3 and jogador_principal in jogo.jogadores_atuais:
            os.system('cls')
            print("VOCÊ CHEGOU AOS TRÊS FINALISTAS!")
            print(f"{jogo.jogadores_atuais[0].nome},{jogo.jogadores_atuais[1].nome},{jogo.jogadores_atuais[2].nome}. O público já decidiu quem de vocês merece ser o campeão.")
            input("Pressione Enter para prosseguir.")
            campeao = jogo.campeao_jogo()
            input("\nE O CAMPEÃO DO JOGO FOI......\nPressione Enter para descobrir quem foi o campeão.")
            print(f"PARABÉNS {campeao.nome}!!!! VOCÊ É O CAMPEÃO DO GAME!")
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \\::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'                    <taça desenhada pelo professor da Alura>")
            input()
            break
        os.system('cls')
        print(f"Semana: {semana}")
        jogo.proxima_rodada()
        input("Aperte Enter para prosseguir")
        os.system('cls')
        jogo.acontecer_crise(semana)
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
        jogo.adicionar_roteiro(semana)
        semana = semana + 1
        input("Pressione Enter para a verificar o status do jogo.")
        os.system('cls')
        print(jogo)
        input("\nPressione Enter para continuar")
    if selecao == 2:
        os.system('cls')
        print(jogo)
        input("\nPressione Enter para prosseguir")
    if selecao == 3:
        os.system('cls')
        jogo.exibe_roteiro()
        input("Pressione Enter para retornar ao MENU")
    if selecao == 4:
        os.system('cls')
        print("Versão 1.0:\n"
              "- Sistema de votação randômico.\n"
              "- Sistema de escolha de lider e anjo randômico.\n\n"
              "Versão 1.1:\n"
              "- Correção de erros.\n"
              "- Correção no sistema de votação\n"
              "+ Menu.\n"
              "+ Implementação de atributos de velocidade, resistência e sorte.\n"
              "+ Implementação de Provas interativas.\n"
              "+ Implementação de Provas de acordo com atributo.\n\n"
              "Versão 1.2:\n"
              "- Correção de novos erros.\n"
              "- Correção de nomes e valores morais.\n"
              "+ Implementação do atributo carisma.\n"
              "+ Implementação de crises interativas."
              "+ Novo sistema de votação da maquina.\n"
              "+ Novo sistema de eliminação.\n"
              "+ Implementação da mudança de atributos conforme situação do jogo.\n"
              "+ Implementação de roteiro.\n"
              "+ Atualização de texto e correção ortográfica."
              "\n\n\n\n\n"
              "Desenvolvedor: Rafael de Melo    -    Estudante de Engenharia da Computação                              LL!FB!DM!<-FRV!\n\n"
              "Colaboradores: Felipe \"Pacheco\" Pacheco, Rafael \"KZ\" Caselli\n\n")
        input("Pressione Enter para retornar ao MENU")

print("Essa foi sua trajetória até aqui:")
jogo.exibe_roteiro()
input("Aperte enter para encerrar!")