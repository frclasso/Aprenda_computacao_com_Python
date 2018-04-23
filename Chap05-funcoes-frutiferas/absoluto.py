#!/usr/bin/env python3


def valorAbs(x):
    if x == 0:
        return 0
    elif x < 0:
        return -x
    elif x > 0:
        return x


print(valorAbs(2))
print(valorAbs(-1))
print(valorAbs(0))