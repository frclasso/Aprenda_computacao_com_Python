#!/usr/bin/env python3


def fatorial(n):
    if n == 0:
        return 1
    else:
        # recursivo = fatorial(n-1) # variaveis temporarias
        # resultado = n * recursivo
        # return resultado
        return n * fatorial(n-1)


print(fatorial(6))