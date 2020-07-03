# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA no nome

#lendo o nome digitado excluindo os espaços digitados antes e depois do nome e deixando todos os caracteres em minusculo
n = str(input('Digite um nome para ser análisado: ')).lower()

#mostrando na tela se o nome digitado contém a palavra silva utilizando o operador "IN"
print('O nome digitado contém a palavra "Silva" {} .\nTrue = Sim, False = Não'.format('silva' in n))

#Desafio concluído