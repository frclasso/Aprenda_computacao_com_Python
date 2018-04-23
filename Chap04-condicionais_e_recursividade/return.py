#!/usr/bin/env python3

"""O comando return permite terminar a execução de uma função antes que ela alcance seu fim.
 Uma razão para usá-lo é se você detectar uma condição de erro"""


import math


def imprimeLogaritmo(x):
    if x <= 0:
        print('Somente numeros positivos.')
        return
    resultado = math.log(x)
    print(f'O logo de x eh {resultado}')


imprimeLogaritmo(-1)