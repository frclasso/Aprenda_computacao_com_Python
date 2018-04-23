#!/usr/bin/env python3


class Carta:
    listaDeNaipes = ["Paus", "Ouros", "Copas", "Espadas"]
    listaDePosicoes = ["narf", "Ás", "2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "Valete", "Rainha", "Rei"]

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

    def estahVazio(self):
        return len(self.cartas == 0)

# teste da classe Carta
# carta1 = Carta(1, 3)
# print(carta1)

baralho = Baralho()
print(baralho)
