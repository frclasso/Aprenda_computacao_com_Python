#!/usr/bin/env python3


def cabeca(lista):
    return lista[0]


def removeCabeca(lista):
    del lista[0]


def cauda(lista):
    return lista[1:]


def main():
    numeros = [1,2,3]
    print(cabeca(numeros))

    removeCabeca(numeros)
    print(numeros)

    resto = cauda(numeros)
    print(resto)


if __name__=="__main__":main()