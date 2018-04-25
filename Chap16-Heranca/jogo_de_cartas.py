#!/usr/bin/env python3


class Carta:
    listaDeNaipes = ["Paus", "Ouros", "Copas", "Espadas"]
    listaDePosicoes = ["narf", "Ás", "2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "Valete","Dama","Rainha", "Rei"]

    def __init__(self, naipe=0, posicao=0):
        self.naipe = naipe
        self.posicao = posicao

    def __str__(self):
        return (self.listaDePosicoes[self.posicao] + " de " +
                self.listaDeNaipes[self.naipe])

    def __cmp__(self, other):
        # verificar os naipes
        if self.naipe > other.naipe: return 1
        if self.naipe < other.naipe: return -1
        # as cartas têm o mesmo naipe... verificar as posições
        if self.posicao > other.posicao: return 1
        if self.posicao < other.posicao: return -1
        # as posições são iguais... é um empate
        return 0


class Baralho:
    def __init__(self):
        self.cartas = []
        for naipe in range(4):
            for posicao in range(1, 14):
                self.cartas.append(Carta(naipe, posicao))

    def imprimirBaralho(self):
        for carta in self.cartas:
            print(carta)

    def __str__(self):
        s = ""
        for i in range(len(self.cartas)):
            s = s + " " * i + str(self.cartas[i]) + "\n"
        return s

    def embaralhar(self):
        import random
        nCartas = len(self.cartas)
        for i in range(nCartas):
            j = random.randrange(i, nCartas)
            self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]

    def removeCarta(self, carta):
        if carta in self.cartas:
            self.cartas.remove(carta)
            return 1
        else:
            return 0

    def distruibuirCartas(self):
        return self.cartas.pop()

    def estahVazia(self):
        return (len(self.cartas) == 0)

    def distribuir(self, maos, nCartas=999):
        nMaos = len(maos)
        for i in range(nCartas):
            if self.estahVazia(): break  # interromper se acabaram as cartas
            carta = self.pegarCarta()  # pegar a carta do topo # Erro
            mao = maos[i % nMaos]  # quem deve receber agora?
            mao.adicionarCarta(carta)  # adicionar a carta à mao

    def pegarCarta(self):  # EDITAR METODO
        pass


class Mao(Baralho):
    def __init__(self, nome=""):
        self.cartas = []
        self.nome = nome

    def adicionarCarta(self, carta):
        self.cartas.append(carta)

    def __str__(self):
        s = "Mao" + self.nome
        if self.estahVazia():
            return s +" esta vazia\n"
        else:
            return s + " contem \n" + Baralho.__str__(self)


class JogoDeCartas:
    def __init__(self):
        self.baralho = Baralho()
        self.baralho.embaralhar()

    def exibirMaos(self):   # EDITAR METODO
        pass


class MaoDeMico(Mao):
    def descartarCasais(self):
        conta = 0
        cartasIniciais = self.cartas[:]
        for carta in cartasIniciais:
            casal = Carta(3 - carta.naipe, carta.valor )
            if casal in self.cartas:
                self.cartas.remove(carta)
                self.cartas.remove(casal)
                print('Mao %s: %s casais %s ' % (self.nome, carta, casal))
                conta = conta +1
        return conta


class Mico(JogoDeCartas):
    def jogar(self, nomes):
        # removendo Dama de Paus
        self.baralho.removeCarta(Carta(0, 13))

        #fazer uma mao para cada jogador
        self.maos = []
        for nome in nomes:
            self.maos.append(MaoDeMico(nome))

        #distribuir cartas
        self.baralho.distribuir(self.maos)
        print('---------- As cartas foram dadas')
        self.exibirMaos()

        #remover casais iniciais
        casais = self.removerTodosOsCasais()
        print('----------- Os pares foram descartados')
        self.exibirMaos()

        #jogar ate que 25 casais se formem
        vez = 0
        numMaos = len(self.maos)
        while casais < 25:
            casais = casais + self.jogarVez(vez)
            vez = (vez + 1) % numMaos

        print("---------- Fim de jogo.")
        self.exibirMaos()

    def removerTodosOsCasais(self):
        conta = 0
        for mao in self.maos:
            conta = conta + mao.descartarCasais()
        return conta

    def jogarVez(self, i):
        if self.maos[i].estahVazia():
            return 0
        vizinho = self.buscarVizinho(i)
        novaCarta = self.maos[vizinho].pegarCarta()
        self.maos[i].adicionarCarta(novaCarta)
        print('Mao ', self.maos[i].nome, 'pegou', novaCarta)
        conta = self.maos[i].embaralhar()
        return conta

    def buscarVizinho(self, i):
        numMaos =len(self.maos)
        for next in range(1, numMaos):
            vizinho = (i + next) % numMaos
            if not self.maos[vizinho].estahVazia():
                return vizinho


# baralho = Baralho()
# baralho.embaralhar()
# mao = Mao("Fabio")
# baralho.distribuir([mao], 5)
# print(mao)

#
# jogo = JogoDeCartas()
# mao = MaoDeMico("Fabio")
# jogo.baralho.distribuir([mao], 13)
# print(mao)

#mao.descartarCasais()

# jogo = Mico()
# jogo.jogar(['Alice', 'Jair', 'Clara'])


"""Erros: faltam o metodos  (exibirMaos) e  (pegarCarta)
        
        line 107, in descartarCasais  casal = Carta(3 - carta.naipe, carta.valor )
        AttributeError: 'NoneType' object has no attribute 'naipe'      
"""