#!/usr/bin/env python3


def compara_numeros(x, y):
    if x > y:
        print(f'{x} eh maior que {y}')
    elif x < y:
        print(f'{x} eh menor que {y}')
    else: print(f'{x} e {y} sao iguais.')


compara_numeros(2,3)
compara_numeros(4,3)
compara_numeros(5,5)