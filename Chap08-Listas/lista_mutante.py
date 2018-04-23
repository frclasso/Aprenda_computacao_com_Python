#!/usr/bin/env python3

frutas = ['banana', 'abacaxi', 'laranja']
print(frutas)
frutas[0] = 'abacate'
frutas[-1] = 'tangerina'
print(frutas)

print()

lista = ['a', 'b', 'c', 'd','e', 'f']
lista[1:3] = ['x', 'y']
print(lista)
lista[1:3] = []
print(lista)
lista[1:1] = ['b', 'c']
print(lista)
print()

#Utilizando del para remover itens de uma lista
a = ['um', 'dois', 'tres']
del a[1]
print(a)
print()

outraLista =['a', 'b', 'c', 'd', 'e', 'f']
del outraLista[1:5]
print(outraLista)
print()

a = 'banana'
b = 'banana'
print(id(a))
print(id(b)) # mesmo id de a, ou seja, refere-se ao mesmo objeto
print()

c = ['1', '2', '3']
d = ['1', '2', '3']
print(id(c))
print(id(d))
e = c
print(id(e)) # mesmo id de c, ou seja, refere-se ao mesmo objeto
e[0] = 5
print(c)
print()

f = c[:]  # faz uma copia da lista c
print(f)
print(id(f)) # id's diferentes, ou seja, objetos diferentes