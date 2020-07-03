'''Crie um programa que simule o funcionamento de um caixa eletônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''

print('\n{}{:^^100}{}\n'.format('\033[1;4;34m', '\033[1;31m Caixa Eletrônico ACSistemas \033[1;4;34m', '\033[m'))

import os
saque = int(input('Informe o valor do saque: '))
print('')

c = 100
valor = saque
cont = 0

while True:
    if valor >= c:
        while valor >= c:
            valor -= c
            cont += 1
            total = cont * c
        print(f'Serão {cont} notas de R${c:.2f} ==> O total das notas de {c} será R${total: .2f} \n')
    if valor >= 50:
        c = 50
        cont = 0
        while valor >= c:
            valor -= c
            cont += 1
            total = cont * c
        print(f'Serão {cont} notas de R${c:.2f} ==> O total das notas de {c} será R${total: .2f} \n')
    elif valor >= 20:
        c = 20
        cont = 0
        while valor >= c:
            valor -= c
            cont += 1
            total = cont * c
        print(f'Serão {cont} notas de R${c:.2f} ==> O total das notas de {c} será R${total: .2f}\n')
    elif valor >= 10:
        c = 10
        cont = 0
        while valor >= c:
            valor -= c
            cont += 1
            total = cont * c
        print(f'Serão {cont} notas de R${c:.2f} ==> O total das notas de {c} será R${total: .2f}\n')
    elif valor >= 1:
        c = 1
        cont = 0
        while valor >= c:
            valor -= c
            cont += 1
            total = cont * c
        print(f'Serão {cont} notas de R${c:.2f} ==> O total das notas de {c} será R${total: .2f}\n')
    else:
        print('-' * 85)
        print('')
        if saque == 0:
            break
        else:
            saque = int(input('Informe um novo valor do saque ou 0 para sair: '))
            print('')

            c = 100
            valor = saque
            cont = 0
print('\033[1;33m{:~^100}'.format(' \033[1;4;34mObrigado por utilizar o nosso sistema de Caixa eletrônico\033[1;33m '))

# Desafio Concluído