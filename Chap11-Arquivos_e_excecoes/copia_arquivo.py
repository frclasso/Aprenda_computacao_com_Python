#!/usr/bin/env python3


def copiaArquivo(velhoArquivo, novoArquivo):
    f1 = open(velhoArquivo, 'r')
    f2 = open(novoArquivo, 'w')
    while 1:
        texto = f1.read(50)
        if texto == "":
            break
        f2.write(texto)
    f1.close()
    f2.close()
    return

