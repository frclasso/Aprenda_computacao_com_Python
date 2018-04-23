#!/usr/bin/env python3
import string


def ehMinusculo(ch):
    return ch in string.ascii_lowercase


print('Eh Minusculo')
print(ehMinusculo('a'))  # True
print(ehMinusculo('A'))  # False
print()


def ehMaiusculo(ch):
    return ch in string.ascii_uppercase


print('Eh Maisuculo:')
print(ehMaiusculo('B'))  # True
print(ehMaiusculo('b'))  # False
print()


def isDigit(ch):
    return ch in string.digits

print('IsDigit:')
print(isDigit('1'))  # True
print(isDigit('a'))  # False