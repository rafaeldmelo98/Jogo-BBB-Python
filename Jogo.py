from Jogador import JogadorMaquina
from Jogador import JogadorPrincipal
from Prova import Prova
from Crises import Crise
import random


class Jogo:
    def __init__(self, jogador_principal: JogadorPrincipal):
        self.__jogador_principal = jogador_principal
        self.__jogadores_atuais = self.carrega_jogadores()
        self.__jogadores_atuais.insert(0, self.jogador_principal)
        self.__eliminados = []
        self.__lider = ""
        self.__anjo = ""
        self.__roteiro = []
        self.crise = ""

    def __str__(self):

        return f"\n\nJogador principal: \n{self.jogador_principal}" + self.lista_jogadores() + self.lista_eliminados()

    @property
    def jogador_principal(self):
        return self.__jogador_principal

    @property
    def jogadores_atuais(self):
        return self.__jogadores_atuais

    @property
    def lider(self):
        return self.__lider

    @property
    def anjo(self):
        return self.__anjo

    @property
    def eliminados(self):
        return self.__eliminados

    def lista_jogadores(self):
        print("\nJogadores atuais:\n")
        for jogador in self.jogadores_atuais:
            print(jogador)
        return ""

    def lista_eliminados(self):
        print("\nEliminados:\n")
        for eliminado in self.eliminados:
            print(eliminado)
        return ""


    def carrega_jogadores(self):
        texto = open('nomes.txt', "r", encoding="utf-8")
        todos_jogadores = [linha.replace("\n", "") for linha in texto] # captura todos os jogadores disponiveis
        jogadores_selecionados = []
        while len(jogadores_selecionados) != 15:
            indice = random.randrange(0, 100)           # sorteia jogadores disponiveis
            if todos_jogadores[indice] not in jogadores_selecionados:
                jogadores_selecionados.append(todos_jogadores[indice])      # adiciona jogador sorteado

        jogadores_atuais = []
        for jogador_selecionado in jogadores_selecionados:
            info_jogador = jogador_selecionado.split(";")
            nome = info_jogador[0]
            peso = info_jogador[1]
            altura = info_jogador[2]
            velocidade = info_jogador[3]
            resistencia = info_jogador[4]
            sorte = info_jogador[5]
            jogador = JogadorMaquina(nome, peso, altura, velocidade, resistencia, sorte)
            jogadores_atuais.append(jogador)    #adiciona informações jogadores
        return jogadores_atuais

    def definir_lider(self):
        participantes = self.selecionar_participantes()
        prova_selecionada = random.randrange(1,5)
        self.__lider = Prova(prova_selecionada, participantes,self.jogador_principal,1).seletor_de_prova()

    def definir_anjo(self):
        participantes = self.selecionar_participantes()
        prova_selecionada = random.randrange(1, 4)
        self.__anjo = Prova(prova_selecionada, participantes, self.jogador_principal,2).seletor_de_prova()

    def votacao(self, disponiveis_menor_carisma, participantes):
        votos = []
        emparedado = -1

        if not self.verifica_jogador_principal_eh_lider():
            voto = self.jogador_principal.votar(participantes)
            votos.append(voto)

        for jogador in self.jogadores_atuais:
            if jogador == self.jogador_principal:
                continue
            voto = jogador.votar(disponiveis_menor_carisma)
            votos.append(voto)

        if len(disponiveis_menor_carisma) < 2:
            emparedado = random.randrange(0,1)

        input("\nA casa votou. Pressione Enter para ver o resultado.")

        return emparedado

    def voto_lider(self, disponiveis_menor_carisma, participantes):
        if self.verifica_jogador_principal_eh_lider():
            voto = self.jogador_principal.votar(participantes)
            input("\nO lider votou! Pressione Enter para prosseguir.")
            return voto
        else:
            input("\nO lider votou! Pressione Enter para prosseguir.")
            return self.__lider.votar(disponiveis_menor_carisma)

    def paredao_eliminacao(self):
        participantes = self.selecionar_participantes()
        disponiveis = self.jogadores_menor_carisma(participantes)
        primeiro_emparedado = participantes[self.voto_lider(disponiveis, participantes)]
        primeiro_emparedado.carisma = 0 if primeiro_emparedado.carisma < 0 else primeiro_emparedado.carisma - 5
        print(f"\nO voto do lider {self.lider.nome} foi em {primeiro_emparedado.nome.upper()}.")
        participantes.remove(primeiro_emparedado)
        disponiveis = self.jogadores_menor_carisma(participantes)
        segundo_emparedado = participantes[self.votacao(disponiveis, participantes)]

        self.diminuir_atributos_emparedados(primeiro_emparedado, segundo_emparedado)

        print(f"\nA casa decidiu. O paredão será entre {primeiro_emparedado.nome.upper()} e {segundo_emparedado.nome.upper()}.")
        input("\nPressione Enter para ver o resultado do paredão.")

        eliminado = self.eliminar_jogador(primeiro_emparedado, segundo_emparedado)

        if primeiro_emparedado != eliminado:
            primeiro_emparedado.sorte += 10
            if primeiro_emparedado.sorte > 100:
                primeiro_emparedado.sorte = 100
        else:
            segundo_emparedado.sorte += 10
            if segundo_emparedado.sorte > 100:
                segundo_emparedado.sorte = 100

        voto = random.randrange(51, 100)
        print(f"\nO público decidiu. E quem sai hoje é {eliminado.nome.upper()} com {voto} % dos votos.")

        if self.verifica_jogador_eliminado():
            campeao = participantes[random.randrange(0, len(participantes))]
            print(f"\nVocê foi eliminado do jogo. O jogo seguiu sem você e o campeão foi {campeao.nome}.")

    def proxima_rodada(self):
        self.__lider = ""
        self.__anjo = ""
        self.crise = ""

    def campeao_jogo(self):
        numero_vencedor = random.randrange(0,100)
        minimo = 100
        sorteio = []
        indice_jogador = 0

        for i in range(0,2):
            sorteio.append(random.randrange(0,100))

        for numero in sorteio:
            numero_sorte = abs(numero_vencedor - numero)
            jogador = self.jogadores_atuais[indice_jogador]
            numero_sorte += jogador.sorte
            indice_jogador += 1

            if numero_sorte < minimo:
                minimo = numero_sorte
                ganhador = sorteio.index(numero)

        return self.jogadores_atuais[ganhador]

    def verifica_jogador_eliminado(self):
        return self.jogador_principal in self.__eliminados

    def verifica_jogador_principal_eh_lider(self):
        return self.jogador_principal == self.lider

    def jogadores_menor_carisma(self, participantes):
        disponivel = []
        menor_carisma = 100

        for jogador in participantes:
            if jogador.carisma < menor_carisma:
                menor_carisma = jogador.carisma

        maior_carisma = menor_carisma + 25

        # Captura jogadores disponiveis

        for jogador in participantes:
            if menor_carisma < jogador.carisma and jogador.carisma < maior_carisma:
                disponivel.append(jogador)

        return disponivel


    def selecionar_participantes(self):
        participantes = self.__jogadores_atuais.copy()
        for jogador in participantes:
            if self.lider == jogador:
                participantes.remove(jogador)
            if self.anjo == jogador:
                participantes.remove(jogador)

        return participantes

    def definir_eliminado(self, primeiro_emparedado, num_primeiro_emparedo, segundo_emparedado, num_segundo_emparedado):
        eliminado = segundo_emparedado if num_primeiro_emparedo > num_segundo_emparedado else primeiro_emparedado
        self.__eliminados.append(eliminado)
        self.__jogadores_atuais.remove(eliminado)
        return eliminado

    def eliminar_jogador(self, primeiro_emparedado, segundo_emparedado):
        diferenca_carisma = abs(segundo_emparedado.carisma - primeiro_emparedado.carisma)
        if diferenca_carisma <= 5:
            percentagem_primeiro_emparedado = primeiro_emparedado.carisma + primeiro_emparedado.sorte
            percentagem_segundo_emparedado = segundo_emparedado.carisma + segundo_emparedado.sorte
            return self.definir_eliminado(primeiro_emparedado, percentagem_primeiro_emparedado, segundo_emparedado, percentagem_segundo_emparedado)
        elif 5 < diferenca_carisma <= 15:
            percentagem_primeiro_emparedado = primeiro_emparedado.carisma + random.randrange(0, 100)
            percentagem_segundo_emparedado = segundo_emparedado.carisma + random.randrange(0, 100)
            return self.definir_eliminado(primeiro_emparedado, percentagem_primeiro_emparedado, segundo_emparedado, percentagem_segundo_emparedado)
        else:
            return self.definir_eliminado(primeiro_emparedado, primeiro_emparedado.carisma, segundo_emparedado, segundo_emparedado.carisma)

    def adicionar_roteiro(self, semana):
        roteiro = f"Semana {semana}:\n- Crise da semana: \n {self.crise}\n- Lider da semana: {self.lider.nome}\n" \
                  f"- Anjo da semana: {self.anjo.nome}\n- Eliminado da semana: {self.eliminados[-1].nome}\n\n"
        self.__roteiro.append(roteiro)

    def exibe_roteiro(self):
        for acontecimento in self.__roteiro:
            print(acontecimento)

    def acontecer_crise(self, semana):
        participantes = self.selecionar_participantes()
        self.crise = Crise(semana, participantes, self.jogador_principal).selecao_de_crise()

    def diminuir_atributos_emparedados(self, primeiro, segundo):
        primeiro.resistencia = 100 if primeiro.resistencia > 100 else primeiro.resistencia - 5
        primeiro.sorte = 100 if primeiro.sorte > 100 else primeiro.sorte - 5
        primeiro.velocidade = 100 if primeiro.velocidade > 100 else primeiro.velocidade - 5
        primeiro.carisma = 100 if primeiro.carisma > 100 else primeiro.carisma - 5

        segundo.resistencia = 100 if segundo.resistencia > 100 else segundo.resistencia - 5
        segundo.sorte = 100 if segundo.sorte > 100 else segundo.sorte - 5
        segundo.velocidade = 100 if segundo.velocidade > 100 else segundo.velocidade - 5
        segundo.carisma = 100 if segundo.carisma > 100 else segundo.carisma - 5