'''Crie um programa onde o usuário possa digitar sete valores e cadastre-os em uma unica lista
que mantenha separados os valores pares e impares. No final mostre os valores pares e ímpares em ordem crescente.'''

print('')
dados = [[], []]
for c in range(1, 8):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        dados[0].append(num)
    else:
        dados[1].append(num)
dados[0].sort()
dados[1].sort()
print('-' * 60)
print('A lista de números pares esta vazia.'if len(dados[0]) == 0 else f'A lista de pares é {dados[0]}.')
print('A lista de números impares esta vazia.'if len(dados[1]) == 0 else f'A lista de impares é {dados[1]}.')

#Desafio concluído