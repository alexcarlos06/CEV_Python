#Crie um programa que leia um numero que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira EX: digite o número 6.127, o número 6.127 tem a sua porção inteira 6

#Importando a função "trunc" dentro da bibliotéca math, da mesma maneira que o EXCEL faz o método "TRUNCAR" mostrar apenas o valor inteiro.
from math import trunc

# Lendo o valor desejado
n = float(input('Informe um número: '))

# Mostrando na tela a parte inteira do valor digitado, com o auxilio do método .format nao é preciso criar uma nova variável pasta inserir o método importado
print(' A parte inteira do número "{}" é "{}" '.format(n, trunc(n)))