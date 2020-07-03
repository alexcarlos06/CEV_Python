#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior, O segundo valor é menor , Não existe valor maior, os dois são iguais.

# Fazendo a leitura de dois números
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
print('')
# Montando a estrutura de condição
if n1 == n2:
    print('Não existe valor maior, pois os dois são iguais.')
elif n1 > n2:
    print('O primeiro valor o maior. ')
else:
    print('O segundo valor é o maior. ')

#Desafio Concluído