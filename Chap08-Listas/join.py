
# A funcao 'join' faz o contrario de 'split', junta

import string


lista = ["O", 'orvalho', 'no', 'carvalho']
#print(type(lista))

outraLista = str(lista)
#print(type(outraLista))
print(outraLista)
print(str.join(' ', ('O','orvalho', 'no', 'carvalho')))
