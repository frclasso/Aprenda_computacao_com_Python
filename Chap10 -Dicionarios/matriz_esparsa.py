#!/usr/bin/env python3

matriz1 = [
    [0,0,0,1,0],
    [0,0,0,0,0],
    [0,2,0,0,0],
    [0,0,0,0,0],
    [0,0,0,3,0]
          ]
#print(matriz1)

matriz2 ={
    (0, 3): 1,
    (2, 1): 2,
    (4, 3): 3
}

print(matriz2)
print(matriz2[0, 3]) # a saida eh o valor
print(matriz2[2, 1])
#print(matriz2[1, 3])  # gera erro
print()
print(matriz2.get((0, 3), 0)) # retorna '1' se encontra a chave
print(matriz2.get((1, 3), 0)) # retorna '0' se NAO encontra a chave