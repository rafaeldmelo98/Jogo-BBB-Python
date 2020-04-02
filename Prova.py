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
        input("Essa é uma prova de sorte. Os jogadores deverão pegar o máximo de bolinhas que conseguirem antes do tempo"
              " acabar. \nO primeiro a conseguir capturar o maior número de bolinhas ganha."
              "\n\nJogadores com maior sorte tem mais chance de ganhar."
              "\nPressione Enter para prosseguir.")

        jogador_upado = []

        while len(self.participantes) != 1:
            minimo = 200
            removido = 0
            frase_escolhida = random.randrange(1,8)
            ganhador = 0

            for jogador in self.participantes:
                if jogador.sorte < minimo:
                    minimo = jogador.sorte
                    removido = jogador
            if len(self.participantes) > 3:
                if frase_escolhida == 1:
                    self.participantes.remove(removido)
                    input(f"\n{removido.nome} pegou diversas bolinhas, mas não o suficiente para se manter no jogo e está"
                        f" eliminado.\nPressione Enter para continuar a prova.")
                if frase_escolhida == 2:
                    self.participantes.remove(removido)
                    input(f"\n{removido.nome} escorregou e perdeu todas as suas bolas e saiu de cabeça baixa da prova."
                        f"\nPressione Enter para continuar a prova.")
                if frase_escolhida == 3:
                    self.participantes.remove(removido)
                    input(f"\nFoi uma disputa acirradissima entre {self.participantes[random.randrange(0,len(self.participantes)-1)].nome},"
                          f" {self.participantes[random.randrange(0,len(self.participantes)-1)].nome} e {removido.nome} \n"
                          f"mas infelizmente {removido.nome} está fora da prova.\nPressione Enter para continuar a prova.")
                if frase_escolhida == 4:
                    self.participantes.remove(removido)
                    input(f"\n{removido.nome} não conseguiu pegar nenhuma bola se quer e está eliminado."
                        f" \nPressione Enter para continuar a prova.")
                if frase_escolhida == 5:
                    self.participantes.remove(removido)
                    input(f"\n{self.participantes[random.randrange(0,len(self.participantes)-1)].nome} cuspiu no chão o que "
                          f"ocasionou na queda de {removido.nome} e eliminou o participante da prova."
                          f"\nPressione Enter para continuar a prova.")
                if frase_escolhida == 6:
                    self.participantes.remove(removido)
                    input(f"\nFoi uma disputa acirradissima entre os participantes mas infelizmente {removido.nome} está"
                        f" fora da prova.\nPressione Enter para continuar a prova.")
                if frase_escolhida == 7:
                    self.participantes.remove(removido)
                    input(f"\n{removido.nome} infringiu uma regra da prova o que ocasionou em sua eliminação imediata da prova."
                          f"\nPressione Enter para continuar a prova.")
                if frase_escolhida == 8:
                    self.participantes.remove(removido)
                    input(f"\n{removido.nome} sofreu um leve acidente rolando duas vezes no chão tentando recuperar suas bolas\n"
                          f"e por esse motivo está fora da prova."
                          f"\nPressione Enter para continuar a prova.")
            elif len(self.participantes) == 3:
                self.participantes.remove(removido)
                input(f"\n{removido.nome} saiu da prova. FALTAM APENAS {self.participantes[0].nome.upper()} e {self.participantes[1].nome.upper()} "
                      f"PARA O NOVO {self.tipo_de_prova.upper()}."
                      f"\nPressione Enter para ver quem é o novo ganhador.")
                jogador_upado.append(self.participantes[0])
                jogador_upado.append(self.participantes[1])
                jogador_upado.append(removido)
            else:
                self.participantes.remove(removido)
                ganhador = self.participantes[0]
                print(f"\nParabéns {ganhador.nome} você é o novo {self.tipo_de_prova}. Boa sorte da próxima vez {removido.nome}.")
                print(f"\n{jogador_upado[0].nome}, {jogador_upado[1].nome} e {jogador_upado[2].nome} sofreram alterações nos atributos.")
                for jogador in jogador_upado:
                    jogador.resistencia += 5
                    if jogador.resistencia > 100:
                        jogador.resistencia = 100
                input(f"\nPressione Enter para prosseguir.")
        return ganhador

    def prova_de_resistencia(self):

        input("Essa é uma prova de resistência. Os jogadores deverão permanecer na mesma posição pelo máximo de tempo possivel."
              "\nJogadores com maior resistência ganharão a prova."
              "\nPressione Enter para prosseguir.")
        primeiro_removido = True

        jogador_upado = []

        while len(self.participantes) != 1:
            frase_escolhida = random.randrange(1,8)
            minimo = 100
            removido = 0
            ganhador = 0

            for jogador in self.participantes:
                if jogador.resistencia <= minimo:
                    removido = jogador
            if len(self.participantes) > 3:
                if frase_escolhida == 1:
                    input(f"Após algumas horas de prova, {removido.nome} não suportou e está fora da prova.\nPressione Enter"
                          f" para continuar a prova.")
                    self.participantes.remove(removido)
                if frase_escolhida == 2:
                    input(f"Demonstrando cansaço desde o começo, {removido.nome} resistiu ao máximo, porém não o suficiente"
                          f" e deixando a disputa.\nPressione Enter para continuar a prova.")
                    self.participantes.remove(removido)
                if frase_escolhida == 3:
                    input(f"Precisamos respeitar os limites do nosso corpo, e com consciência disso {removido.nome} está"
                          f" fora da prova.\nPressione Enter para continuar a prova.")
                    self.participantes.remove(removido)
                if frase_escolhida == 4:
                    input(f"{removido.nome}, não aguentou as provocações de {self.participantes[random.randrange(0,len(self.participantes)-1)]}"
                          f" e desistiu da prova.\nPressione Enter para continuar a prova.")
                    self.participantes.remove(removido)
                if frase_escolhida == 5:
                    input(f"Lágrimas e mais lágrimas escorreram do rosto de {removido.nome} que não aguentou a prova e "
                          f" está fora.\nPressione Enter para continuar a prova.")
                    self.participantes.remove(removido)
                if frase_escolhida == 6:
                    input(f"{removido.nome} desmaiou na prova e teve que ter atendimento médico, e acabou perdendo a prova."
                          f"\nPressione Enter para continuar a prova.")
                    self.participantes.remove(removido)
                if frase_escolhida == 7:
                    input(f"{removido.nome} não conseguiu se manter firme por muito tempo e cedeu."
                          f"\nPressione Enter para continuar a prova.")
                    self.participantes.remove(removido)
                if frase_escolhida == 8:
                    input(f"\"Eu não vou desistir agora\" gritou {removido.nome} momentos antes de desabar sentindo dores"
                          f"musculares e deixar a prova."
                          f"\nPressione Enter para continuar a prova.")
            elif len(self.participantes) == 3:
                self.participantes.remove(removido)
                horas_prova = random.randrange(12,48)
                input(f"\nApós mais de {horas_prova}, {removido.nome} não resistiu por mais tempo e abandonou a prova."
                      f"\nRESTA APENAS {self.participantes[0].nome.upper()} E {self.participantes[1].nome.upper()} PARA O NOVO {self.tipo_de_prova.upper()}."
                      f"\nPressione Enter para ver quem é o novo {self.tipo_de_prova}.")
                jogador_upado.append(self.participantes[0])
                jogador_upado.append(self.participantes[1])
                jogador_upado.append(removido)
            else:
                self.participantes.remove(removido)
                ganhador = self.participantes[0]
                print(f"\nParabéns {ganhador.nome} você é o novo {self.tipo_de_prova}. Boa sorte da próxima vez {removido.nome}")
                print(f"\n{jogador_upado[0].nome}, {jogador_upado[1].nome} e {jogador_upado[2].nome} sofreram alterações nos atributos.")
                for jogador in jogador_upado:
                    jogador.velocidade += 5
                    jogador.sorte += 13
                    if jogador.velocidade > 100:
                        jogador.velocidade = 100
                    if jogador.sorte > 100:
                        jogador.sorte = 100
                input(f"\nPressione Enter para seguir.")

            if primeiro_removido:
                primeiro_removido = False
                removido.sorte -= 10
                if removido.resistencia < 0:
                    removido.resistencia = 0
        return ganhador

    def prova_de_velocidade(self):
        input("Essa é uma prova de velocidade e um pouquinho de sorte. Os jogadores deverão percorrer um percurso e estourar \n"
              "o máximo de balões que conseguirem antes do tempo acabar."
              "\n\nJogadores com maior velocidade e sorte terão mais chance de ganhar."
              "\n\nVence o primeiro jogador mais veloz que conseguir estourar mais balões dentro do tempo.\n\nPressione Enter para prosseguir.")
        maior_quantidade = 0
        ganhador = 0

        for jogador in self.participantes:
            soma_atributos = jogador.velocidade + jogador.sorte
            if soma_atributos == 200:
                baloes = 25
                maior_quantidade = baloes
                ganhador = jogador
                input(f"\n{jogador.nome} foi muito bem e conseguiu estourar TODOS OS {baloes} balões.\nProvavelmente"
                      f"será o novo {self.tipo_de_prova}.\nPressione Enter para ver o resultado do próximo jogador.")
            elif 150 <= soma_atributos < 200:
                baloes = random.randrange(20,24)
                input(f"\n{jogador.nome} estorou {baloes} balões. Boa prova!"
                      f"\nPressione Enter para ver o resultado do próximo jogador.")
                if baloes > maior_quantidade:
                    maior_quantidade = baloes
                    ganhador = jogador
            elif 100 <= soma_atributos < 150:
                baloes = random.randrange(15,19)
                input(f"\n{jogador.nome} correu bastante mas não deu sorte e só estorou {baloes} balões."
                      f"\nPressione Enter para ver o resultado do próximo jogador.")
                if baloes > maior_quantidade:
                    maior_quantidade = baloes
                    ganhador = jogador
            else:
                baloes = random.randrange(5,14)
                input(f"\n{jogador.nome} não deve ter tomado café da manhã, estorou apenas {baloes} balões. Não foi uma boa prova para {jogador.nome}."
                      f"\nPressione Enter para ver o resultado do próximo jogador.")
                if baloes > maior_quantidade:
                    maior_quantidade = baloes
                    ganhador = jogador
        print(f"\nParabéns {ganhador.nome}. Você é o novo {self.tipo_de_prova}!")
        print(f"\n{ganhador.nome} sofreu alterações de atributo.")
        ganhador.resistencia = 100 if ganhador.resistencia > 100 else ganhador.resistencia + 10
        ganhador.velocidade = 100 if ganhador.velocidade > 100 else ganhador.velocidade + 5
        input("\nPressione Enter para prosseguir.")
        return ganhador

    def prova_interativa_jaula(self):
        input("Essa é uma prova de escolhas. Selecione dentre das opções qual das jaulas você quer ficar e tente sobreviver na prova!"
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
                        jaula_inexistente = True
                        chute_jogador = 0
                        while jaula_inexistente:
                            chute_jogador = input("\nSelecione a jaula [1], [2], [3] ou [4].\n-> ")
                            if chute_jogador != "1" and chute_jogador != "2" and chute_jogador != "3" and chute_jogador != "4":
                                print("Informe uma jaula existente!")
                            else:
                                chute_jogador = int(chute_jogador)
                                jaula_inexistente = False
                        if chute_jogador != jaula_salva:
                            self.participantes.remove(jogador)
                            eliminados.append(jogador)
                        if len(self.participantes) == 1 and self.jogador_principal in self.participantes:
                            ganhador = jogador
                            input(f"Parabéns {ganhador.nome}, você é o novo {self.tipo_de_prova}!")
                            return ganhador
                    else:
                        chute_maquina = random.randrange(1, 4)
                        input(f"\nO {jogador.nome} foi na jaula {chute_maquina}. Pressione Enter para seguir")
                        if chute_maquina != jaula_salva:
                            self.participantes.remove(jogador)
                            eliminados.append(jogador)
                    if len(eliminados) == 4:
                        for jogador in eliminados:
                            jogador.resistencia = 0 if jogador.resistencia < 0 else jogador.resistencia - 10
                            jogador.sorte = 0 if jogador.sorte < 0 else jogador.sorte - 10
                            jogador.velocidade = 0 if jogador.velocidade < 0 else jogador.velocidade - 10
                            jogador.carisma = 0 if jogador.carisma < 0 else jogador.carisma - 10
                print(f"\nA jaula correta é a {jaula_salva}.")
                if ganhador == 0:
                    print(f"\nOs seguintes jogadores não escolheram a jaula {jaula_salva} e estão eliminados da prova.")
                    for eliminado in eliminados:
                        print(eliminado.nome)
            elif len(self.participantes) == 3:
                print("\nSobraram apenas 3 jogadores.")
                if self.jogador_principal in self.participantes:
                    jaula_salva = random.randrange(1, 3)

                    jaula_inexistente = True
                    chute_jogador = 0
                    while jaula_inexistente:
                        chute_jogador = input("\nSelecione a jaula [1], [2] ou [3] \n-> ")
                        if chute_jogador != "1" and chute_jogador != "2" and chute_jogador != "3":
                            print("Informe uma jaula existente!")
                        else:
                            chute_jogador = int(chute_jogador)
                            jaula_inexistente = False

                    if chute_jogador == jaula_salva:
                        input(f"{self.jogador_principal.nome} escolheu a jaula certa e é o novo {self.tipo_de_prova}.\n Pressione Enter"
                              f" para prosseguir")
                        return self.jogador_principal
                    elif chute_jogador == 1:
                        chute_maquina = 2
                        if jaula_salva == chute_maquina:
                            print(f"{self.jogador_principal.nome} e {self.participantes[2].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[1].nome} é o novo {self.tipo_de_prova}.")
                            return self.participantes[1]
                        else:
                            print(f"{self.jogador_principal.nome} e {self.participantes[1].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[2].nome} é o novo {self.tipo_de_prova}.")
                            return self.participantes[2]
                    elif chute_jogador == 2:
                        chute_maquina = 1
                        if jaula_salva == chute_maquina:
                            print(
                                f"{self.jogador_principal.nome} e {self.participantes[2].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[1].nome} é o novo {self.tipo_de_prova}.")
                            return self.participantes[1]
                        else:
                            print(
                                f"{self.jogador_principal.nome} e {self.participantes[1].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[2].nome} é o novo {self.tipo_de_prova}.")
                            return self.participantes[2]
                    elif chute_jogador == 3:
                        chute_maquina = 1
                        if jaula_salva == chute_maquina:
                            print(
                                f"{self.jogador_principal.nome} e {self.participantes[2].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[1].nome} é o novo {self.tipo_de_prova}.")
                            return self.participantes[1]
                        else:
                            print(f"{self.jogador_principal.nome} e {self.participantes[1].nome} escolheram a jaula errada.")
                            print(f"{self.participantes[2].nome} é o novo {self.tipo_de_prova}.")
                            return self.participantes[2]
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
                    jaula_inexistente = True
                    chute_jogador = 0
                    while jaula_inexistente:
                        chute_jogador = input("\nSelecione entre a jaula número [1] e a jaula numero [2].\n-> ")
                        if chute_jogador != "1" and chute_jogador != "2":
                            print("Informe uma jaula existente!")
                        else:
                            chute_jogador = int(chute_jogador)
                            jaula_inexistente = False

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

    def prova_elimina_jogador(self):
        input("Essa é uma prova de eliminação. Vence o último jogador a ser eliminado.\nPressione Enter para continuar.")
        informado = False
        while len(self.participantes) != 1:
            for jogador in self.participantes:
                jogador_disponivel = self.participantes.copy()
                if jogador == self.jogador_principal:
                    for jogador in self.participantes:
                        if jogador == self.jogador_principal:
                            continue
                        print(f"[{self.participantes.index(jogador)}] - {jogador.nome}")
                    voto = -1
                    jogador_nao_exite = True
                    while jogador_nao_exite:
                        voto = int(input("Vote no número de um jogador para ser eliminado.\n-> "))
                        if 0 >= voto > len(jogador):
                            print("\nInforme um número válido de jogador.")
                        else:
                            jogador_nao_exite = False
                    print(f"{self.jogador_principal.nome} eliminou {self.participantes[voto].nome}.\n")
                    self.participantes.pop(voto)
                else:
                    elimina_jogador = random.randrange(0,(len(self.participantes) - 1))
                    jogador_disponivel.remove(jogador)
                    input(f"{jogador.nome} escolheu eliminar {jogador_disponivel[elimina_jogador].nome}.Pressione Enter para continuar.\n")
                    self.participantes.remove(jogador_disponivel[elimina_jogador])
                if not self.jogador_principal in self.participantes and informado == False:
                    informado = True
                    input(f"\nVocê foi eliminado da prova.\nPressione Enter para continuar.\n")
        ganhador = self.participantes[0]
        print(f"Parabéns {ganhador.nome}, você é o novo {self.tipo_de_prova}.")
        input("O ganhador da prova sofreu alterações em seus atributos.")
        ganhador.resistencia = 100 if jogador.resistencia > 100 else jogador.resistencia + 10
        ganhador.sorte = 100 if jogador.sorte > 100 else jogador.sorte + 10
        ganhador.velocidade = 100 if jogador.velocidade > 100 else jogador.velocidade + 10
        ganhador.carisma = 100 if jogador.carisma > 100 else jogador.carisma + 10
        return ganhador