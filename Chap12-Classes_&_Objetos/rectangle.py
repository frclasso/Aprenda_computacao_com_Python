#!/usr/bin/env python3


class Ponto:
    def final(self):
        self.final()


class Rectangle:
    def corner(self, x, y):
        self.corner()
        # self.corner.x = x
        # self.corner.y = y

final = Ponto()
final.x = 3.0
final.y = 4.0


box = Rectangle()
box.width = 100.0
box.height = 200.0

box.corner = Ponto()
box.corner.x = 0.0
box.corner.y = 0.0

def mostraPonto(p):
    print('(' + str(p.x) + ', ' + str(p.y) + ')')

mostraPonto(final)

def findCenter(box):
    p = Ponto()
    p.x = box.corner.x + box.width/2.0
    p.y = box.corner.y + box.height/2.0

    center = findCenter(box)
    print(mostraPonto(center))  # Error AttributeError: 'NoneType' object has no attribute 'x'

box.width = box.width + 50
box.height = box.height + 100


def growRect(box, dwidth, dheight):
    import copy
    newbox = copy.deepcopy(box)
    newbox.width = newbox.widht + dwidth
    newbox.height = newbox.height = dheight
    return newbox


bob = Rectangle()
bob.width = 100.0
# bob.height = 200.0
# bob.corner.x = 0.0
# bob.corner.y = 0.0
# growRect(bob, 50, 100)