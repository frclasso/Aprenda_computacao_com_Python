#!/usr/bin/env python3


def filtraArquivo(velhoArquivo, novoArquivo):
    f1 = open(velhoArquivo, 'r')
    f2 = open(novoArquivo, 'w')
    while 1:
        texto = f1.readline()
        if texto == "":
            break
        if texto[0] == "#":
            continue
        f2.write(texto)
    f1.close()
    f2.close()
    return