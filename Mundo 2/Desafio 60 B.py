'''Faça um programa que leia um número qualquer e mostre seu fatorial usando a instrução FOR Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''


# Paleta de cores
cores = {'azul': '\033[1;34m',
         'amarelo:': '\033[1;33m',
         'vermelho': '\033[1;31m',
         'limpa': '\033[1m'}


print('''
{}{}{}

Número Natural é todo número inteiro positivo
Incluindo o zero. EX: 0, 1, 2, 3, 4...

O fatorial de um número natural n é representado por "n!", 
é o produto de todos os números positivos menores ou igual a n.

{}{}{}
'''.format(cores['vermelho'], '*' * 65, cores['amarelo:'], cores['vermelho'], '*' * 65, cores['limpa']))
n = int(input('Informe o número Natural diferente de zero: '))

f = 1
print('')
print('Calculando {}{}{}! = '.format(cores['azul'], n, cores['limpa'],), end=' ')
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' = ' if c == 1 else ' x ', end='')
    f *= c

print('{}{}'.format(cores['azul'], f))

# Desafio Concluído