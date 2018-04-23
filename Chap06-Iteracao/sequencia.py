#!/usr/bin/env python3


def sequencia(n):
    while n != 1:
        print(n, end='- ')
        if n % 2 == 0:
            n = n/2
        else:
            n = n * 3+1


sequencia(3)