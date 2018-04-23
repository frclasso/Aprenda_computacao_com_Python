#!/usr/bin/env python3

'''Uma vez que os dicionários são mutáveis, voce precisa saber sobre Aliasing.
Sempre que duas variáveis referenciarem o mesmo objeto, quando uma é alterada, afeta a outra.

Se você quer modificar um dicionário e continuar com uma copia original,
utilize o método copy. '''

oppsites = {'up':'down', 'right':'wrong', 'true':'false'}
alias = oppsites
copy = oppsites.copy()

print(alias)
print(copy)

alias['right'] = 'left' # alias e opposites se referem ao mesmo objeto;
print(oppsites['right'])

copy['right'] = 'privilege' # modificamos copy, opposites eh modificado
print(oppsites['right'])