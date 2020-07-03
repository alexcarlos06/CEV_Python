# Faça um programa que leia o nome completo de uma pessoa, monstrando em seguida o primeiro e o ultimo nome separadamente
# EX: Ana Maria de Souza, primeiro nome Ana, Último nome Souza

# Lendo o nome completo, retirando os espaços digitados no inicio e no final e fazendo o split do nome
n = str(input('Informe seu nome completo: ')).split()
print('Análisando o nome.................. ')

# Para mostrar o primeiro nome usamos a primeira posição do split do nome digitados
# Para  o último nome contamos a quantidade de splits do nome digitado e subtraimos uma posição para chegar ao número da ultima posição do split,
# Colocamos o comando .title para mostrar a primeira letra do nome em letra maiuscula.
print('O primeiro nome é {} e o último nome é {}'.format(n[0].title(),n[len(n)-1].title()))


#Desafio concluído
