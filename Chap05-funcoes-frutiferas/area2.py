#!/usr/bin/env python3

# Exemplo de composicao

import math


# from raio import area
# from calcula_distancia import distancia

def area(raio):
   return math.pi * raio**2


def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dquadrado = dx**2 + dy**2
    resultado = math.sqrt(dquadrado)
    return resultado


def area2(xc, yc, xp, yp):
    raio = distancia(xc, yc, xp, yp)
    resultado= area(raio)
    print(resultado)


area2(1,2,4,6)