#!/usr/bin/env python3


def existe(nomeDoArquivo):
    try:
        f =open(nomeDoArquivo)
        f.close()
        return 1
    except:return 0

print(existe('teste.dat'))