#!/usr/bin/env python3

cavaleiros = ['morte', 'guerra', 'peste', 'fome']

i = 0
while i < len(cavaleiros): # melhor utilizar a funcao len do que uma constante
# while i < 4:
    print(cavaleiros[i])
    i +=1

print()
print('peste' in cavaleiros) # True
print('depravacao' in cavaleiros) # False
print('depravacao' not in cavaleiros) # True

print()
for cavaleiro in cavaleiros:
    print(cavaleiro, end=' ,')