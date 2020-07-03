'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos núumeros foram digitados e qual foi a soma entre elas ( desconsiderando o flag)'''


print('\n\033[1;33m{:=^100}\033[m\n'.format(' \033[1;31mCalculadora de soma ACSistemas\033[1;33m '))
c = 0
soma = 0

while True:
    n = int(input('Informe um número inteiro ou 999 para sair: '))
    if n == 999:
        break
    else:

        c += 1
        soma += n
print('\n\033[1;36mCalculando..........')
print(f'\n\033[1;32mForam digitados \033[1;36m{c}\033[1;32m números.\nA soma entre eles é igual a \033[1;36m{soma}\033[m.')
print('\n\033[1;33m{:=^100}'.format(' \033[1;31mObrigado por utilizar a Calculadora ACSistemas\033[1;33m '))

# Desafio Concluído