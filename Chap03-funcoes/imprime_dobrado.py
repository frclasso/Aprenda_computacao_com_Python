#!/usr/bin/env python3

import math

def imprime_dobrado(nome):
    print (nome, nome)


imprime_dobrado('Spam')
imprime_dobrado(5)
imprime_dobrado(3.14159)
imprime_dobrado('Spam' * 4)
imprime_dobrado(math.cos(math.pi))
imprime_dobrado('Spam*4')

#Usando uma variavel como argumento
miguel = 'Eric, the half a bee.'
imprime_dobrado(miguel)