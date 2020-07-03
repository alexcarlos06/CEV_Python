print('''\nCrie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista.
já na posição correta de inserção ( sem usar o sort()). No final, mostre a lista ordenada na tela.''')
print('')

lista = []
for c in range(0, 5):
    n = int(input('Informe um valor inteiro: '))
    if c == 0:
        lista.append(n)
        print(f'O número {n} foi inserido na {lista.index(n)+1}º posição.')
        print(f'{"-" * 50}')
    else:
        if n < min(lista):
            lista.insert(0, n)
            print(f'O número {n} foi inserido na 1º posição.')
            print(f'{"-" * 50}')
        elif n > max(lista):
            lista.append(n)
            print(f'O número {n} foi inserido na {len(lista)}º posição.')
            print(f'{"-" * 50}')
        else:
            for var in range(0, len(lista)):
                if n <= lista[var]:
                    lista.insert(var, n)
                    print(f'O número {n} foi inserido na {lista.index(n)+1}º posição.')
                    print(f'{"-" * 50}')
                    break

print(f'\nA lista exibida de forma crescente é {lista}')

#Desafio Concluído









