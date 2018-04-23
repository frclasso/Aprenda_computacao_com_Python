#!/usr/bin/env python3

"""O Teorema de Pitágoras diz que: “a soma dos quadrados dos catetos é igual
ao quadrado da hipotenusa.”"""

import math


def calculaHipotenusa(x, y):
    z = x**2 + y**2
    hipo = math.sqrt(z)
    return hipo


print(calculaHipotenusa(9,12))