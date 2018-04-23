#!/usr/bin/env python3

salarios = {'maria':6.23, 'joao':5.42, 'josue':4.25}


def realtorio(salarios):
    estudantes = sorted(salarios.keys())
    estudantes.sort()
    for estudante in estudantes:
        print('%-20s %12.02f'% (estudante, salarios[estudante]))
        #print(f'{estudante} {salarios[estudante]}')


realtorio(salarios)