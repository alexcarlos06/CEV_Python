#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. ( as formunlas para achar os dados pedidos calculam o valor dos graus em radianos)

# Vamos importar os metódos necessários dentro da bibliotéca math
from math import cos
from math import sin
from math import tan
from math import radians

# Ler o valor do angulo
a = int(input('Digite um ángulo: '))

# calculos de cosseno, seno e tangente ,sao feitos com radianos e nao com graus, (Vide guia do python.org), por tanto precisamos transformar os graus informados em radianos antes de fazer as contas
a1 = radians(a)

# Fazendo os calculos com o valor do grau informado convertido para radianos
c = cos(a1)
s = sin(a1)
t = tan(a1)

# Mostrando na tela o valor informando para o grau, valores obtidos do seno, cosseno e tangente.
print('O valor do seno para o ângulo {0}º é {1:.2f}\nO valor do cosseno para o ángulo {0}º é {2:.2f}\nO valor da tangente para o ángulo {0}º é {3:.2f} '.format(a, s, c, t))

# Desafio concluído