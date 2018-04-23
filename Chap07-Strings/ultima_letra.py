#!/usr/bin/env python3


def indice_palavra(fruta):
    indice = 0
    while indice < len(fruta):
        letra = fruta[indice]
        print(letra)
        indice = indice+1


indice_palavra('apple')

print()


def ultima_letra(fruta):
    ultima = fruta[-1]
    print('Ultima letra da palavra:',ultima)


ultima_letra('apple')