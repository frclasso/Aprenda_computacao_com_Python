#!/usr/bin/env python3


def contaLetras(palavra, n):
    contador = 0
    for letra in palavra:
        if letra == n:
        # if letra == 'a':
            contador += 1
    print(contador)


contaLetras('macarronada', 'a')