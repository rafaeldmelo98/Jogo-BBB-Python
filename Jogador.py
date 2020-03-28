import random


class JogadorPrincipal:
    def __init__(self,nome, peso, altura):
        self.__nome = nome
        self.__peso = peso
        self.__altura = altura
        self.__velocidade = 0
        self.__resistencia = 0
        self.__sorte = random.randrange(0,100)

    @property
    def nome(self):
        return self.__nome

    @property
    def peso(self):
        return self.__peso

    @property
    def altura(self):
        return self.__altura

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def resistencia(self):
        return self.__resistencia

    @property
    def sorte(self):
        return self.__sorte

    def __str__(self):
        return f"Jogador: {self.nome} (Peso:{self.peso} Altura:{self.altura} VEL:{self.velocidade} RES: {self.resistencia} SOR: {self.sorte}"

    def definir_valores_iniciais(self, peso, altura):
        #definindo valores de velocidade, resistencia e sorte de acordo com dados do jogador
        imc = peso / pow(altura, 2)

        if imc <= 18.4:
            self.__resistencia = random.randrange(50,80)
            self.__velocidade = random.randrange(80,100)
        elif 18.5 <= imc <= 24.9:
            self.__resistencia = random.randrange(70, 100)
            self.__velocidade = random.randrange(70, 100)
        elif 25 <= imc <= 29.9:
            self.__resistencia = random.randrange(60, 90)
            self.__velocidade = random.randrange(60, 90)
        elif 30 <= imc <= 34.9:
            self.__resistencia = random.randrange(50, 80)
            self.__velocidade = random.randrange(50, 70)
        elif 35 <= imc <= 39.9:
            self.__resistencia = random.randrange(40, 70)
            self.__velocidade = random.randrange(40, 60)
        else:
            self.__resistencia = random.randrange(20, 50)
            self.__velocidade = random.randrange(20, 50)

    def votar(self, participantes):
        input("\nVoto do jogador. Pressione Enter para prosseguir\n")
        print("Jogadores disponiveis para voto.\n")
        jogadores_disponiveis = participantes.copy()
        if self.jogador_principal in jogadores_disponiveis:
            jogadores_disponiveis.remove(self.jogador_principal)

        voto = -1

        for jogador in jogadores_disponiveis:
            print(f"{jogadores_disponiveis.index(jogador)} - {jogador}")

        while voto <= -1 or voto > len(jogadores_disponiveis):
            voto = int(input("Informe o número do jogador que você deseja que saia: "))
            if voto >= len(jogadores_disponiveis) or voto <= -1 or voto is None:
                print("\n Informe o número de um jogador disponivel para voto!")
            if voto >= 0 or voto < len(jogadores_disponiveis):
                break
        return voto


class JogadorMaquina:
    def __init__(self, nome, peso, altura, velocidade, resistencia, sorte):
        self.__nome = nome
        self.__peso = peso
        self.__altura = altura
        self.__velocidade = velocidade
        self.__resistencia = resistencia
        self.__sorte = sorte

    @property
    def nome(self):
        return self.__nome

    @property
    def peso(self):
        return self.__peso

    @property
    def altura(self):
        return self.__altura

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def resistencia(self):
        return self.__resistencia

    @property
    def sorte(self):
        return self.__sorte

    def votar(self, participantes):
        participantes.remove(JogadorMaquina)
        for count in range(len(participantes)):
            if len(participantes) > 2:
                return random.randrange(0, len(participantes)-1)
            else:
                return 0