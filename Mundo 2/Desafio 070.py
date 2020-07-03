'''Crie um programa que leia o nome e o peço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
a) Qual é o total gasto na compra. b) Quantos produtos custam mais de R$ 1000. c) Qual é o nome do produto mais barato. '''

print('\n\033[1;32m{:~^100}\033[m'.format(' \033[1;4;33mRegistrador de Compras\033[1;32m '))

total = valor = acima = menor = contador = 0
produto = barato = ''
while True:
    print('\n{}'.format('~' * 84))
    produto = str(input('\nInforme o nome do produto: ')).strip()
    valor = float(input('Informe o preço do produto: '))
    print('')
    print('~' * 84)
    valida = str(input('Deseja continuar [S / N]: ')).upper().strip()
    total += valor
    contador += 1
    if valor > 1000:
        acima += 1

    if contador <= 1:
        menor = valor
        barato = produto
    elif menor > valor:
        menor = valor
        barato = produto

    while valida not in 'SN':
        valida = str(input('Deseja continuar "S" para SIM ou "N" NÃO: ')).upper().strip()
    if valida == 'N':
            print('~' * 84)
            print('')
            break

print('\033[1;32m{:=^97}\033[1m\n'.format(' \033[1;4mResumo das compras \033[1;32m'))
print(f'O total das compras foi R${total: .2f} .')

if acima == 0:
    print('Você não comprou nenhum produto acima de R$1000,00 .')
elif acima == 1:
    print('Você comprou um produto acima de R$1000,00 .')
else:
    print(f'Você comprou {acima} produtos com valor acima de R$ 1000,00 .')

print(f'O produto mais barato comprado foi {barato} que custou R${menor: .2f} .')
print('\n\033[1;32m{:~^100}'.format('\033[1;4;33m Obrigado por utilizar o Gerenciador de Compras ACSistemas\033[1;32m '))

# Desafio Concluído