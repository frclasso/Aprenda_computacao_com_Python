#!/usr/bin/env python3

import math


class Ponto:
    pass


final = Ponto()
final.x = 3.0
final.y = 4.0


def distancia(a, b):
    dquadrado = a**2 + b**2
    resultado = math.sqrt(dquadrado)
    return resultado


print(distancia(final.x, final.y))