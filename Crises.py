import random


class Crise:
    def __init__(self, semana:int, participantes:list, jogador_principal):
        self.semana = semana
        self.participantes = participantes
        self.jogador_principal = jogador_principal

    def selecao_de_crise(self):
        if 1 >= self.semana >= 4:
            selecao_crise = random.randrange(1,2) #MODIFICAR PARA 4
            if selecao_crise == 1:
                return self.crise_organizacao_casa()
            elif selecao_crise == 2:
                return self.crise_louca()
            '''elif selecao_crise == 3:
                return self.crise_higiene()
            else:
                return self.crise_desperdicio_de_agua()'''
        elif 5 >= self.semana >= 8:
            selecao_crise = 1 #MODIFICAR PARA random.randrange(1, 4)
            if selecao_crise == 1:
                return self.crise_festa()
            '''elif selecao_crise == 2:
                return self.crise_desperdicio_de_agua()
            elif selecao_crise == 3:
                return self.crise_conflito()
            else:
                return self.crise_comentario()'''
        elif 9 >= self.semana >= 12:
            selecao_crise = random.randrange(1, 2) #MODIFICAR PARA 4
            if selecao_crise == 1:
                return self.crise_prova_lider()
            '''elif selecao_crise == 2:
                return self.crise_desperdicio_de_agua()
            elif selecao_crise == 3:
                return self.crise_roubar_comida()
            else:
                return self.crise_conflito()'''
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

            pro.append(jogador) if escolha_maquina == 1 else contra.append(jogador)

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
            if not jogador_selecionado in atores and not jogador_selecionado == self.jogador_principal:
                atores.append(self.participantes[jogador_selecionado])
        return atores

    def altera_carisma(self, maioria, aumenta_carisma, diminui_carisma):
        for jogador in self.participantes:
            if jogador in maioria:
                jogador.carisma += aumenta_carisma
            else:
                jogador.carisma -= diminui_carisma


    def crise_organizacao_casa(self):
        atores = self.selecionar_atores_crise(4)
        print(f"Os participantes haviam combinado como manteriam a casa organizada, porém {atores[0].nome} e {atores[1].nome} acabaram não cumprindo com o combinado.\n"
              f"\nAchando injusto a atitudes tomadas, {atores[2].nome} e {atores[3].nome} resolveram tirar satisfação causando uma pequena confunsão.\n"
              f"\n{atores[2].nome} alegou que a postura de {atores[1].nome} causaria grande conflitos posteriormente caso não seguisse o combinado.\n")

        decisao_jogador = input(f"Você apoia a postura de {atores[2].nome} e {atores[3].nome}?\n[S/N] -> ")
        decisao_jogador = decisao_jogador.lower()
        decisao_jogador = 1 if decisao_jogador == "s" else 0

        maioria = self.resultado_da_crise(decisao_jogador,atores)
        crise = (f"Os participantes haviam combinado como manteriam a casa organizada, porém {atores[0].nome} e {atores[1].nome} acabaram não cumprindo com o combinado.\n" +
                    f"Achando injusto a atitudes tomadas, {atores[2].nome} e {atores[3].nome} resolveram tirar satisfação causando uma pequena confunsão.\n" +
                    f"{atores[2].nome} alegou que a postura de {atores[1].nome} causaria grande conflitos posteriormente caso não seguisse o combinado.\n")

        if maioria == 0:
            print("A casa não se decidiu e acabaram abafando a situação.")
            input("Pressione Enter para prosseguir")
            crise += "A casa não se decidiu e acabaram abafando a situação."
            return crise
        elif self.jogador_principal in maioria:
            if decisao_jogador == 1:
                print(f"\nVocê e a maioria da casa concordou com {atores[2].nome} e {atores[3].nome} sobre as atitudes de {atores[1].nome} e {atores[0].nome}\n."
                      f"As suas atitudes e a da maioria da casa foram bem vistas.")
                crise += f"\nVocê e a maioria da casa concordou com {atores[2].nome} e {atores[3].nome} sobre as atitudes de {atores[1].nome} e {atores[0].nome}."
            else:
                print(f"\nVocê e a maioria da casa discordaram com {atores[2].nome} e {atores[3].nome} sobre as atitudes de {atores[1].nome} e {atores[0].nome}\n"
                      f"Você achou que a atitude de {atores[2].nome} foi desnecessária e {atores[1].nome} não agiu por maldade.")
                crise += f"\nVocê e a maioria da casa discordaram com {atores[2].nome} e {atores[3].nome} sobre as atitudes de {atores[1].nome} e {atores[0].nome}\n"
            print("\nOs jogadores que concordaram com você foram: ")
        else:
            if decisao_jogador == 1:
                print(f"\nVocê concordou com {atores[2].nome} e {atores[3].nome} sobre as atitudes de {atores[1].nome} e {atores[0].nome}\n "
                      f"Porém a casa não viu da mesma forma com você. Essa atitude pode ter te prejudicado.")
                crise += (f"\nVocê concordou com {atores[2].nome} e {atores[3].nome} sobre as atitudes de {atores[1].nome} e {atores[0].nome}\n "
                    f"Porém a casa não viu da mesma forma com você.")
            else:
                print(f"\nVocê não conseguiu ver maldade nas atitudes de {atores[1].nome} e {atores[0].nome} e foi contra {atores[2].nome} e {atores[3].nome}.\n"
                    f"Já a casa ficou do lado de {atores[2].nome}. Isso provavelmente trará reves em seu jogo.")
                crise += (f"\nVocê não conseguiu ver maldade nas atitudes de {atores[1].nome} e {atores[0].nome} e foi contra {atores[2].nome} e {atores[3].nome}.\n"
                        f"Já a casa ficou do lado de {atores[2].nome}.")
            print("\nOs jogadores que discordaram de você foram: ")
        for jogador in maioria:
            print(jogador.nome)
        input("\nPressione Enter para prosseguir o jogo.")
        self.altera_carisma(maioria, 10, 5)
        return crise

    def crise_louca(self):
        atores = self.selecionar_atores_crise(3)
        print(f"Em uma casa é necessário organização, mas {atores[0].nome} e {atores[1].nome} comeram em diversos pratos diferentes não lavaram a louça.\n"
              f"\n{atores[2].nome} estava de saco cheio de somente lavar a louça enquanto os outros não moviam um dedo para ajudar.\n"
              f"\n{atores[2].nome} disse que já tinha percebido a folga de {atores[1].nome} e não toleraria mais \"essa palhaçada\".\n")

        decisao_jogador = input(f"Você concorda com {atores[2].nome}?\n[S/N] -> ")
        decisao_jogador = decisao_jogador.lower()
        decisao_jogador = 1 if decisao_jogador == "s" else 0

        maioria = self.resultado_da_crise(decisao_jogador, atores)
        crise = (f"Em uma casa é necessário organização, mas {atores[0].nome} e {atores[1].nome} comeram em diversos"
                f" pratos diferentes não lavaram a louça.\n"
                f"{atores[2].nome} estava de saco cheio de somente lavar a louça enquanto os outros não moviam um"
                f" dedo para ajudar.\n"
                f"{atores[2].nome} disse que já tinha percebido a folga de {atores[1].nome} e não toleraria mais"
                f" \"essa palhaçada\".\n")

        if maioria == 0:
            print("A casa não se importou com a situação.")
            input("Pressione Enter para prosseguir")
            crise += "A casa não se importou com a situação."
            return crise
        elif self.jogador_principal in maioria:
            if decisao_jogador == 1:
                print(f"\nBANDO DE FOLGADOS! Você e a maioria da casa apoiaram {atores[2].nome} e deram um sermão em {atores[1].nome} e {atores[0].nome}\n "
                    f"As suas atitudes e a da maioria da casa foram bem vistas.")
                crise += (f"BANDO DE FOLGADOS! Você e a maioria da casa apoiaram {atores[2].nome} e deram um sermão em {atores[1].nome} e {atores[0].nome}\n "
                    f"As suas atitudes e a da maioria da casa foram bem vistas.")
            else:
                print(f"\n\"{atores[2].nome} você é uma pessoa irritante\" essa foi uma das frases ditas por você e aplaudidas pelas casa.\n"
                      f"Você achou que a atitude de {atores[2].nome} foi bastante desnecessária, é apenas uma louça.")
                crise += (f"\"{atores[2].nome} você é uma pessoa irritante\" essa foi uma das frases ditas por você e aplaudidas pelas casa.\n"
                      f"Você achou que a atitude de {atores[2].nome} foi bastante desnecessária, é apenas uma louça.")
            print("\nOs jogadores que concordaram com você foram: ")
        else:
            if decisao_jogador == 1:
                print(f"\n\"{atores[2].nome} não tá falando besteira, tem que lavar!\" foram as suas palavras.\n "
                    f"Porém para a maioria era só UMA louça, ninguém ia morrer por isso.")
                crise += (f"\"{atores[2].nome} não tá falando besteira, tem que lavar!\" foram as suas palavras.\n "
                    f"Porém para a maioria era só UMA louça, ninguém ia morrer por isso.")
            else:
                print(f"\n\"Eu já vi {atores[1].nome} e {atores[0].nome} lavando outras vezes. Relaxa {atores[2].nome}\".\n"
                      f"\"Nunca fizeram nada!\"gritou {atores[2].nome}. E pelo visto a casa também não gostou das atitudes do outros.")
                crise += (f"\"Eu já vi {atores[1].nome} e {atores[0].nome} lavando outras vezes. Relaxa {atores[2].nome}.\n"
                      f"\"Nunca fizeram nada!\"gritou {atores[2].nome}. E pelo visto a casa também não gostou das atitudes do outros.")
            print("\nOs jogadores que discordaram de você foram: ")
        for jogador in maioria:
            print(jogador.nome)
        input("\nPressione Enter para prosseguir o jogo.")
        self.altera_carisma(maioria, 10, 5)
        return crise

    def crise_festa(self):
        atores = self.selecionar_atores_crise(3)
        cenarios = ["os pais", "as mães","a familia", "os animais", "o relacionamento", "a amizade"]
        causa_briga = cenarios[random.randrange(0,5)]

        print(f"{atores[0].nome} bebeu demais em uma festa e acabou ofendendo {causa_briga} de {atores[1].nome} e {atores[2].nome}\n"
              f"\n{atores[2].nome} disse que se não tivessem dentro da casa as coisas se resolveriam de outra forma.\n")

        decisao_jogador = input(f"Você concorda com {atores[2].nome}?\n[S/N] -> ")
        decisao_jogador = decisao_jogador.lower()
        decisao_jogador = 1 if decisao_jogador == "s" else 0

        maioria = self.resultado_da_crise(decisao_jogador, atores)
        crise = (f"{atores[0].nome} bebeu demais em uma festa e acabou ofendendo {causa_briga} de {atores[1].nome} e {atores[2].nome}\n"
                 f"{atores[2].nome} disse que se não tivessem dentro da casa as coisas se resolveriam de outra forma.\n")

        if maioria == 0:
            print(f"A casa separou a briga mas não achou nem que as atitudes de {atores[0].nome} estavam correta como a reação de {atores[2].nome}")
            input("Pressione Enter para prosseguir")
            crise += f"A casa separou a briga mas não achou nem que as atitudes de {atores[0].nome} estavam correta como a reação de {atores[2].nome}"
            return crise
        elif self.jogador_principal in maioria:
            if decisao_jogador == 1:
                print(f"\n\"Com {causa_briga} não se brinca!\" Você e a maioria da casa apoiaram {atores[2].nome} "
                      f"mandaram ir dormir pois já tinha acabado com a festa\n "
                      f"As suas atitudes e a da maioria da casa foram bem vistas.")
                crise += (f"\"Com {causa_briga} não se brinca!\" Você e a maioria da casa apoiaram {atores[2].nome} "
                      f"mandaram ir dormir pois já tinha acabado com a festa\n "
                      f"As suas atitudes e a da maioria da casa foram bem vistas.")
            else:
                print(f"\n\"{atores[2].nome} é só o alcool falando, releva.\" Você tentou amenizar o lado {atores[0].nome} e a casa concordou.\n"
                      f"\nVocê achou que a atitude de {atores[2].nome} foi desproporcional a situação.")
                crise += (f"\n\"{atores[2].nome} é só o alcool falando, releva.\" Você tentou amenizar o lado {atores[0].nome} e a casa concordou.\n"
                          f"Você achou que a atitude de {atores[2].nome} foi desproporcional a situação.")
            print("\nOs jogadores que concordaram com você foram: ")
        else:
            if decisao_jogador == 1:
                print(f"\n\"{atores[2].nome} mete a porrada logo, não espera!\", disse você enquanto segurava um copo cheio de vodka.\n "
                      f"\nPorém para a maioria da casa achou que a sua atitude só causaria mais intriga na casa.")
                crise += (f"\n\"{atores[2].nome} mete a porrada logo, não espera!\", disse você enquanto segurava um copo cheio de vodka.\n "
                          f"Porém para a maioria da casa achou que a sua atitude só causaria mais intriga na casa.")
            else:
                print(f"\n\"{atores[0].nome} bebeu demais, pra que julgar?\", você disse para {atores[2].nome} e {atores[1].nome}.\n"
                    f"\n\"Você não faria nada se ele falasse merda sobre {causa_briga}?\"gritou {atores[1].nome}. E a casa concordou com ele.")
                crise += (f"\n\"{atores[0].nome} bebeu demais, pra que julgar?\", você disse para {atores[2].nome} e {atores[1].nome}.\n"
                          f"\"Você não faria nada se ele falasse merda sobre {causa_briga}?\"gritou {atores[1].nome}. E a casa concordou com ele.")
            print("\nOs jogadores que discordaram de você foram: ")
        for jogador in maioria:
            print(jogador.nome)
        input("\nPressione Enter para prosseguir o jogo.")
        self.altera_carisma(maioria, 17, 11)
        return crise

    def crise_prova_lider(self):
        atores = self.selecionar_atores_crise(2)
        print(
            f"{atores[0].nome} alegou que em uma prova passada {atores[1].nome} o atrapalhou e isso ocasionou em sua derrota.\n"
            f"\n\"Respeita minha historia {atores[0].nome}\", respondeu furiosamente {atores[1].nome}.\n"
            f"\n\"Sua incapacidade de vencer não é culpa minha!\", exclamou {atores[1].nome}.\n")

        decisao_jogador = input(f"Você concorda com {atores[1].nome}?\n[S/N] -> ")
        decisao_jogador = decisao_jogador.lower()
        decisao_jogador = 1 if decisao_jogador == "s" else 0

        maioria = self.resultado_da_crise(decisao_jogador, atores)
        crise = (f"{atores[0].nome} alegou que em uma prova passada {atores[1].nome} o atrapalhou e isso ocasionou em sua derrota. \n"
                f"\"Respeita minha historia {atores[0].nome}\", respondeu furiosamente {atores[1].nome}. \n"
                f"\"Sua incapacidade de vencer não é culpa minha!\", exclamou {atores[1].nome}. ")

        if maioria == 0:
            print("A casa amenizou a situação e disse que haverá outras provas onde ambos poderão mostrar quem é o melhor.")
            input("Pressione Enter para prosseguir")
            crise += "A casa amenizou a situação e disse que haverá outras provas onde ambos poderão mostrar quem é o melhor."
            return crise
        elif self.jogador_principal in maioria:
            if decisao_jogador == 1:
                print(f"\n\"Não seja um mal perdedor {atores[0].nome}.\" Pra você {atores[0].nome} apenas estava fazendo "
                      f"tempestade em copo d'água. "
                      f"As suas atitudes e a da maioria da casa foram bem vistas.")
                crise += (f"\"Não seja um mal perdedor {atores[0].nome}.\" Pra você {atores[0].nome} apenas estava fazendo "
                      f"tempestade em copo d'água. "
                      f"As suas atitudes e a da maioria da casa foram bem vistas.")
            else:
                print(f"\n\"{atores[0].nome}, não só dessa vez como em outras.\" Você também acha que {atores[1].nome} roubou nas provas.\n"
                    f"\nA casa também concorda que {atores[1].nome} talvez não tenha agido com honestidade.")
                crise += (f"\"{atores[0].nome}, não só dessa vez como em outras.\" Você também acha que {atores[1].nome} roubou nas provas. \n"
                          f"A casa também concorda que {atores[1].nome} talvez não tenha agido com honestidade.")
            print("\nOs jogadores que concordaram com você foram: ")
        else:
            if decisao_jogador == 1:
                print(f"\n\"{atores[1].nome} tá certo. Perdeu, perdeu. Culpa sua!\", disse você enquanto abraçava {atores[1].nome}.\n "
                    f"\nPorém para a maioria da casa você apenas estava sendo oportunista.")
                crise += (f"\n\"{atores[1].nome} tá certo. Perdeu, perdeu. Culpa sua!\", disse você enquanto abraçava {atores[1].nome}.\n "
                    f"\nPorém para a maioria da casa você apenas estava sendo oportunista.")
            else:
                print(f"\n\"{atores[0].nome}, houve injustiça mesmo, deveriam rever a prova\". Disse você apoiando {atores[0].nome}\n"
                    f"\n\"Insanidade de vocês, não tem nem como roubar aqui\", disse uma voz dentre os apoiadores de {atores[1].nome}.\n"
                      f"\nVocê escolheu a minoria.")
                crise += (f"\"{atores[0].nome}, houve injustiça mesmo, deveriam rever a prova\". Disse você apoiando {atores[0].nome}\n"
                          f"\"Insanidade de vocês, não tem nem como roubar aqui\", disse uma voz dentre os apoiadores de {atores[1].nome}.\n"
                          f"Você escolheu a minoria.")
        for jogador in maioria:
            print(jogador.nome)
        input("\nPressione Enter para prosseguir o jogo.")
        self.altera_carisma(maioria, 10, 5)
        return crise
    '''
    def crise_higiene(self):
        #JACKIE
        pass

    def crise_desperdicio_de_agua(self):
        #JACKIE
        pass

    def crise_roubar_comida(self):
        pass

    def crise_conflito(self):
        pass

    def crise_comentario(self):
        #JACKIE
        pass
    '''