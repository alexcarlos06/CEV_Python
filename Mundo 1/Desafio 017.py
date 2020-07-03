#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

#Importando dentro da bibliotéca math o método hypot responsavel por calcular a hipotenusa sem uso do teorema de pitágoras
from math import hypot

# Lendo os valores dos catetos
c1 = float(input('Informe o cateto oposto: '))
c2 = float(input('Informe o cateto adjacente: '))

# Exibindo na tela o valor obitido da hipotenusa, com o auxilio do método "format" é possivel obter o resultado sem a necessidade de uma nova variável.
print('A medida da Hipotenusa é "{:.2f}"'.format(hypot(c1,c2)))

# Desafio concluído