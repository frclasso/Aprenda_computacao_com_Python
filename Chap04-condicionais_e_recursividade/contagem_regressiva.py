#!/usr/bin/env python3


def contagemRegressiva(n):
    if n == 0:
        print('Fogo!!!')
    else:
        print(n)
        contagemRegressiva(n -1)  # chamada recursiva


contagemRegressiva(3)