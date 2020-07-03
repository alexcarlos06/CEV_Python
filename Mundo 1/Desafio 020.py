#O mesmo professor professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#Primeiro vamos importar apenas o metodo usado da bibliotéca random

from random import sample

# Ler os quatro nomes  que serão sorteados.
n1 = str(input('Informe o nome do primeiro aluno: '))
n2 = str(input('Informe o nome do segundo aluno: '))
n3 = str(input('informe o nome do terceiro aluno: '))
n4 = str(input('informe o nome do quarto aluno: '))

#colocando o nome dentro de uma lista para depois sortearmos a sequência
seq = [n1, n2, n3, n4]

#o metodo simple mostra valores aleatórios dentro de uma lista primeiro informamos o nome da lista e em seqguida informamos a quantidade de nomes.

n = sample(seq, 4)

#informar na tela a lista com os valores armazenados aleatóriamente
print('A seguência será: {} '.format(n))

#Desafio concluído