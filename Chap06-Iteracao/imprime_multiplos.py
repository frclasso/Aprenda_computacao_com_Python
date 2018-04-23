#!/usr/bin/env python3


def imprimeMultiplos(n, altura): # altura refere-se a tabuada nesse caso.
    i = 1
    while i <= altura:
        print (n, 'x', i, '=', n*i, '\t',)
        i = i + 1
    print()

# teste da funcao imprimeMultiplos
# imprimeMultiplos(3, 2)


def imprimeTabMult(altura):  # altura nesse caso refere-se ao numero maximo
    i = 1
    while i <= altura:
        imprimeMultiplos(i, altura)  # chamda da funcao imprimeMultiplos
        i = i + 1

# chamada da funcao imprimeTabMult
imprimeTabMult(6)