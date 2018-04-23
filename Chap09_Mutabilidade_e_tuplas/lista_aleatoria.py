#!/usr/bin/env python3

import random


def listAleatoria(n):
    s = [0] * n
    for i in range(n):
        s[i] = random.random()
    return s


print(listAleatoria(4))
