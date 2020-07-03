#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e 0,15 reais por km rodado

#Fazendo a leitura dos dados
km = int(input(' Quantos KM foram percorridos? '))
d = int(input(' Quantos dias o carro foi alugado? '))

# Definindo os valores de KM rodado e dias alugados
dxrs = float(60.00)
kmxrs = float(0.15)

# Mostrando na tela o valor devido, com o auxilido do método .format não é mecessário criar uma nova variável
print(' O valor devido é {} reais'.format(km*kmxrs+d*dxrs))