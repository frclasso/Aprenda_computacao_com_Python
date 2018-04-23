#!/usr/bin/env python3


def nLinhas(n):
    if n > 0:
        print('**********')
        nLinhas(n-1)  # o número total de novas linhas é 1 + (n-1) que, vem a ser o próprio n.


nLinhas(5)