#Faça um programa que leia a largura e a altura de uma parede em metros e cacule sua área e a quantidade de tinta necessária para pinta-la. sabendo que cada litro de tinta pinta uma área de 2m²

# Lendo o rendimento da embalagem de tinta a ser comprada
rend = int(input('Informe o rendimento da embalagem de tinta: '))

# Lendo o valor do preço de uma embalagem de tinta
rs = float(input('Informe quanto custa a tinta desejada '))

# Lendo as medidas da parede
h = int(input('Informe a altura da parede '))
b = int(input('informe a largura da parede '))

# Calculando a área da parede
a = b*h

# Definindo variáveis para mostrar a necessidade e o preço gasto para pitar a parede
neces = a/rend
vl = neces*rs

# Mostrando na tela os valores , desta vez para maior entendimento do código foram criadas as variáveis fora do método .format, desta forma fica mais facíl o entendimento do código.
print('O tamanho da parede é {} m²\nPara pintar toda a parede serão necessários {:.2f} latas de tinta e o valor pago será {} reais. '.format(a,neces, vl))

#Desafio concluído