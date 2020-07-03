'''Crie um progrma que vai gerar cinco números aleatórios e coloque em uma tupla.
Depois disso, mostre a listagem de núumeros gerados e também indique o menor e o maior valor que estão dentro da tupla.'''

from random import randint

n1 = randint(0, 9)
n2 = randint(0, 9)
n3 = randint(0, 9)
n4 = randint(0, 9)
n5 = randint(0, 9)

n = (n1, n2, n3, n4, n5)

print('\nOs valores que foram sorteados e colocado dentro da tupla foram: ',end='')
for c in n:
    print(c, end=' ')

print(f'\n\nO maior valor sorteado foi {max(n)}\nO menor valor sorteado foi {min(n)}')
