#!/usr/bin/env python3

import math


def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    # print(f'dx vale {dx}')  # variveis temporarias
    # print(f'dy vale {dy}')
    dquadrado = dx**2 + dy**2
    #print(f'dquadrado vale {dquadrado}')
    resultado = math.sqrt(dquadrado)
    return resultado



#print(distancia(1,2,4,6))