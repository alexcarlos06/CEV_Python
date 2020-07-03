'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci. Ex: 0 ==> 1 ==> 1 ==> 2 ==> 3 ==> 5 ==> 8 '''

# Paleta de cores
cores = {'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'vermelho': '\033[1;31m',
         'limpa': '\033[1m',
         'verde': '\033[1;32m',
         'roxo': '\033[1;35m',
         'azulm': '\033[1;36m',
         'cinza': '\033[1;37'}

print('{}{:=^100}{}'.format(cores['roxo'], ' Gerador de Sequeência de Fibonacci ', cores['limpa']))
print('\n{}{}{}\n'.format(cores['amarelo'], '*' * 100, cores['limpa']))

n = int(input('Informe quantos termos deseja exibir: '))
print('')

c = 0
fi = 1
ant = 1

if n == 1 :
    print('0 .Fim\n')
elif n == 0:
    print('Você não solicitou nenhum termo.!\n')
    exit()
else:
    while c < n-1:
        if c < 1:
            print('{}'.format(0), end='')
            print(' ==> ', end='')
        if c < 2:
            print('{}'.format(fi), end='')
            print(' ==> ' if c < n - 2 else '. Fim.!', end='')
            c += 1
        elif c < 4:
            fi += ant
            print('{}'.format(fi), end='')
            print(' ==> ' if c < n - 2 else '. Fim.!', end='')
            c += 1
        elif c < 5:
            ant += ant
            fi += ant
            print('{}'.format(fi), end='')
            print(' ==> ' if c < n - 2 else '. Fim.!', end='')
            c += 1
        else:
            ant = fi - ant
            fi += ant
            print('{}'.format(fi), end='')
            print(' ==> ' if c < n - 2 else '. Fim.!', end='')
            c += 1
print('\n\n\033[1;36m{:=^100}\n'.format(' Obrigado por utilizar o Gerador de Sequência de Fibonacci da ACSistemas '))

# Desafio Concluído
