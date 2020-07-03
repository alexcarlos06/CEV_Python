#Escreva um programa que leia a velocidade de um carro. Se ela ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$ 7,00 por cada Km acima do limite.

#Importando o método sleep dentro da bibliotéca time para dar a impressão de verificação no sistema.
from    time import sleep

#Mensagem de boas vindas e definindo o limite maximo.
limite = 80
print('Olá condutor vamos ver se você sofreu uma multa de trânsito no Radar! ')
print('=====x=====' * 10)

#Fazendo a leitura da velocidade o valor a ser aplicado na multa e a quantidade de Km/h ultrapassados
vel = int(input('Qual era a velocidade em Km/h que você passou pelo Radar? '))

ultr = vel - limite
valor = (vel - limite)* 7
print('Verificando...................')
sleep(2)
if vel > limite:
    print('Você ultrapassou em {} Km/h, o valor da multa aplicada será de R${: .2f} '.format(ultr,valor))
else:
    print('Você passou dentro da velocidade permitida .!')

#Desafio Concluído
