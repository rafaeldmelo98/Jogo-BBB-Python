import random


class JogadorPrincipal:
    def __init__(self, nome, peso, altura):
        self.__nome = nome
        self.__peso = peso
        self.__altura = altura
        self.__velocidade = 0
        self.__resistencia = 0
        self.__sorte = random.randrange(0,100)
        self.carisma = 50

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

    @velocidade.setter
    def velocidade(self, value):
        self._velocidade = value

    @sorte.setter
    def sorte(self, value):
        self._sorte = value

    @resistencia.setter
    def resistencia(self, value):
        self._resistencia = value

    def __str__(self):
        return "Jogador: {:25} (Peso:{:3} Kg, Altura:{:3} cm, VEL:{:3}, RES: {:3}, SOR: {:3}, CAR: {:3})".format(self.nome,
                                                                                                     self.peso,
                                                                                                     self.altura,
                                                                                                     self.velocidade,
                                                                                                     self.resistencia,
                                                                                                     self.sorte,
                                                                                                     self.carisma)

    def definir_valores_iniciais(self):
        #definindo valores de velocidade, resistencia e sorte de acordo com dados do jogador
        imc = self.peso / pow(self.altura, 2)

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
        voto_errado = True
        input("\nVoto do jogador. Pressione Enter para prosseguir\n")
        print("Jogadores disponiveis para voto.\n")
        jogadores_disponiveis = participantes.copy()
        if self in jogadores_disponiveis:
            jogadores_disponiveis.remove(self)

        for jogador in jogadores_disponiveis:
            print(f"{jogadores_disponiveis.index(jogador)} - {jogador.nome}")

        while voto_errado:
            voto = int(input("Informe o número do jogador que você deseja que saia: "))
            if (len(jogadores_disponiveis) - 1) <= voto <= 0:
                print("\n Informe o número de um jogador disponivel para voto!")
            else:
                voto_errado = False
        return voto


class JogadorMaquina:
    def __init__(self, nome, peso, altura, velocidade, resistencia, sorte):
        self.__nome = nome
        if "rafael mello" in self.nome.lower() or "rafael melo" in self.nome.lower():
            self.__nome = "Rafael de Melo"
        if "ricardo" in self.nome.lower():
            self.__nome = "Ricardo (Bostão)"
        self.__peso = int(peso)
        self.__altura = int(altura)
        self.__velocidade = int(velocidade)
        self.__resistencia = int(resistencia)
        self.__sorte = int(sorte)
        self.carisma = 50

    def __str__(self):
        return "Jogador: {:25} (Peso:{:3} Kg, Altura:{:3} cm, VEL: {:3}, RES: {:3}, SOR: {:3}, CAR: {:3})".format(self.nome,
                                                                                                     self.peso,
                                                                                                     self.altura,
                                                                                                     self.velocidade,
                                                                                                     self.resistencia,
                                                                                                     self.sorte,
                                                                                                     self.carisma)

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

    @velocidade.setter
    def velocidade(self, value):
        self._velocidade = value

    @sorte.setter
    def sorte(self, value):
        self._sorte = value

    @resistencia.setter
    def resistencia(self, value):
        self._resistencia = value

    def votar(self, participantes):
        if len(participantes) > 2:
            return random.randrange(0, len(participantes) - 1)
        else:
            return 0