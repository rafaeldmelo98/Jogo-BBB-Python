import random


class Jogo:
    def __init__(self, jogador_principal):
        self.__jogador_principal = jogador_principal
        self.__jogadores_atuais = self.carrega_jogadores()
        self.__jogadores_atuais[0] = self.__jogador_principal
        self.__eliminados = []
        self.__lider = ""
        self.__anjo = ""

    def __str__(self):
        print(f"Jogador principal: {self.jogador_principal}")
        print("Jogadores atuais")
        for jogador in self.jogadores_atuais:
            print(jogador)
        print(f"Atual lider: {self.lider}")
        print(f"Atual anjo: {self.anjo}")
        print("Eliminados:")
        for eliminado in self.eliminados:
            print(eliminado)

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

    def carrega_jogadores(self):
        texto = open('nomes.txt', "r", encoding="utf-8")
        todos_jogadores = [linha.replace("\n", "") for linha in texto]
        jogadores_atuais = []
        while len(jogadores_atuais) != 16:
            indice = random.randrange(0, 100)
            if todos_jogadores[indice] not in jogadores_atuais:
                jogadores_atuais.append(todos_jogadores[indice])
        return jogadores_atuais

    def definir_lider(self):
        self.__lider = self.sorteia_ganhador_prova(self.jogadores_atuais)

    def definir_anjo(self):
        participantes = self.jogadores_atuais.copy()
        if self.lider != "":
            participantes.remove(self.lider)
        self.__anjo = self.sorteia_ganhador_prova(participantes)

    def votacao(self, participantes):
        votos = []
        if self.jogador_principal != self.lider:
            voto = self.voto_jogador(participantes, self.jogador_principal)
            votos.append(voto)
        for count in range(len(participantes)):
            voto = random.randrange(0, len(participantes)-1)
            votos.append(voto)

        emparedado = -1
        for voto in votos:
            if votos.count(voto) > emparedado:
                emparedado = voto

        return emparedado

    def voto_jogador(self, jogadores, jogador):
        print("Jogadores disponiveis para voto.")
        jogadores_disponiveis = jogadores
        if jogador in jogadores_disponiveis:
            jogadores_disponiveis.remove(jogador)

        voto = -1

        for jogador in jogadores_disponiveis:
            print(f"{jogadores_disponiveis.index(jogador)} - {jogador}")

        while -1 >= voto >= len(jogadores_disponiveis):
            voto = int(input("Informe o número do jogador que você deseja que saia"))
            if voto >= len(jogadores_disponiveis) or voto <= -1:
                print("Informe o número de um jogador disponivel para voto!")
        print("A casa votou.")
        return voto

    def voto_lider(self, participantes):
        if self.jogador_principal == self.lider:
            voto = self.voto_jogador(participantes, self.jogador_principal)
            emparedado = voto
        else:
            voto = self.votacao(participantes)
            emparedado = voto
        print("O lider votou!")
        return emparedado

    def paredao_eliminacao(self):
        participantes = self.selecionar_participantes()
        primeiro_emparedado = participantes[self.voto_lider(participantes)]
        segundo_emparedado = participantes[self.votacao(participantes)]

        print(f"A casa decidiu. O paredão será entre {primeiro_emparedado} e {segundo_emparedado}")

        percentagem_primeiro_emparedado = random.randrange(0,100)
        percentagem_segundo_emparedado = random.randrange(0,100)
        if percentagem_primeiro_emparedado > percentagem_segundo_emparedado:
            print(f"O público decidiu. E quem sai hoje é {primeiro_emparedado}.")
            self.__eliminados.append(primeiro_emparedado)
            self.__jogadores_atuais.remove(primeiro_emparedado)
        else:
            print(f"O público decidiu. E quem sai hoje é {segundo_emparedado}.")
            self.__eliminados.append(segundo_emparedado)
            self.__jogadores_atuais.remove(segundo_emparedado)

        self.__lider = ""
        self.__anjo = ""

        if self.verifica_jogador_eliminado():
            campeao = participantes[random.randrange(0,len(participantes))]
            print(f"Você foi eliminado do jogo. O jogo seguiu sem você e o campeão foi {campeao}")

    def campeao_jogo(self):
        numero_vencedor = random.randrange(0,100)
        minimo = 100
        sorteio = []
        for i in range(3):
            sorteio.append(random.random())
        for numero in sorteio:
            numero_sorte = abs(numero_vencedor - sorteio)
            if numero_sorte < minimo:
                minimo = numero_sorte
                ganhador = sorteio.index(numero)
        return self.jogadores_atuais[ganhador]

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

    def verifica_jogador_eliminado(self):
        return self.jogador_principal in self.__eliminados

    def selecionar_participantes(self):
        participantes = self.__jogadores_atuais.copy()
        if self.lider != "":
            participantes.remove(self.lider)
        if self.anjo != "":
            participantes.remove(self.anjo)
        return participantes