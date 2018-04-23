#!/usr/bin/env python3


def fatorial(n):
    if type(n) != type(1):
        print('Fatorial eh somente definido para inteiros.')
        return -1
    elif n < 0:
        print('Fatorial eh somente definido para  inteiros positivos.')
        return -1
    elif n == 0:
        return 1
    else:
        return n * fatorial(n-1)


print(fatorial(6))
print(fatorial('fred'))
print(fatorial(-2))