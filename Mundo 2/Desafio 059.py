'''Crie um programa que leia dois valores e mostre um menu na tela:[1] somar; [2] multiplicar; [3] maior; [4] novos números; [5] sair do programa
seu programa deverá realizar a operação solicitada em cada caso'''


cores = {'verde' : '\033[1;32m',
         'limpa' : '\033[m',
         'amarelo' : '\033[1;33m'}


print(''
      '\n{:=^70}'
      '\n'.format(' Operações com 2 números Inteiros '))

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

menu = str('''{2}
{0}
{1}MENU

[ 1 ] SOMAR
[ 2 ] MULTILICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR
{0}{3}
'''.format('=' * 40, ' ' * 7,cores['amarelo'],cores['limpa']))

print(menu)

opção = int(input('Informe a opção desejada: '))
print('')

while opção > -1:
    if opção == 1:
        soma = n1 + n2
        print('{}'
              '\n{}O resultado de {} + {} é igual {}{}'.format('*' * 40, cores['verde'], n1, n2, soma, cores['limpa']))
        print('*' * 40,
              '\n{}.'.format(menu))
        opção = int(input('Informe uma nova opção: '))
        print('')
    elif opção == 2:
        multiplicação = n1 * n2
        print('{}'
              '\n{}O resultado de {} x {} é igual a  {}{}'.format('*' * 40, cores['verde'],n1, n2, multiplicação, cores['limpa']))
        print('*' * 40,
              '\n{}'.format(menu))
        opção = int(input('Informe uma nova opção: '))
        print('')
    elif opção == 3:
        maior = max(n1, n2)
        print('{}'
              '\n{}O maior valor digitado entre {} e {} foi {}{}'.format('*' * 40, cores['verde'],n1, n2, maior, cores['limpa']))
        print('*' * 40,
              '\n{}'.format(menu))
        opção = int(input('Informe uma nova opção: '))
        print('')
    elif opção == 4:
        n1 = int(input('{}'
                       '\nInforme o primeiro novo número: '.format('*' * 40)))
        n2 = int(input('Infrome o segundo novo número: '))
        print('*' * 40,
              '\n{}'.format(menu))
        opção = int(input('Informe a nova opção: '))
        print('')
    elif opção == 5:
        print('{}'
              '\n'
              '\n{: ^70}'.format('=' * 70, 'Obrigado po usar a Calculadora da ACSistemas de Gestão de Dados'))
        exit()
    elif opção not in [1, 2, 3, 4, 5]:
            opção = int(input('{}'
                              '\nInforme uma opção válida: '.format('*' * 40)))

# Desafio Concluído
