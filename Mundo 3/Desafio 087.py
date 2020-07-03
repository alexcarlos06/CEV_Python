'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna C) O maior valor da segunda linha.'''

print()
lista = [[], [], []]
par = []
núm = npar = tcoluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        núm = int(input(f'Digite um valor para a posição [ {l}, {c} ]: '))
        lista[l].append(núm)
        if núm % 2 == 0:
            npar += núm
            par.append(núm)
        if c == 2:
            tcoluna += núm
print('-_' * 30)
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}] ', end='')
    print()
print(f'\n\033[1;33m{" Análisando os dados ":=^60}\033[m')

if len(par) == 0:
    print('Não foi digitado nenhum número par.')
elif len(par) == 1:
    print(f'Foi digitado apenas um número par que foi {par} .')
else:
    print(f'Foram digitados {len(par)} números pares e a soma é {npar} .')
print(f'A soma dos valores da 3º Coluna foi {tcoluna} . ')
print(f'O maior valor da 2º Linha foi {max(lista[1])} .')
