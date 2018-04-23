#!/usr/bin/env python3


class Horario:

    def imprimeHorario(horas, minutos, segundos):
        # self.horas = horas
        # self.minutos = minutos
        # self.segundos = segundos
        print(f'{horas}h :{minutos}m :{segundos}s')

    def somaHorario(h1,h2):
        soma = Horario()
        soma.horas = h1.horas + h2.horas
        soma.minutos = h1.minutos + h2.minutos
        soma.segundos = h1.segundos + h2.segundos

        if soma.segundos >= 60:
            soma.segundos = soma.segundos - 60
            soma.minutos = soma.minutos + 1

        if soma.minutos >= 60:
            soma.minutos = soma.minutos - 60
            soma.horas = soma.horas + 1

        return soma

    def incrementar(self, horario, segundos):
        horario.segundos = horario.segundos + segundos

        while horario.segundos >=60:
            horario.segundos = horario.segundos - 60
            horario.minutos = horario.minutos + 1

        while horario.minutos >= 60:
            horario.minutos = horario.minutos - 60
            horario.horas = horario.horas + 1


class Time:

    def converteParaSegundos(self, t):
        minutos = t.horas * 60 + t.minutos
        segundos = minutos * 60 + t.segundos
        return segundos

    def criaHorario(self, segundos):
        horario = Time()
        horario.horas = segundos/3600
        segundos = segundos - horario.horas * 3600
        horario.minutos = segundos/60
        segundos = segundos - horario.minutos * 3600
        horario.segundos = segundos
        return horario

    def somaHorario(self, t1, t2):
        segundos = Time.converteParaSegundos(t1) + Time.converteParaSegundos(t2)
        return Time.criaHorario(segundos)


class main:

    # Horario.imprimeHorario(11, 59, 30)

    horarioAtual = Horario()
    horarioAtual.horas = 9
    horarioAtual.minutos = 14
    horarioAtual.segundos = 30
    print('Horario atual')
    Horario.imprimeHorario(horarioAtual.horas, horarioAtual.minutos, horarioAtual.segundos)

    horarioDoPao = Horario()
    horarioDoPao.horas = 3
    horarioDoPao.minutos = 35
    horarioDoPao.segundos = 0
    print('Horario do Pao')
    Horario.imprimeHorario(horarioDoPao.horas, horarioDoPao.minutos, horarioDoPao.segundos)

    #horarioDeTermino = Horario.somaHorario(horarioAtual, horarioDoPao)
    #Horario.imprimeHorario(horarioDeTermino)


if __name__ == '__main__':main()
