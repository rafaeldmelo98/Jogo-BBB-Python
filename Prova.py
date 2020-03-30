import random

class Prova:
    def __init__(self, numero, participantes:list, jogador_principal, tipo_de_prova):
        self.prova_selecionada = numero
        self.participantes = participantes.copy()
        self.jogador_principal = jogador_principal
        if tipo_de_prova == 1:
            self.tipo_de_prova = "líder"
        else:
            self.tipo_de_prova = "anjo"

    def seletor_de_prova(self):
        print(f"PROVA DO {self.tipo_de_prova.upper()}.")
        ganhador = 0
        if self.prova_selecionada == 1:
            ganhador = self.prova_elimina_jogador()
        elif self.prova_selecionada == 2:
            ganhador = self.prova_de_sorte()
        elif self.prova_selecionada == 3:
            ganhador = self.prova_de_velocidade()
        elif self.prova_selecionada == 4:
            ganhador = self.prova_interativa_jaula()
        elif self.prova_selecionada == 5:
            ganhador = self.prova_de_resistencia()
        return ganhador

    def prova_de_sorte(self):
        input("Essa é uma prova de sorte. Os jogadores deverão pegar o máximo de bolinhas que conseguirem. O primeiro a"
              " conseguir capturar o maior número de bolinhas ganha."
              "\nPressione Enter para prosseguir.")
        while len(self.participantes) != 1:
            numero_sorte = random.randrange(0, 200)
            minimo = 200
            removido = 0
            frase_escolhida = random.randrange(1,3)
            ganhador = 0

            for jogador in self.participantes:
                bolinhas_capturadas = abs(numero_sorte - jogador.sorte)
                if bolinhas_capturadas < minimo:
                    minimo = bolinhas_capturadas
                    removido = jogador
            if len(self.participantes) > 3:
                if frase_escolhida == 1:
                    input(f"\n{removido.nome} pegou diversas bolinhas, mas não o suficiente para se manter no jogo e está"
                        f" eliminado.\nPressione Enter para continuar a prova.")
                    self.participantes.remove(removido)
                if frase_escolhida == 2:
                    input(f"\n{removido.nome} não teve sorte o suficiente na hora de escolher onde ficar para pegar as bolinhas"
                        f" e está eliminado da prova.\nPressione Enter para continuar a prova.")
                    self.participantes.remove(removido)
                if frase_escolhida == 3:
                    input(f"\nFoi uma disputa acirradissima entre os participantes mas infelizmente {removido.nome} está"
                        f" fora da prova.\nPressione Enter para continuar a prova.")
                    self.participantes.remove(removido)
            elif len(self.participantes) == 3:
                input(f"\nO(A) jogador(a) {removido.nome} saiu da prova. FALTAM APENAS DOIS JOGADORES PARA O NOVO {self.tipo_de_prova.upper()}."
                      f"\nPressione Enter para ver quem é o novo ganhador.")
                self.participantes.remove(removido)
            else:
                self.participantes.remove(removido)
                ganhador = self.participantes[0]
                input(f"\nParabéns {ganhador.nome} você é o novo {self.tipo_de_prova}. Boa sorte da próxima vez {removido.nome}."
                      f"\nPressione Enter para seguir.")
        return ganhador

    def prova_de_resistencia(self):
        input("Essa é uma prova de resistência. Os jogadores deverão permanecer na mesma posição pelo máximo de tempo possivel."
              "\nPressione Enter para prosseguir.")
        while len(self.participantes) != 1:
            frase_escolhida = random.randrange(1,3)
            minimo = 100
            removido = 0
            ganhador = 0

            for jogador in self.participantes:
                if jogador.resistencia <= minimo:
                    removido = jogador
            if len(self.participantes) > 3:
                if frase_escolhida == 1:
                    input(f"Após algumas horas de prova, {removido.nome} não suportou e está eliminado.\nPressione Enter"
                          f" para continuar a prova.")
                    self.participantes.remove(removido)
                if frase_escolhida == 2:
                    input(f"Demonstrando cansaço desde o começo, {removido.nome} resistiu ao máximo, porém não o suficiente"
                          f" e está eliminado da prova\nPressione Enter para continuar a prova.")
                    self.participantes.remove(removido)
                if frase_escolhida == 3:
                    input(f"Precisamos respeitar os limites do nosso corpo, e com consciência disso {removido.nome} está"
                          f" fora da prova.\nPressione Enter para continuar a prova.")
                    self.participantes.remove(removido)
            elif len(self.participantes) == 3:
                horas_prova = random.randrange(12,48)
                input(f"\nApós mais de {horas_prova}, {removido.nome} não resisti por mais tempo e abandona a prova. "
                      f"FALTAM APENAS DOIS JOGADORES PARA O NOVO {self.tipo_de_prova.upper()}."
                      f"\nPressione Enter para ver quem é o novo {self.tipo_de_prova}.")
                self.participantes.remove(removido)
            else:
                self.participantes.remove(removido)
                ganhador = self.participantes[0]
                input(f"\nParabéns {ganhador.nome} você é o novo {self.tipo_de_prova}. Boa sorte da próxima vez {removido.nome}"
                      f"\nPressione Enter para seguir.")
        return ganhador

    def prova_de_velocidade(self):
        input("Essa é uma prova de velocidade e um pouquinho de sorte. Os jogadores deverão percorrer um percurso e coletar alguns itens."
              "\nVence o mais veloz com o maior número de itens.\nPressione Enter para prosseguir.")
        maior_quantidade = 0
        ganhador = 0

        for jogador in self.participantes:
            soma_atributos = jogador.velocidade + jogador.sorte
            if soma_atributos == 200:
                bolas_coletadas = 25
                maior_quantidade = bolas_coletadas
                ganhador = jogador
                input(f"\n{jogador.nome} foi muito bem e conseguiu coletar todas as {bolas_coletadas} bolas.\nProvavelmente"
                      f"será o novo {self.tipo_de_prova}.\nPressione Enter para ver o resultado do próximo jogador.")
            elif 150 <= soma_atributos < 200:
                bolas_coletadas = random.randrange(20,24)
                input(f"\n{jogador.nome} conseguiu capturar {bolas_coletadas} bolas."
                      f"\nPressione Enter para ver o resultado do próximo jogador.")
                if bolas_coletadas > maior_quantidade:
                    maior_quantidade = bolas_coletadas
                    ganhador = jogador
            elif 100 <= soma_atributos < 150:
                bolas_coletadas = random.randrange(15,19)
                input(f"\n{jogador.nome} não tão veloz, conseguiu pegar {bolas_coletadas} bolas."
                      f"\nPressione Enter para ver o resultado do próximo jogador.")
                if bolas_coletadas > maior_quantidade:
                    maior_quantidade = bolas_coletadas
                    ganhador = jogador
            else:
                bolas_coletadas = random.randrange(5,14)
                input(f"\n{jogador.nome} coletou {bolas_coletadas} bolas. Não foi uma boa prova para {jogador.nome}."
                      f"\nPressione Enter para ver o resultado do próximo jogador.")
                if bolas_coletadas > maior_quantidade:
                    maior_quantidade = bolas_coletadas
                    ganhador = jogador
        input(f"\nParabéns {ganhador.nome}. Você é o novo {self.tipo_de_prova}!\nPressione Enter para prosseguir")
        return ganhador

    def prova_interativa_jaula(self):
        input("Essa é uma prova de escolhas. Selecione dentre das opções qual das jaulas você quer ficar e tente sobreviver na prova"
              "\nPressione Enter para continuar.")
        eliminados = []
        ganhador = 0

        while len(self.participantes) != 1:
            if len(self.participantes) > 3:
                jaula_salva = random.randrange(1,4)
                for jogador in self.participantes:
                    if len(self.participantes) == 1:
                        ganhador = jogador
                        print(f"Todos os outros jogadores escolheram uma jaula errada. A jaula correta era {jaula_salva}")
                        input(f"Parabéns {ganhador.nome}, você é o novo {self.tipo_de_prova}!\nPressione Enter para prosseguir.")
                        return ganhador
                    if jogador == self.jogador_principal:
                        chute_jogador = input("\nSelecione a jaula [1], [2], [3] ou [4].\n-> ")
                        if chute_jogador != jaula_salva:
                            self.participantes.remove(jogador)
                            eliminados.append(jogador.nome)
                        if len(self.participantes) == 1 and self.jogador_principal in self.participantes:
                            ganhador = jogador
                            input(f"Parabéns {ganhador.nome}, você é o novo {self.tipo_de_prova}!")
                            return ganhador
                    else:
                        chute_maquina = random.randrange(1, 4)
                        input(f"\nO {jogador.nome} foi na jaula {chute_maquina}. Pressione Enter para seguir")
                        if chute_maquina != jaula_salva:
                            self.participantes.remove(jogador)
                            eliminados.append(jogador.nome)
                print(f"\nA jaula correta é a {jaula_salva}.")
                if ganhador == 0:
                    print(f"\nOs seguintes jogadores não escolheram a jaula {jaula_salva} e estão eliminados da prova.")
                    for eliminado in eliminados:
                        print(eliminado)
            elif len(self.participantes) == 3:
                print("\nSobraram apenas 3 jogadores.")
                if self.jogador_principal in self.participantes:
                    jaula_salva = random.randrange(1, 3)
                    chute_jogador = input("\nSelecione a jaula [1], [2] ou [3] .\n-> ")
                    if chute_jogador == jaula_salva:
                        ganhador = self.jogador_principal
                        input(f"{self.jogador_principal.nome} escolheu a jaula certa e é o novo {self.tipo_de_prova}.\n Pressione Enter"
                              f" para prosseguir")
                    elif chute_jogador == 1:
                        chute_maquina = 2
                        if jaula_salva == chute_maquina:
                            print(f"{self.jogador_principal.nome} e {self.participantes[2].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[1].nome} é o novo {self.tipo_de_prova}.")
                            ganhador = self.participantes[1]
                        else:
                            print(f"{self.jogador_principal.nome} e {self.participantes[1].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[2].nome} é o novo {self.tipo_de_prova}.")
                            ganhador = self.participantes[2]
                    elif chute_jogador == 2:
                        chute_maquina = 1
                        if jaula_salva == chute_maquina:
                            print(
                                f"{self.jogador_principal.nome} e {self.participantes[2].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[1].nome} é o novo {self.tipo_de_prova}.")
                            ganhador = self.participantes[1]
                        else:
                            print(
                                f"{self.jogador_principal.nome} e {self.participantes[1].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[2].nome} é o novo {self.tipo_de_prova}.")
                            ganhador = self.participantes[2]
                    elif chute_jogador == 3:
                        chute_maquina = 1
                        if jaula_salva == chute_maquina:
                            print(
                                f"{self.jogador_principal.nome} e {self.participantes[2].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[1].nome} é o novo {self.tipo_de_prova}.")
                            ganhador = self.participantes[1]
                        else:
                            print(f"{self.jogador_principal.nome} e {self.participantes[1].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[2].nome} é o novo {self.tipo_de_prova}.")
                            ganhador = self.participantes[2]

                    return ganhador
                else:
                    sorteio_ganhador = random.randrange(0,2)
                    ganhador = self.participantes[sorteio_ganhador]
                    input(f"{self.participantes[0].nome}, {self.participantes[1].nome}, {self.participantes[2].nome}, já escolheram suas jaulas."
                          f"\nPressione Enter para descobrir quem é o novo {self.tipo_de_prova}.")
                    input(f"\nO novo {self.tipo_de_prova} é {ganhador.nome}! Parabéns!\nPressione Enter para prosseguir.")

                    return ganhador
            elif len(self.participantes) == 2:
                print("\nSobraram apenas 2 jogadores.")
                if self.jogador_principal in self.participantes:
                    chute_jogador = input("\nSelecione entre a jaula número [1] e a jaula numero [2].\n-> ")
                    jaula_salva = random.randrange(1,2)
                    if chute_jogador == jaula_salva:
                        ganhador = self.jogador_principal.nome
                        input(f"\nParabéns {ganhador.nome}, você escolheu a jaula certa e é o novo {self.tipo_de_prova}.\nPressione Enter para prosseguir.")
                        return ganhador
                    else:
                        ganhador = self.participantes[1]
                        input(f"\nParabéns {ganhador.nome}, você escolheu a jaula certa e é o novo {self.tipo_de_prova}.\nPressione Enter para prosseguir.")
                        return ganhador
                else:
                    vencedor = random.randrange(0,1)
                    ganhador = self.participantes[vencedor]
                    input(f"\nParabéns {ganhador.nome}, você escolheu a jaula certa e é o novo {self.tipo_de_prova}.\nPressione Enter para prosseguir.")
                    return ganhador
        if ganhador == 0:
            ganhador = self.participantes[0]
        return ganhador

    def prova_elimina_jogador(self):
        input("Essa é uma prova de eliminação. Vence o último jogador a ser eliminado.\nPressione Enter para prosseguir.")
        informado = False
        while len(self.participantes) != 1:
            for jogador in self.participantes:
                jogador_disponivel = self.participantes.copy()
                if jogador == self.jogador_principal:
                    for jogador in self.participantes:
                        if jogador == self.jogador_principal:
                            continue
                        print(f"[{self.participantes.index(jogador)}] - {jogador.nome}")
                    voto = int(input("\nVote em um jogador para ser eliminado.\n->"))
                    while 0 > voto > len(jogador):
                        print("\nInforme um número válido de jogador.")
                        voto = int(input("Vote em um jogador para ser eliminado.\n-> "))
                        print("\n")
                    print(f"{self.jogador_principal.nome} eliminou {self.participantes[voto].nome}\n")
                    self.participantes.pop(voto)
                else:
                    elimina_jogador = random.randrange(0,(len(self.participantes) - 1))
                    jogador_disponivel.remove(jogador)
                    input(f"{jogador.nome} escolheu eliminar {jogador_disponivel[elimina_jogador].nome}.Pressione Enter para continuar\n.")
                    self.participantes.remove(jogador_disponivel[elimina_jogador])
                if not self.jogador_principal in self.participantes and informado == False:
                    informado = True
                    input(f"\nVocê foi eliminado da prova.\nPressione Enter para continuar.\n")
        ganhador = self.participantes[0]
        input(f"Parabéns {ganhador.nome}, você é o novo {self.tipo_de_prova}.")
        return ganhador