'''Faça um programa que leia um número qualquer e mostre seu fatorial usando a instrução while Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
from time import sleep
print('{}{:=^60}'
      '\n{}'.format("\033[1;33m", ' Calculo de Fatorial ', "\033[1m"))
print('''Número natural é todo número inteiro e positivo.

O fatorial de um número "n" é o produto de todos os números
naturais menor ou igual a "n"

{}{}{}
'''.format('\033[1;33m', '=' * 60, '\033[1m'))

n = int(input('Informe número natural diferente de zero: '))
c = n
f = 1

print('')
print('Calculando {}! = '.format(n), end='')
while c > 0:

    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' =', end='')
    f *= c
    c -= 1

print('\033[1;33m'' {}'.format(f))

# Desafio concluído
