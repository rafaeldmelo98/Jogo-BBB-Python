import random


class Crise:
    def __init__(self, semana:int, participantes:list, jogador_principal):
        self.semana = semana
        self.participantes = participantes
        self.jogador_principal = jogador_principal

    def selecao_de_crise(self):
        if 1 >= self.semana >= 4:
            selecao_crise = random.randrange(1,4)
            if selecao_crise == 1:
                return self.crise_organizacao_casa()
            elif selecao_crise == 2:
                return self.crise_louca()
            elif selecao_crise == 3:
                return self.crise_higiene()
            else:
                return self.crise_desperdicio_de_agua()
        elif 5 >= self.semana >= 8:
            selecao_crise = random.randrange(1, 5)
            if selecao_crise == 1:
                return self.crise_desperdicio_de_agua()
            elif selecao_crise == 2:
                return self.crise_conflito()
            elif selecao_crise == 3:
                return self.crise_festa()
            elif selecao_crise == 4:
                return self.crise_comentario()
            else:
                return self.crise_descobriu_voto()
        elif 9 >= self.semana >= 12:
            selecao_crise = random.randrange(1, 4)
            if selecao_crise == 1:
                return self.crise_desperdicio_de_agua()
            elif selecao_crise == 2:
                return self.crise_prova_lider()
            elif selecao_crise == 3:
                return self.crise_roubar_comida()
            elif selecao_crise == 4:
                return self.crise_conflito()
            else:
                return self.crise_descobriu_voto()
        else:
            return "Não houve crise."

        pass

    def resultado_da_crise(self, escolha_jogador, atores):
        jogadores_decisao = self.participantes.copy()
        pro = []
        contra = []

        for jogador in atores:
            jogadores_decisao.remove(jogador)

        pro.append(self.jogador_principal) if escolha_jogador == 1 else contra.append(self.jogador_principal)

        for jogador in self.participantes:

            escolha_maquina = random.randrange(0,1)

            pro.append(jogador.nome) if escolha_maquina == 1 else contra.append(jogador.nome)

        if len(pro) > len(contra):
            return pro
        elif len(contra) > len(pro):
            return contra
        else:
            return 0

    def selecionar_atores_crise(self, quantidade):
        atores = []
        while len(atores) < quantidade:
            jogador_selecionado = random.randrange(0,len(self.participantes))
            if not jogador_selecionado in atores:
                atores.append(self.participantes[jogador_selecionado])
        return atores

    def crise_organizacao_casa(self):
        atores = self.selecionar_atores_crise(4)
        print(f"Os participantes haviam combinado como manteriam a casa organizada, porém {1} e {2} acabaram não cumprindo com o combinado.\n")
        print(f"\nAchando injusto a atitudes tomadas, {3} e {4} resolveram tirar satisfação causando uma pequena confunsão.\n")
        print(f"\n{3} alegou que a postura de {2} causaria grande conflitos posteriormente caso não seguisse o combinado.\n")
        decisao_jogador = input(f"Você apoia a postura de {3} e {4}?\n[S/N] -> ")

    def crise_louca(self):
        pass

    def crise_festa(self):
        pass

    def crise_prova_lider(self):
        pass

    def crise_higiene(self):
        pass

    def crise_desperdicio_de_agua(self):
        pass

    def crise_roubar_comida(self):
        pass

    def crise_conflito(self):
        pass

    def crise_comentario(self):
        pass

    def crise_briga_de_sexo(self):
        pass

    def crise_descobriu_voto(self):
        pass