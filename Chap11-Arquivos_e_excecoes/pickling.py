#!/usr/bin/env python3


"""Pickling preserva a estrutura de dados original,
 evitando conversoes de int para str"""

import pickle

f = open('teste.pck', 'wb')

pickle.dump(12.3, f)
pickle.dump([1,2,3, ], f)
f.close()

with open('teste.pck','rb') as f:
     x = pickle.load(f)
     y = pickle.load(f)
print(x)
print(y)

print('ou...')

f = open('teste.pck', 'rb')
x = pickle.load(f)
y = pickle.load(f)
print(x)
print(y)
