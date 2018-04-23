#!/usr/bin/env python3


def find(str, ch):
    indice = 0
    while indice < len(str):
        if str[indice] == ch:
            print(f'Achou caractere "{ch}" na posicao "{indice}".')
            return indice
        indice += 1
    return -1


find('banana', 'a')