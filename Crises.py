import random


class Crise:
    def __init__(self, semana:int, participantes:list, jogador_principal):
        self.semana = semana
        self.participantes = participantes
        self.jogador_principal = jogador_principal

    def selecao_de_crise(self):
        if self.semana >= 1 and self.semana <= 3:
            selecao_crise = random.randrange(1,3) #MODIFICAR PARA 4
            if selecao_crise == 1:
                return self.crise_organizacao_casa()
            elif selecao_crise == 2:
                return self.crise_louca()
            else:
                return self.crise_higiene()
        elif self.semana >= 4 and self.semana <= 7:
            selecao_crise = random.randrange(1,4)
            if selecao_crise == 1:
                return self.crise_festa()
            elif selecao_crise == 2:
                return self.crise_organizacao_casa()
            elif selecao_crise == 3:
                return self.crise_louca()
            else:
                return self.crise_comentario()
        elif 8 >= self.semana >= 10:
            selecao_crise = random.randrange(1, 5) #MODIFICAR PARA 4
            if selecao_crise == 1:
                return self.crise_prova_lider()
            elif selecao_crise == 2:
                return self.crise_comentario()
            elif selecao_crise == 3:
                return self.crise_festa()
            if selecao_crise == 4:
                return self.crise_organizacao_casa()
            else:
                return self.crise_conflito()
        else:
            return "Não houve crise"

    def resultado_da_crise(self, escolha_jogador, atores):
        jogadores_decisao = self.participantes.copy()
        pro = []
        contra = []

        for jogador in atores:
            jogadores_decisao.remove(jogador)

        pro.append(self.jogador_principal) if escolha_jogador == 1 else contra.append(self.jogador_principal)

        for jogador in jogadores_decisao:
            escolha_maquina = random.randrange(1, 10)
            if jogador != self.jogador_principal:
                pro.append(jogador) if escolha_maquina >= 5 else contra.append(jogador)

        if len(pro) > len(contra):
            return pro
        elif len(contra) > len(pro):
            return contra
        else:
            return 0

    def selecionar_atores_crise(self, quantidade):
        atores = []
        copia_participantes = self.participantes.copy()
        copia_participantes.remove(self.jogador_principal)
        while len(atores) < quantidade:
            jogador_selecionado = random.randrange(0,len(copia_participantes)-1)
            if copia_participantes[jogador_selecionado] not in atores:
                atores.append(copia_participantes[jogador_selecionado])
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
              f"\nAchando injusto a atitudes tomadas, {atores[2].nome} e {atores[3].nome} resolveram tirar satisfação "
              f"causando uma pequena confunsão.\n"
              f"\n{atores[2].nome} alegou que a postura de {atores[1].nome} causaria grande conflitos posteriormente "
              f"caso não seguisse o combinado.\n")

        errado = True

        while errado:
            decisao_jogador = input(f"Você apoia a postura de {atores[2].nome} e {atores[3].nome}?\n[S/N] -> ")
            decisao_jogador = decisao_jogador.lower()
            if decisao_jogador != "s" and decisao_jogador != "n":
                print("\nPor favor, informe um valor válido.")
            else:
                decisao_jogador = 1 if decisao_jogador == "s" else 0
                errado = False

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
        self.altera_carisma(maioria, 13, 7)
        return crise

    def crise_louca(self):
        atores = self.selecionar_atores_crise(3)
        print(f"Em uma casa é necessário organização, mas {atores[0].nome} e {atores[1].nome} comeram em diversos pratos diferentes e não lavaram a louça.\n"
              f"\n{atores[2].nome} estava de saco cheio de somente lavar a louça enquanto os outros não moviam um dedo para ajudar.\n"
              f"\n{atores[2].nome} disse que já tinha percebido a folga de {atores[1].nome} e não toleraria mais \"essa palhaçada\".\n")

        errado = True

        while errado:
            decisao_jogador = input(f"Você concorda com {atores[2].nome}?\n[S/N] -> ")
            decisao_jogador = decisao_jogador.lower()
            if decisao_jogador != "s" and decisao_jogador != "n":
                print("\nPor favor, informe um valor válido.")
            else:
                decisao_jogador = 1 if decisao_jogador == "s" else 0
                errado = False

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
                print(f"\n\"Eu já vi {atores[1].nome} e {atores[0].nome} lavando outras vezes. Relaxa {atores[2].nome}\", você comentou.\n"
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

        errado = True

        while errado:
            decisao_jogador = input(f"Você concorda com {atores[2].nome}?\n[S/N] -> ")
            decisao_jogador = decisao_jogador.lower()
            if decisao_jogador != "s" and decisao_jogador != "n":
                print("\nPor favor, informe um valor válido.")
            else:
                decisao_jogador = 1 if decisao_jogador == "s" else 0
                errado = False

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
                print(f"\n\"Com {causa_briga} não se brinca!\" Você e a maioria da casa apoiaram {atores[2].nome}, "
                      f"mandaram {atores[0].nome} ir dormir pois já tinha acabado com a festa\n "
                      f"As suas atitudes e a da maioria da casa foram bem vistas.")
                crise += (f"\"Com {causa_briga} não se brinca!\" Você e a maioria da casa apoiaram {atores[2].nome} "
                      f"mandaram {atores[0].nome} ir dormir pois já tinha acabado com a festa\n "
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

        errado = True

        while errado:
            decisao_jogador = input(f"Você concorda com {atores[1].nome}?\n[S/N] -> ")
            decisao_jogador = decisao_jogador.lower()
            if decisao_jogador != "s" and decisao_jogador != "n":
                print("\nPor favor, informe um valor válido.")
            else:
                decisao_jogador = 1 if decisao_jogador == "s" else 0
                errado = False

        maioria = self.resultado_da_crise(decisao_jogador, atores)
        crise = (f"{atores[0].nome} alegou que em uma prova passada {atores[1].nome} o atrapalhou e isso ocasionou sua derrota. \n"
                f"\"Respeita minha historia {atores[0].nome}\", respondeu furiosamente {atores[1].nome}. \n"
                f"\"Sua incapacidade de vencer não é culpa minha!\", exclamou {atores[1].nome}. ")

        if maioria == 0:
            print("A casa amenizou a situação e disse que haverá outras provas onde poderão mostrar quem é o melhor.")
            input("Pressione Enter para prosseguir")
            crise += "A casa amenizou a situação e disse que haverá outras provas onde poderão mostrar quem é o melhor."
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
                crise += (f"\"{atores[1].nome} tá certo. Perdeu, perdeu. Culpa sua!\", disse você enquanto abraçava {atores[1].nome}.\n "
                    f"Porém para a maioria da casa você apenas estava sendo oportunista.")
            else:
                print(f"\n\"{atores[0].nome}, houve injustiça mesmo, deveriam rever a prova\". Disse você apoiando {atores[0].nome}\n"
                    f"\n\"Insanidade de vocês, não tem nem como roubar aqui\", disse uma voz dentre os apoiadores de {atores[1].nome}.\n"
                      f"\nVocê escolheu a minoria.")
                crise += (f"\"{atores[0].nome}, houve injustiça mesmo, deveriam rever a prova\". Disse você apoiando {atores[0].nome}\n"
                          f"\"Insanidade de vocês, não tem nem como roubar aqui\", disse uma voz dentre os apoiadores de {atores[1].nome}.\n"
                          f"Você escolheu a minoria.")
            print("\nOs jogadores que discordaram de você foram: ")
        for jogador in maioria:
            print(jogador.nome)
        input("\nPressione Enter para prosseguir o jogo.")
        self.altera_carisma(maioria, 15, 15)
        return crise

    def crise_higiene(self):
        atores = self.selecionar_atores_crise(3)
        print(f"\"Você precisa tomar banho todos os dias, {atores[0].nome}. Tá fedendo muito.\", disse {atores[1].nome}.\n"
            f"\n\"Não seja uma pessoa incoveniente, {atores[1].nome}\", retrucou {atores[2].nome} sobre a atitude de {atores[1].nome}.\n"
            f"\n\"Moramos todos juntos nessa casa agora. O minimo que {atores[0].nome} deve fazer é tomar banho.\", exclamou {atores[1].nome}.\n")

        errado = True

        while errado:
            decisao_jogador = input(f"Você concorda com {atores[1].nome}?\n[S/N] -> ")
            decisao_jogador = decisao_jogador.lower()
            if decisao_jogador != "s" and decisao_jogador != "n":
                print("\nPor favor, informe um valor válido.")
            else:
                decisao_jogador = 1 if decisao_jogador == "s" else 0
                errado = False

        maioria = self.resultado_da_crise(decisao_jogador, atores)
        crise = (f"\"Você precisa tomar banho todos os dias, {atores[0].nome}. Tá fedendo muito.\", disse {atores[1].nome}.\n"
            f"\"Não seja uma pessoa incoveniente, {atores[1].nome}\", retrucou {atores[2].nome} sobre a atitude de {atores[1].nome}.\n"
            f"\"Moramos todos juntos nessa casa agora. O minimo que {atores[0].nome} deve fazer é tomar banho.\", exclamou {atores[1].nome}.\n")

        if maioria == 0:
            print(f"A casa ficou sem graça com a atitude de {atores[1].nome}, mas também concordava que {atores[0].nome}"
                  f"\nprecisava cuidar melhor da sua higiene pessoal.")
            input("Pressione Enter para prosseguir")
            crise += (f"A casa ficou sem graça com a atitude de {atores[1].nome}, mas também concordava que {atores[0].nome}"
                     f"\nprecisava cuidar melhor da sua higiene pessoal.\n")
            return crise
        elif self.jogador_principal in maioria:
            if decisao_jogador == 1:
                print(f"\n\"Sendo bem sincero, você está mesmo precisando de um banho, {atores[0].nome}.\" "
                      f"\n{atores[0].nome} talvez não tenha de maneira correta, mas era verdade."
                      f"As suas atitudes e a da maioria da casa foram bem vistas.")
                crise += (f"\"Sendo bem sincero, você está mesmo precisando de um banho, {atores[0].nome}.\" "
                      f"{atores[0].nome} talvez não tenha de maneira correta, mas era verdade.\n")
            else:
                print(f"\n\"{atores[0].nome}, não merece esse tipo de comentário. Peça desculpas!\"\n"
                      f"Você e a casa abominaram as atitudes de {atores[1].nome}\n")
                crise += (f"\"{atores[0].nome}, não merece esse tipo de comentário. Peça desculpas!\"\n"
                          f"Você e a casa abominaram as atitudes de {atores[1].nome}\n")
            print("\nOs jogadores que concordaram com você foram: ")
        else:
            if decisao_jogador == 1:
                print(f"\n\"{atores[0].nome}, precisamos economizar água, mas ficar dois dias sem tomar banho não dá!\", dizia você enquanto ria.\n "
                    f"\nPorém para a casa você estava apenas piorando a situação e causando mais desconforto para {atores[0].nome}.")
                crise += (f"\"{atores[0].nome}, precisamos economizar água, mas ficar dois dias sem tomar banho não dá!\", dizia você enquanto ria.\n "
                          f"Porém para a casa você estava apenas piorando a situação e causando mais desconforto para {atores[0].nome}.\n")
            else:
                print(f"\n\"{atores[1].nome}, um ou dois dias sem tomar banho não tem problema\", você comentou."
                    f"\n\"Isso é porque você também não sente seu próprio cheiro\", {atores[1].nome} enquanto os outros riam.\n"
                    f"\nA casa zombou de você e de {atores[0].nome}.")
                crise += (f"\n\"{atores[1].nome}, um ou dois dias sem tomar banho não tem problema\", você comentou.\n"
                    f"\"Isso é porque você também não sente seu próprio cheiro\", {atores[1].nome} enquanto os outros riam.\n"
                    f"A casa zombou de você e de {atores[0].nome}.")
                print("\nOs jogadores que discordaram de você foram: ")
        for jogador in maioria:
            print(jogador.nome)
        input("\nPressione Enter para prosseguir o jogo.")
        self.altera_carisma(maioria, 10, 20)
        return crise

    def crise_conflito(self):
        atores = self.selecionar_atores_crise(2)
        print(
            f"Durante uma festa {atores[0].nome} e {atores[1].nome} iniciaram uma discussão que quase terminou em agressão.\n"
            f"\nOs participantes se olharam sem saber como reagir.\n"
            f"\n{atores[1].nome} estava a ponto de socar o rosto de {atores[0].nome}.\n")

        errado = True

        while errado:
            decisao_jogador = input(f"\nVocê entrará no meio e separará a briga antes que ela aconteça."
                                    f"\n[S/N] -> ")
            decisao_jogador = decisao_jogador.lower()
            if decisao_jogador != "s" and decisao_jogador != "n":
                print("\nPor favor, informe um valor válido.")
            else:
                decisao_jogador = 1 if decisao_jogador == "s" else 0
                errado = False

        maioria = self.resultado_da_crise(decisao_jogador, atores)
        crise = (f"Durante uma festa {atores[0].nome} e {atores[1].nome} iniciaram uma discussão que quase terminou em agressão.\n"
                 f"Os participantes se olharam sem saber como reagir.\n"
                 f"{atores[1].nome} estava a ponto de socar o rosto de {atores[0].nome}.\n")

        if maioria == 0:
            print(f"\nVocê e a casa acabaram separando a briga. \"Pessoas civilizadas não se tratam assim\", disse um dos participantes.\n"
                  f"\nNinguém apoiou nenhum lado da confusão.\n")
            input("Pressione Enter para prosseguir")
            crise += (f"Você e a casa acabaram separando a briga. \"Pessoas civilizadas não se tratam assim\", disse um dos participantes.\n"
                      f"Ninguém apoiou nenhum lado da confusão.\n")
            return crise
        elif self.jogador_principal in maioria:
            if decisao_jogador == 1:
                print(f"Você se meteu no meio da confusão antes que alguém acabasse se machucando, alguns participantes te ajudaram e você\n"
                      f"foi visto como um herói.\n"
                      f"Sua atitudes foram muito bem vistas pela casa.\n")
                input("Pressione Enter para prosseguir")
                crise += (f"\nVocê se meteu no meio da confusão antes que alguém acabasse se machucando, alguns participantes te ajudaram e você\n"
                          f"foi visto como um herói.\n"
                          f"\nSua atitudes foram muito bem vistas pela casa.\n")
            else:
                print(f"\n\"E quem disse que isso é problema meu?\", você pensou em voz alta.\n"
                      f"\nA maioria dos participantes riram, e concordaram que era melhor não se meter, assim eliminava a concorrência.\n")
                crise += (f"\"E quem disse que isso é problema meu?\", você pensou em voz alta.\n"
                          f"A maioria dos participantes riram, e concordaram que era melhor não se meter, assim eliminava a concorrência.\n")
            print("\nOs jogadores que concordaram com você foram: ")
        else:
            if decisao_jogador == 1:
                print(f"\nVocê resolveu se meter, mas acabou empurrando {atores[0].nome} e {atores[2].nome} iniciou uma discussão com você.\n "
                      f"\nVocê pode não ser expulso por essa atitude, mas com certeza não ficará impune pela casa.")
                crise += (f"Você resolveu se meter, mas acabou empurrando {atores[0].nome} e {atores[2].nome} iniciou uma discussão com você.\n "
                        f"Você pode não ser expulso por essa atitude, mas com certeza não ficará impune pela casa.")
            else:
                print(f"\nVocê resolveu ficar sentado e ver o circo pegar fogo, enquanto os outros participantes resolveram separar a briga.\n"
                      f"\nTalvez você tenha tentado se manter imparcial, mas ao ver os olhares dos outros você soube que cometeu um ERRO.\n")
                crise += (f"\nVocê resolveu ficar sentado e ver o circo pegar fogo, enquanto os outros participantes resolveram separar a briga.\n"
                        f"\nTalvez você tenha tentado se manter imparcial, mas ao ver os olhares dos outros você soube que cometeu um ERRO.\n")
            print("\nOs jogadores que discordaram de você foram: ")
        for jogador in maioria:
            print(jogador.nome)
        input("\nPressione Enter para prosseguir o jogo.")
        self.altera_carisma(maioria, 25, 45)
        return crise

    def crise_comentario(self):
        atores = self.selecionar_atores_crise(4)
        print(
            f"{atores[0].nome} fez diversos comentários ofensivos sobre {atores[1].nome} com todos os participantes da casa.\n"
            f"\nEsse comentários acabaram chegando aos ouvidos de {atores[1].nome} que foi tirar satisfação.\n"
            f"\n\"É isso mesmo {atores[1].nome}, porque você é esse tipo de pessoa.\", exclamou {atores[0].nome}.\n")

        errado = True

        while errado:
            decisao_jogador = input(
                f"{atores[2].nome} perguntou se você também achava que {atores[2].nome} era esse tipo de pessoa."
                f"\n[S/N] -> ")
            decisao_jogador = decisao_jogador.lower()
            if decisao_jogador != "s" and decisao_jogador != "n":
                print("\nPor favor, informe um valor válido.")
            else:
                decisao_jogador = 1 if decisao_jogador == "s" else 0
                errado = False

        maioria = self.resultado_da_crise(decisao_jogador, atores)
        crise = (
            f"{atores[0].nome} fez diversos comentários ofensivos sobre {atores[1].nome} com todos os participantes da casa.\n"
            f"Esse comentários acabaram chegando aos ouvidos de {atores[1].nome} que foi tirar satisfação.\n"
            f"\"É isso mesmo {atores[1].nome}, porque você é esse tipo de pessoa.\", exclamou {atores[0].nome}.\n")

        if maioria == 0:
            print(f"\nVocê se manteve calado, assim como o resto da casa enquanto {atores[0].nome} e {atores[1].nome} discutiam.\"\n")
            input("\nPressione Enter para prosseguir")
            crise += (f"Você se manteve calado, assim como o resto da casa enquanto {atores[0].nome} e {atores[1].nome} discutiam.\"\n")
            return crise
        elif self.jogador_principal in maioria:
            if decisao_jogador == 1:
                print(f"\n\"Sabe como é né, {atores[2].nome}, com essas atitudes é meio dificil contrariar.\"\n"
                      f"\nSeu comentário repercutiu pela casa e as pessoas concordaram com você.\n")
                input("Pressione Enter para prosseguir")
                crise += (f"\"Sabe como é né, {atores[2].nome}, com essas atitudes é meio dificil contrariar.\"\n"
                          f"Seu comentário repercutiu pela casa e as pessoas concordaram com você.\n")
            else:
                print(f"\n\"Eu não concordo com nada que {atores[0].nome} disse.\"\n"
                      f"\nEscolher o lado de {atores[1].nome} pode ter sido uma boa opção.\n")
                crise += (f"\"Eu não concordo com nada que {atores[0].nome} disse.\"\n"
                          f"Escolher o lado de {atores[1].nome} pode ter sido uma boa opção.\n")
            print("\nOs jogadores que concordaram com você foram: ")
        else:
            if decisao_jogador == 1:
                print(
                    f"\n\"{atores[0].nome} apenas diz a verdade sobre as pessoas. {atores[1].nome} deve ser assim.\"\n "
                    f"\nSeu comentário só serviu para causar mais intrigas na casa e não foi bem visto.\n")
                crise += (f"\"{atores[0].nome} apenas diz a verdade sobre as pessoas. {atores[1].nome} deve ser assim.\"\n "
                    f"Seu comentário só serviu para causar mais intrigas na casa e não foi bem visto.\n")
            else:
                print(f"\n\"Só sai besteira da boca de {atores[0].nome}\", você comentou.\n"
                      f"\n\"Como se você fosse um sábio\", comentou {atores[3].nome}. O que acarretou em outra discussão.\n"
                      f"\nA casa já estava cansada de brigas pela semana.\n")
                crise += (f"\"Só sai besteira da boca de {atores[0].nome}\", você comentou.\n"
                          f"\"Como se você fosse um sábio\", comentou {atores[3].nome}. O que acarretou em outra discussão.\n"
                          f"A casa já estava cansada de brigas pela semana.\n")
                print("\nOs jogadores que discordaram com você foram: ")
        for jogador in maioria:
            print(jogador.nome)
        input("\nPressione Enter para prosseguir o jogo.")
        self.altera_carisma(maioria, 18, 10)
        return crise