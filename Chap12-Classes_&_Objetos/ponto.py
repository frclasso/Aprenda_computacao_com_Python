#!/usr/bin/env python3

class Ponto:
    pass


final = Ponto()
final.x = 3.0
final.y = 4.0

# print(final.x)
# print(id(final.x))
# print(final.y)
# print(id(final.y))
#
# print('(' + str(final.x) + ', ' + str(final.y) + ')')
# distAoQuadrado = final.x * final.x + final.y * final.y
# print(distAoQuadrado)


def mostraPonto(p):
    print('(' + str(p.x) + ', ' + str(p.y) + ')')


mostraPonto(final)