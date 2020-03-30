import random

class ProvaLider:
    def __init__(self, numero, participantes:list, jogador_principal):
        self.prova_selecionada = numero
        self.participantes = participantes.copy()
        self.jogador_principal = jogador_principal

    def seletor_de_prova(self):
        print("PROVA DO LÍDER.")
        if self.prova_selecionada == 1:
            self.prova_de_resistencia()
        elif self.prova_selecionada == 2:
            self.prova_de_sorte()
        elif self.prova_selecionada == 3:
            self.prova_de_velocidade()
        elif self.prova_selecionada == 4:
            self.prova_interativa_jaula()
        elif self.prova_selecionada == 5:
            self.prova_elimina_jogador()

    def prova_de_sorte(self):
        input("Essa é uma prova de sorte. Os jogadores deverão pegar o máximo de bolinhas que conseguirem."
              "\nPressione Enter para prosseguir.")
        while len(self.participantes) != 1:
            numero_sorte = random.random(0, 200)
            minimo = 200
            removido = 0
            frase_escolhida = random.randrange(1,3)
            lider = 0

            for jogador in self.participantes:
                bolinhas_capturadas = abs(numero_sorte - jogador.sorte)
                if bolinhas_capturadas < minimo:
                    removido = jogador
            if len(self.participantes) > 3:
                if frase_escolhida == 1:
                    input(f"{removido.nome} pegou diversas bolinhas, mas não o suficiente para se manter no jogo e está"
                        f"eliminado.\nPressione Enter para continuar a prova.")
                if frase_escolhida == 2:
                    input(f"{removido.nome} não teve sorte o suficiente na hora de escolher onde ficar para pegar as bolinhas"
                        f"e está eliminado da prova.\nPressione Enter para continuar a prova.")
                if frase_escolhida == 3:
                    input(f"Foi uma disputa assirradicima entre os participantes mas infelizmente {removido.nome} está"
                        f" fora da prova.\nPressione Enter para continuar a prova.")
            elif len(self.participantes) == 3:
                input(f"\nO(A) jogador(a) {removido.nome} saiu da prova. FALTAM APENAS DOIS JOGADORES PARA O NOVO LIDER."
                      f"\nPressione Enter para ver quem é o novo lider.")
            else:
                self.participantes.remove(removido)
                lider = self.participantes[0]
                input(f"\nParabéns {lider.nome} você é o novo lider. Boa sorte da próxima vez {removido.nome}"
                      f"\nPressione Enter para seguir.")
        return lider

    def prova_de_resistencia(self):
        input("Essa é uma prova de resistência. Os jogadores deverão permanecer na mesma posição pelo máximo de tempo possivel."
              "\nPressione Enter para prosseguir.")
        while len(self.participantes) != 1:
            frase_escolhida = random.randrange(1,3)
            minimo = 100
            removido = 0
            lider = 0

            for jogador in self.participantes:
                if jogador.resistencia <= minimo:
                    removido = jogador
            if len(self.participantes) > 3:
                if frase_escolhida == 1:
                    input(f"Após algumas horas de prova, {removido.nome} não supotour e está eliminado.\nPressione Enter"
                          f" para continuar a prova.")
                if frase_escolhida == 2:
                    input(f"Demonstrando cansaço desde o começo, {removido.nome} resistiu ao máximo porém não o suficien"
                          f"te e está eliminado da prova\nPressione Enter para continuar a prova.")
                if frase_escolhida == 3:
                    input(f"Precisamos respeitar os limites do nosso corpo, e com consciência disso {removido.nome} está"
                          f" fora da prova.\nPressione Enter para continuar a prova.")
            elif len(self.participantes) == 3:
                horas_prova = random.randrange(12,48)
                input(f"\nApós mais de {horas_prova}, {removido.nome} não resisti por mais tempo e abandona a prova. "
                      f"FALTAM APENAS DOIS JOGADORES PARA O NOVO LIDER."
                      f"\nPressione Enter para ver quem é o novo lider.")
            else:
                self.participantes.remove(removido)
                lider = self.participantes[0]
                input(f"\nParabéns {lider.nome} você é o novo lider. Boa sorte da próxima vez {removido.nome}"
                      f"\nPressione Enter para seguir.")
        return lider

    def prova_de_velocidade(self):
        input("Essa é uma prova de velocidade e um pouquinho de sorte. Os jogadores deverão percorrer um percurso e coletar alguns itens."
              "Vence o mais veloz com o maior número de itens.\nPressione Enter para prosseguir.")
        maior_quantidade = 0
        lider = 0

        for jogador in self.participantes:
            soma_atributos = jogador.velocidade + jogador.sorte
            if soma_atributos == 200:
                bolas_coletadas = 25
                lider = jogador
                input(f"\n{jogador.nome} foi muito bem e conseguiu coletar todas as {bolas_coletadas} bolas.\nProvavelmente"
                      f"será o novo lider.\nPressione Enter para ver o resultado do próximo jogador.")
            elif 150 <= soma_atributos < 200:
                bolas_coletadas = random.randrange(20,24)
                if bolas_coletadas > maior_quantidade:
                    input(f"\n{jogador.nome} conseguiu capturar {bolas_coletadas} bolas."
                          f"\nPressione Enter para ver o resultado do próximo jogador.")
                    lider = jogador
            elif 100 <= soma_atributos < 150:
                bolas_coletadas = random.randrange(15,19)
                if bolas_coletadas > maior_quantidade:
                    input(f"\n{jogador.nome} não tão veloz, conseguiu pegar {bolas_coletadas} bolas."
                          f"\nPressione Enter para ver o resultado do próximo jogador.")
                    lider = jogador
            else:
                bolas_coletadas = random.randrange(5,14)
                if bolas_coletadas > maior_quantidade:
                    input(f"\n{jogador.nome} coletou {bolas_coletadas} bolas. Não foi uma boa prova para {jogador.nome}"
                        f"\nPressione Enter para ver o resultado do próximo jogador.")
                    lider = jogador
        input(f"\nParabéns {lider.nome}. Você é o novo lider!\nPressione Enter para prosseguir")
        return lider

    def prova_interativa_jaula(self):
        input("Essa é uma prova de escolhas. Selecione dentre das opções qual das jaulas você quer ficar e tente sobreviver na prova"
              "\nPressione Enter para continuar.")
        eliminados = []
        lider = 0

        while len(self.participantes) != 1:
            if len(self.participantes) > 3:
                jaula_salva = random.randrange(1,4)
                for jogador in self.participantes:
                    if len(self.participantes) == 1:
                        lider = jogador
                        print(f"Todos os outros jogadores escolheram uma jaula errada. A jaula correta era {jaula_salva}")
                        input(f"Parabéns {lider.nome}, você é o novo líder!\nPressione Enter para prosseguir.")
                        continue
                    if jogador == self.jogador_principal:
                        chute_jogador = input("\nSelecione a jaula [1], [2], [3] ou [4].\n-> ")
                        if chute_jogador != jaula_salva:
                            self.participantes.remove(jogador)
                            eliminados.append(jogador.nome)
                        if len(self.participantes) == 1 and self.jogador_principal in self.participantes:
                            lider = jogador
                            input(f"Parabéns {lider.nome}, você é o novo líder!")
                        continue
                    chute_maquina = random.randrange(1, 4)
                    if chute_maquina != jaula_salva:
                        input(f"\nO {jogador.nome} foi na jaula {chute_maquina}. Pressione Enter para seguir.")
                        self.participantes.remove(jogador)
                        eliminados.append(jogador.nome)
                if lider == 0:
                    print(f"\nOs seguintes jogadores não escolheram a jaula {jaula_salva} e estão eliminados da prova.")
                    for eliminado in eliminados:
                        print(eliminado)
            elif len(self.participantes) == 3:
                print("\nSobraram apenas 3 jogadores.")
                if self.jogador_principal in self.participantes:
                    jaula_salva = random.randrange(1, 3)
                    chute_jogador = input("\nSelecione a jaula [1], [2] ou [3] .\n-> ")
                    if chute_jogador == jaula_salva:
                        lider = self.jogador_principal
                        input(f"{self.jogador_principal.nome} escolheu a jaula certa e é o novo lider.\n Pressione Enter"
                              f" para prosseguir")
                    elif chute_jogador == 1:
                        chute_maquina = 2
                        if jaula_salva == chute_maquina:
                            print(f"{self.jogador_principal.nome} e {self.participantes[2].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[1].nome} é o novo líder.")
                            lider = self.participantes[1]
                        else:
                            print(f"{self.jogador_principal.nome} e {self.participantes[1].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[2].nome} é o novo líder.")
                            lider = self.participantes[2]
                    elif chute_jogador == 2:
                        chute_maquina = 1
                        if jaula_salva == chute_maquina:
                            print(
                                f"{self.jogador_principal.nome} e {self.participantes[2].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[1].nome} é o novo líder.")
                            lider = self.participantes[1]
                        else:
                            print(
                                f"{self.jogador_principal.nome} e {self.participantes[1].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[2].nome} é o novo líder.")
                            lider = self.participantes[2]
                    elif chute_jogador == 3:
                        chute_maquina = 1
                        if jaula_salva == chute_maquina:
                            print(
                                f"{self.jogador_principal.nome} e {self.participantes[2].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[1].nome} é o novo líder.")
                            lider = self.participantes[1]
                        else:
                            print(
                                f"{self.jogador_principal.nome} e {self.participantes[1].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[2].nome} é o novo líder.")
                            lider = self.participantes[2]
                if not self.jogador_principal in self.participantes:
                    sorteio_lider = random.randrange(0,2)
                    lider = self.participantes[sorteio_lider]
                    input(f"{self.participantes[0].nome}, {self.participantes[0].nome}, {self.participantes[0].nome}, já escolheram suas jaulas."
                          f"\nPressione Enter para descobrir quem é o novo lider.")
                    input(f"\nO novo lider é {lider.nome}! Parabéns!\nPressione Enter para prosseguir.")
            elif len(self.participantes) == 2:
                print("\nSobraram apenas 2 jogadores.")
                if self.jogador_principal in self.participantes:
                    chute_jogador = input("\nSelecione entre a jaula número [1] e a jaula numero [2].\n-> ")
                    jaula_salva = random.randrange(1,2)
                    if chute_jogador == jaula_salva:
                        lider = self.jogador_principal.nome
                        input(f"\nParabéns {lider.nome}, você escolheu a jaula certa e é o novo lider.\nPressione Enter para prosseguir.")
                    else:
                        lider = self.participantes[1]
                        input(f"\nParabéns {lider.nome}, você escolheu a jaula certa e é o novo lider.\nPressione Enter para prosseguir.")
                else:
                    vencedor = random.randrange(0,1)
                    lider = self.participantes[vencedor]
                    input(f"\nParabéns {lider.nome}, você escolheu a jaula certa e é o novo lider.\nPressione Enter para prosseguir.")
        if lider == 0:
            lider = self.participantes[0]
        return lider

    def prova_elimina_jogador(self):
        print("Essa é uma prova de eliminação. Vence o último jogador a ser eliminado.\n")
        while len(self.participantes) != 1:
            for jogador in self.participantes:
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
                        self.participantes.pop(voto)
                else:
                    elimina_jogador = random.randrange(0,(len(self.participantes) - 1))
                    input(f"{jogador.nome} escolheu eliminar {self.participantes[elimina_jogador].nome}.\nPressione Enter para continuar.")
                    self.participantes.pop(elimina_jogador)
                if not self.jogador_principal in self.participantes1:
                    input(f"\nVocê foi eliminado da prova.\nPressione Enter para continuar.")
        lider = self.participantes[0]
        input(f"Parabéns {lider.nome}, você é o novo lider.")
        return lider


'''
    def sorteia_ganhador_prova(self, jogadores):
        participantes = jogadores
        maior_numero = 0
        ganhador = -1

        for count in range(len(participantes)):
            sorteio = random.randrange(0, 100)
            if sorteio > maior_numero:
                maior_numero = sorteio
                ganhador = count
        return participantes[ganhador]
'''

class ProvaAnjo:
    def __init__(self, numero, lider, participantes: list, jogador_principal):
        self.prova_selecionada = numero
        self.lider = lider
        self.participantes = participantes.copy()
        self.jogador_principal = jogador_principal

    def seletor_de_prova(self):
        if self.prova_selecionada == 1:
            self.prova_forca()
        elif self.prova_selecionada == 2:
            self.prova_escolhe_bomba()
        elif self.prova_selecionada == 3:
            self.prova_velocidade_caminho()
        elif self.prova_selecionada == 4:
            self.prova_velocidade()

    def prova_forca(self):
        pass

    def prova_escolhe_bomba(self):
        pass

    def prova_velocidade_caminho(self):
        pass

    def prova_velocidade(self):
        pass

    def prova_sorte(self):
        pass