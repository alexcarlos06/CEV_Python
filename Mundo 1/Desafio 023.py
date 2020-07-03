# Faça um programa que leia um numero de 0 a 9999 e mostre cada um dos digitos
# EX digite um número 1834, unidade 4, dezena 3, centena 8 e milhar 1

from math import trunc
# Lendo o número
n = int(input('Informe um número de até 4 digitos: '))
print('Análisando o número digitado ....................')

# Através do recusso da divisão inteira "//" e do resto da divisão "%" obtemos o valor desejado
m = n // 1000 % 10
c = n // 100 % 10
d = n // 10 % 10
u = n // 1 % 10

#Mostrando na tela os valores obtidos
print('Unidade {}\nDezena {}\nCentena {}\nMilhar {} '.format(u, d, c, m))

#Desafio concluído