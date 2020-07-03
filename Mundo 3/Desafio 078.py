print('''\nFaça um programa que leia 5 valores númericos e guarde - os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista\n''')

n = []
pmaior = []
pmenor = []
print(f'{"-" * 50}')
for c in range(0, 5):
    colocar = n.append(int(input(f'Digite um válor inteiro para a posição {c}: ')))
nmaior = max(n)
nmenor = min(n)
for num, p in enumerate(n):
    if p == nmaior:
        pmaior.append(num)
    elif p == nmenor:
        pmenor.append(num)
print(f'\n{"Resultado da análise":~^50}')
print(f'\nVocê digitou os valores: {n}')
if len(pmenor) > 1:
    print(f'O menor valor digitado foi: {nmenor} e está nas posições {pmenor}')
else:
    print(f'O menor valor digitado foi: {nmenor} e está na posição: {pmenor}')
if len(pmaior) > 1:
    print(f'O maior valor digitado foi: {nmaior} e está nas posições: {pmaior}')
else:
    print(f'O maior valor digitado foi: {nmaior} e esta na posição: {pmaior}')

#Desafio Concluído.