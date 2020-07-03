'''Faça um programa que leia o nome e o peso de varias pessoas guardando dentro de uma lista. No final mostre
a)Quantas pessoas foram cadastradas. B)Uma listagem com as pessoas mais pesadas.
C)Uma listagem com as pessoas mais leves'''

lpesos = list()
pessoas = list()
dados = list()
while True:
    dados.clear()
    nome = str(input('\nNome: ')).strip()
    peso = float(input('Peso (Kg) : '))
    dados.append(nome)
    dados.append(peso)
    lpesos.append(peso)
    pessoas.append(dados[:])
    valida = str(input('Deseja continuar? [S / N] ')).strip().upper()
    while valida not in 'SN':
        valida = str(input('Digite "S" para SIM ou "N" para NÃO:  ')).strip().upper()
    if valida == 'N':
        break
print('--' * 30)
print(f'\nForam cadastrados {len(pessoas)} pessoas.\n')
print(f'O maior peso foi de {max(lpesos)} Kg. Peso de ', end='')
for c in pessoas:
    if c[1] == max(lpesos):
        print(f'{c[0]}; ', end='')
print('')
print(f'O menor peso foi de {min(lpesos)} Kg. Peso de ', end='')
for c in pessoas:
    if c[1] == min(lpesos):
        print(f'{c[0]}; ', end='')

#Desafio concluído

