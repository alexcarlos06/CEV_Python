'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci. Ex: 0 ==> 1 ==> 1 ==> 2 ==> 3 ==> 5 ==> 8
SOLUÇÃO PÓS RESOLUÇÃO DO VIDEO DO EXERCICIO!!!!!!'''

print('{:=^100}'.format(' Gerador de sequência de Fibonacci '))
print('')

n = int(input('Informe quantos termos deseja exibir: '))

# Na sequência de fibonacci o primeiro e o segundo termo são fixos, ou seja, independente da do tamanho da sequência sempre haverá estes dois termos.
# O proxímo termo será a soma dos dois termos anteriores.

t1 = 0
t2 = 1
c = 3

print('{} ==> {}'.format(t1, t2), end='')

while c <= n:
    t3 = t1 + t2
    print(' ==> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1

print(' Fim.!', end='')

# Desafio Concluído
