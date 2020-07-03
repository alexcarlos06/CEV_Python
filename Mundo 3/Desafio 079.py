print('''\nCrie um programa onde o usuário possa digitar vários valores numéricos e cadastre - os em uma lista.
Caso o número já exista dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.''')

print('')
lista = []
while True:
    n = int(input('\nDigite um valor inteiro a ser cadastrado: '))
    if n not in lista:
        lista.append(n)
        print(f'Valor inserido com sucesso {"."*20}')
    else:
        print(f'Valor já digitado na {lista.index(n)+1}º posição da lista.')
        print('Apenas são aceitos valores exclusivos.')
    r = str(input('Deseja continuar [S / N]: ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Digite "S" para continuar ou "N" para terminar: ')).upper().strip()[0]
    if r == 'N':
        break
lista.sort()
print(f'\nA lista formada em ordem crescente foi: {lista}')

# Desafio Concluído.