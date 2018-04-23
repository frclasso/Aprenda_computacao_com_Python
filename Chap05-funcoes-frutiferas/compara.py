#!/usr/bin/env python3


def compara(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

print(compara(1,2))
print(compara(3,2))
print(compara(3,3))