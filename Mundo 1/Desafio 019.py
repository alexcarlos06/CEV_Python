#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele lendo o nome delas e escrevendo o nome escolhido.

# Importando o método choice dentro da biblioteca random para mostrar apenas um dos valores dentro de uma lista
from random import choice

# Lendo os nomes para compor a lista.
n1 = input('Informe o nome do primeiro aluno: ')
n2 = input('Informe o nome do segundo aluno: ')
n3 = input('Informe o nome do terceiro aluno: ')
n4 = input('informe o nome do quarto aluno: ')

#Montando uma variável com todos os nomes informados
lista = [n1, n2, n3, n4]

# Informar na tela o nomes escolhido dentro da lista com o metódo choice
# Neste caso nao foi preciso criar uma nova variável, com o método ".format informamos a variavel necessaria para mostrar o print com o nome escolhido
print('O aluno escolhido foi: {} '.format(choice(lista)))

# Desafio concluído