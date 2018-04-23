#1/usr/bin/env python3


def executar_escolha(escolha):
    if escolha == 'A':
        funcaoA()
    elif escolha == 'B':
        funcaoB()
    elif escolha == 'C':
        funcaoC()
    else:print('Escolha invalida.')


def funcaoA():
    print('A, foi a funcao escolhida')


def funcaoB():
    print('B, foi a funcao escolhida')


def funcaoC():
    print('C, foi a funcao escolhida')


executar_escolha('B')