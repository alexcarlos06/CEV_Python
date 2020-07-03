# Faça um programa que leia o pesos de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.

# Paleta de cores:
cores = {'amarelo'  : '\033[1;33m',
         'azul'     : '\033[1;34m',
         'vermelho' : '\033[1;31m',
         'cinza'    : '\033[1;37m',
         'limpa'    : '\033[1;m'}


menor = 0
maior = 0
# Mensagem ínicial do programa
print('{}{: ^50}'.format(cores['limpa'], ' Análisador de Pesos '))


print('{}{}'.format(cores['azul'], '*' * 50))

for p in range(1, 6):
    peso = float(input('{}Informe {}{}{}º peso: {} '.format(cores['cinza'], cores['amarelo'], p, cores['cinza'],cores['limpa'])))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso >= maior:
            maior = peso

        elif peso < menor:
            menor = peso
print('{}{}'.format(cores['azul'], '*' * 50))
print(''
      '\n{}O maior peso informado é {}Kg'
      '\n'
      '\n{}O menor peso informado é {}Kg'.format( cores['vermelho'], maior, cores['amarelo'],menor ))

# Desafio Concluido