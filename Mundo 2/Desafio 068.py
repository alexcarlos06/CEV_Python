'''Faça um programa que jogue Par ou Ímpar com o computador. O jogo será interrompido quando o jogador PERDER, Mostrando o total de votórias consecutivas que ele conquistou no final do jogo'''

from random import randint
from time import sleep
print('\n\033[1;36m{:=^100}\033[m\n'.format('\033[1;4;33m Vamos jogar Par ou Ímpar? \033[1;36m'))



cont = 0

while True:
    c = randint(0, 10)
    n = int(input('Qual sua jogada? '))
    e = str(input('Par ou Ímpar [P / I]: ')).upper().strip()[0]
    while e != 'I' and e != 'P':
        e = str(input('Par ou Ímpar [P / I]: ')).upper().strip()[0]

    c = randint(0, 10)
    soma = c + n
    resultado = soma % 2

    if resultado == 0:
        ganhador = 'P'
        pi = 'PAR'
    else:
        ganhador = 'I'
        pi = 'ÍMPAR'


    print('\n\033[1;31mPar..........')
    sleep(1)
    print('\n\033[1;33mOu..........')
    sleep(1)
    print('\n\033[1;32mÍMPAR..........\033[1m')
    print('')

    print(f'\nO computador Jogou \033[1;34m{c}\033[1m. Você Jogou \033[1;34m{n}\033[1m ==> \033[1;34m{c}\033[1m + \033[1;34m{n}\033[1m = \033[1;34m{soma}\033[m = \033[1;34m{pi}\033[m ', end='')
    print('\033[1;32m O JOGADOR Venceu.!\033[m' if ganhador == e else '\033[1;31m O COMPUTADOR Venceu.!\033[m')

    if ganhador == e:
        cont += 1
        e = ''
    else:
        break

print(f'\n\033[1;35mSua pontuação foi: {cont}')
print('\n\033[1;32m{:~^100}\033[m'.format('\033[1;31m Game Over \033[1;32m'))
print('\n\033[1;36m{:=^102}'.format('\033[1;4;33m Obrigado por utilizar o Software da ACSistemas \033[1;36m'))


# Desafio Concluído