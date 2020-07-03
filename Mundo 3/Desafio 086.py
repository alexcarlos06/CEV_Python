'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valors lidos pelo teclado,
no final, mostre na tela, com a formatação correta'''

print('')
lista = [[], [], []]
linha = coluna = 0
for c in range(0, 9):
    lista[linha].append(int(input(f'Digite um valor para a posição [{linha}, {coluna}] : ')))
    if coluna >= 2:
        coluna = 0
    else:
        coluna += 1
    if 2 <= c < 5:
        linha = 1
    elif 5 <= c < 9:
        linha = 2
print('-_' * 25)
print('')
for c in range(0, 3):
    print(f'[ {lista[c][0]:^5} ]  [ {lista[c][1]:^5} ]  [ {lista[c][2]:^5} ]')

# Desafio Concluído.