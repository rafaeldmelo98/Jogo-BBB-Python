from Jogador import JogadorMaquina
from Jogador import JogadorPrincipal
import random


class Jogo:
    def __init__(self, jogador_principal: JogadorPrincipal):
        self.__jogador_principal = jogador_principal
        self.__jogadores_atuais = self.carrega_jogadores()
        self.__jogadores_atuais.insert(0, self.jogador_principal)
        self.__eliminados = []
        self.__lider = ""
        self.__anjo = ""

    def __str__(self):

        return f"Jogador principal: {self.jogador_principal}" + self.lista_jogadores() + self.lista_eliminados()

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

    def lista_eliminados(self):
        print("\nEliminados:\n")
        for eliminado in self.eliminados:
            print(eliminado)


    def carrega_jogadores(self):
        texto = open('nomes.txt', "r", encoding="utf-8")
        todos_jogadores = [linha.replace("\n", "") for linha in texto] #captura todos os jogadores disponiveis
        jogadores_selecionados = []
        while len(jogadores_selecionados) != 16:
            indice = random.randrange(0, 100)           #sorteia jogadores disponiveis
            if todos_jogadores[indice] not in jogadores_selecionados:
                jogadores_selecionados.append(todos_jogadores[indice])      #adiciona jogador sorteado

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
        # MUDAR PARA PROVA DO LIDER
        self.__lider = self.sorteia_ganhador_prova(self.jogadores_atuais)

    def definir_anjo(self):
        #MUDAR PARA PROVA DO ANJO
        participantes = self.jogadores_atuais.copy()
        if self.lider != "":
            participantes.remove(self.lider)
        self.__anjo = self.sorteia_ganhador_prova(participantes)

    def votacao(self, participantes):
        votos = []
        emparedado = -1

        voto = self.jogador_principal.votar(participantes)
        votos.append(voto)

        for jogador in self.jogadores_atuais:
            if jogador == self.jogador_principal:
                continue
            voto = jogador.votar(participantes)
            votos.append(voto)

        if len(participantes) < 2:
            emparedado = random.randrange(0,1)

        input("A casa votou. Pressione Enter para ver o resultado.")

        return emparedado

    def voto_lider(self, participantes):
        if self.verifica_jogador_principal_eh_lider():
            voto = self.jogador_principal.votar(participantes)
            input("\nO lider votou! Pressione Enter para prosseguir.")
            return voto
        else:
            input("\nO lider votou! Pressione Enter para prosseguir.")
            lider = 0
            for jogador in self.jogadores_atuais:
                if jogador.nome == self.lider:
                    lider = jogador
            return lider.votar(participantes)

    def paredao_eliminacao(self):
        participantes = self.selecionar_participantes()
        primeiro_emparedado = participantes[self.voto_lider(participantes)]
        participantes.remove(primeiro_emparedado)
        segundo_emparedado = participantes[self.votacao(participantes)]

        print(f"\nO voto do lider foi {primeiro_emparedado}.")
        print(f"\nA casa decidiu. O paredão será entre {primeiro_emparedado.nome} e {segundo_emparedado.nome}.")
        input("Pressione Enter para ver o resultado do paredão.")

        percentagem_primeiro_emparedado = random.randrange(0,100)
        percentagem_segundo_emparedado = random.randrange(0,100)
        if percentagem_primeiro_emparedado > percentagem_segundo_emparedado:
            print(f"\nO público decidiu. E quem sai hoje é {primeiro_emparedado.nome}.")
            self.__eliminados.append(primeiro_emparedado)
            self.__jogadores_atuais.remove(primeiro_emparedado)
        else:
            print(f"\nO público decidiu. E quem sai hoje é {segundo_emparedado.nome}.")
            self.__eliminados.append(segundo_emparedado)
            self.__jogadores_atuais.remove(segundo_emparedado)

        if self.verifica_jogador_eliminado():
            campeao = participantes[random.randrange(0,len(participantes))]
            print(f"\nVocê foi eliminado do jogo. O jogo seguiu sem você e o campeão foi {campeao}.")

    def proxima_rodada(self):
        self.__lider = ""
        self.__anjo = ""

    def campeao_jogo(self):
        numero_vencedor = random.randrange(0,100)
        minimo = 100
        sorteio = []
        indice_jogador = 0

        for i in range(3):
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

    def selecionar_participantes(self):
        participantes = self.__jogadores_atuais.copy()
        for jogador in participantes:
            if self.lider == jogador:
                participantes.remove(jogador)
            if self.anjo == jogador:
                participantes.remove(jogador)

        return participantes