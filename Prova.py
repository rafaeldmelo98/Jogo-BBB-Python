import random


class ProvaAnjo:
    def __init__(self, numero, participantes: list):
        self.prova_selecionada = numero
        self.participantes = participantes.copy()

    def seletor_de_prova(self):
        pass

    def prova_de_sorte(self):
        pass

    def prova_de_resistencia(self):
        pass

    def prova_de_velocidade(self):
        pass

    def prova_interativa_cor(self):
        pass

    def prova_interativa_numero(self):
        pass

    def prova_elimina_jogador(self):
        pass

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


class ProvaLider:
    def __init__(self, numero, lider, participantes: list):
        self.prova_selecionada = numero
        self.lider = lider
        self.participantes = participantes.copy()

    def seletor_de_prova(self):
        pass

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