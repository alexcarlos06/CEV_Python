'''Crie um programa que vai ler vários números e colocar em uma lista despois disso mostre:
a) quantos números foram digitados  b) a lista de valores ordenadas em forma decrescente.
c)se o valor 5 foi digitado e se está ou não na lista.'''

lista = []
cont = ''
print('')
while cont !='N':
    lista.append(int(input('Informe um número inteiro: ')))
    cont = str(input('Deseja continuar [S / N]: ')).upper().strip()
    while cont not in "N, S" or cont == '':
        cont = str(input('Deseja continuar?  S para "SIM" ou N para "NÂO": ')).upper().strip()

lista.sort(reverse=True)

print(f'{"=====x"* 20}\n')

if len(lista) == 1:
    print(f'Foi digitado apenas um número.'
          f'\nO número digitado foi {lista} .')
else:
    print(f'Foram digitados {len(lista)} números.'
          f'\nOs números digitados em ordem decrescente são {lista}')
if 5 in lista:
    print('O número "5" faz parte da lista')
else:
    print('O número "5" não faz parte da lista.')

#Desafio Concluído