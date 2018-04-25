#!/usr/bin/env python3


class No:
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

    # def imprimeDeTrasPraFrente(self):
    #     if self.proximo == None:
    #         rabo = lista.proximo
    #         rabo = No.imprimeDeTrasPraFrente()
    #     print(self.carga, end=" ")

    def imprimeDeTrasPraFrente(lista):
        if lista == None: return
        cabeca = lista
        rabo = lista.proximo
        No.imprimeDeTrasPraFrente(rabo)
        print(cabeca, end=" ")

    def removeSegundo(lista):
        if lista == None: return
        primeiro = lista
        segundo = lista.proximo     #faz primeiro 'no' se referir ao terceiro
        primeiro.proximo = segundo.proximo
        segundo.proximo = None     #separa  o segundo 'no' do resto da lista
        return segundo


class listaLigada:
    def __init__(self):
        self.comprimento = 0
        self.cabeca = None

    def imprimeDeTrasParaFrente(self):
        print("[")
        if self.cabeca != None:   #ERRO
            self.cabeca.imprimeDeTrasParaFrente()
        print("]")

    def adicionarPrimeiro(self, carga):
        no = No(carga)
        no.proximo = self.cabeca
        self.cabeca = no
        self.comprimento = self.comprimento+1

no = No('teste')
# print(no)
no1 = No(1)
no2 = No(2)
no3 = No(3)

no1.proximo = no2
no2.proximo = no3

No.imprimeLista(no1)

removido = No.removeSegundo(no1)
No.imprimeLista(removido)

No.imprimeLista(no1)

No.imprimeDeTrasPraFrente(no1)

print()
#listaLigada.imprimeDeTrasParaFrente(no1)
