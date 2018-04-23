#!/usr/bin/env python3

f = open('teste.dat', 'w')
#print(f)
f.write('Agora e a hora ')
f.write('de fechar o arquivo.')
f.close()

f = open('teste.dat', 'r')
texto = f.read()
print(texto)

f = open('teste.dat', 'w')
f.write('Linha um\nLinhas dois\nLinhas tres')
f.close()

f = open('teste.dat', 'r')
print(f.readline()) # Linha um

print(f.readlines()) # readlines retorna todas as linhas restantes como uma lista de strings

print(f.readline()) # retorna a string vazia
print(f.readlines())  # retorna lista vazia