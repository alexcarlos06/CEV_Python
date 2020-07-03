#Escreva um programa que converta uma temperatura digitada em º C e converta para ºF

# Fazendo a leitura da temperatura
c = int(input('Informe a temperatura em ºC: '))

# Mostrando na tela o valor gerado com a informação de º C digitada de acordo com a formula de conversão usada para converter ºC em ºF
print('{}ºC correspondem a {}ºF '.format(c,(c*9)/5+32))

# Desafio concluído