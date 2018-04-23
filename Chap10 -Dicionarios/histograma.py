#!/usr/bin/env python3

 # histograma, quantas vezes cada letra aparece na string.

letterCounts = {}
for letter in 'Mississipi':
    letterCounts[letter] = letterCounts.get(letter, 0) + 1

print(letterCounts)


"""Começamos com um dicionário vazio. Para cada letra da string, achamos
 o contador (possivelmente zero) e o incrementamos. No final, o dicionário
  contem pares de letras e as suas frequências.

"""
"""items retorna em tuplas (key and values), sorted retorna em ordem alfabetica"""
letterItems = sorted(letterCounts.items())
print(letterItems)

