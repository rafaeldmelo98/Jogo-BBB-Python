from Jogo import Jogo
import math
import random

class Jogador:
    def __init__(self, nome, peso, altura):
        self.__nome = nome
        self.__peso = peso
        self.__altura = altura
        self.__velocidade = 0
        self.__resistencia = 0
        self.__sorte = random.randrange(0,100)

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
        


