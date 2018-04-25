#!/usr/bin/env python3


class Node:
    def __init__(self, carga=None, proximo=None):
        self.carga=carga
        self.proximo=proximo

    def __str__(self):
        return str(self.carga)

    def imprimeLista(no):
        while no:
            print(no, end=" ")
            no = no.proximo
        print()

    def imprimeDeTrasPraFrente(lista):
        if lista == None: return
        cabeca = lista
        rabo = lista.proximo
        Node.imprimeDeTrasPraFrente(rabo)
        print(cabeca, end=" ")

    def removeSegundo(lista):
        if lista == None: return
        primeiro = lista
        segundo = lista.proximo     #faz primeiro 'no' se referir ao terceiro
        primeiro.proximo = segundo.proximo
        segundo.proximo = None     #separa  o segundo 'no' do resto da lista
        return segundo


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def isEmpty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.head == None: # if list is empty the new node goes first
            self.head = node
        else:
            # find the last node in the list
            last = self.head
            while last.next: last = last.next
            # append new node
            last.next = node
        self.length = self.length + 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length  = self.length -1
        return cargo


class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def isEmpty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.length == 0:
            #if list is empty, the new node is head and last
            self.head = self.last = node
        else:
            #find the last node
            last = self.last
            #append new node
            last.next = node
            self.last = node
        self.length = self.length + 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length -1
        if self.length == 0:
            self.last = None
        return cargo


class PriorityQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        self.items[maxi:maxi + 1] = []
        return item


class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return ("%-16s: %d" % (self.name, self.score))

    def __cmp__(self, other):
        if self.score < other.score: return 1 # less is more
        if self.score > other.score: return -1
        return 0



# q = PriorityQueue()
# q.insert(11)
# q.insert(12)
# q.insert(14)
# q.insert(13)
# while not q.isEmpty():print(q.remove())


tiger = Golfer("Tiger Woods", 61)
phil = Golfer("Phil Mickelson", 72)
hal = Golfer("Hall Sutton",69)

pq = PriorityQueue()
pq.insert(tiger)
pq.insert(phil)
pq.insert(hal)
while not pq.isEmpty():print(pq.remove())

'''line 106, in remove
    if self.items[i] >= self.items[maxi]:
TypeError: '>=' not supported between instances of 'Golfer' and 'Golfer'''