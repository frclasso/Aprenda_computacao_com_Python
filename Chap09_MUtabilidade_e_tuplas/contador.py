#!/usr/bin/env python3


def noIntervalo(lista, inferior, superior):
    contador = 0
    for numero in lista:
      if inferior < numero < superior:
        contador = contador + 1
    return contador


lista = []
numeroDeIntervalos = 8
intervalos = [0] * numeroDeIntervalos
larguraDoIntervalo = 1.0 / numeroDeIntervalos
for i in range(numeroDeIntervalos):
    inferior = i * larguraDoIntervalo
    superior = inferior + larguraDoIntervalo
    intervalos[i] = noIntervalo(lista, inferior, superior)
print(intervalos)

# numeroDeIntervalos = 8
# intervalos = [0] * numeroDeIntervalos
# for i in lista:
#     indice = int(i * numeroDeIntervalos)
#     intervalos[indice] = intervalos[indice]+ 1
# print(intervalos)