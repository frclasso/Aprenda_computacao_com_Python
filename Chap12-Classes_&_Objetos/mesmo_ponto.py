#!/usr/bin/env python3


class Ponto:
    pass


p1 = Ponto()
p1.x = 3
p1.y = 4

p2 = Ponto()
p2.x = 3
p2.y = 4

print(p1 == p2) # False

"""Este tipo de igualdade é chamado de igualdade rasa porque ela compara 
somente as referências e não o conteúdo dos objetos."""
p2 = p1
print(p2 == p1) # True


def mesmoPonto(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y )


print(mesmoPonto(p1, p2)) # True

