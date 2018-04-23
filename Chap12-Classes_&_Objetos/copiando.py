#!/usr/bin/env python3

import copy

class Ponto:
    pass


p1 = Ponto()
p1.x =3
p1.y = 4
p2 = copy.copy(p1)
print(p1 == p2)


def mesmoPonto(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y )


print(mesmoPonto(p1, p2))