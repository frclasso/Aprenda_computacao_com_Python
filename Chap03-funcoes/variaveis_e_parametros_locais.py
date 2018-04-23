#!/usr/bin/env python3


def imprime_dobrado(nome):
    print (nome, nome)


def concatDupla(part1 , part2):
    concat = part1 + part2
    imprime_dobrado(concat)

#Esta função recebe dois argumentos, concatena-os, e então
# imprime o resultado duas vezes.
# Podemos chamar a função com duas strings:

canto1 = 'Pie Jesus domine'
canto2 = ' Dona eis requiem.'
concatDupla(canto1,canto2)