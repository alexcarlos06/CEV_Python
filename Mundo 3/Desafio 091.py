'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.'''

# Importando as bibliotécas necessárias
from random import randint
from time import sleep
from operator import itemgetter

#Mensagem inicial  do jogo de dados
print(f'\n{" Jogo de Dados ":~^40}\n')

#Informando a proxíma ação a ser executada
print('Sorteando valores...')

#Definindo o tempo para proxíma instrução
sleep(1)

#definindo a variável responsável por sortear os valores e colocar dentro do dicionário principal
j = 0

#Declarando o dicionário principal e o dicionário que sera ordenado
dados = {}
rank = dict()

#Loop para colocar os valores dentro do dicionário
while j < 4:
    jog = randint(1, 6)
    j += 1
    dados[f'jogador_{j}'] = jog
    print(f'O {j}º jogador tirou o número {jog} '.center(40))
    sleep(1)

print(f'\n{"~" * 40}\n')

#Comando para ordenar os valores sorteados, estamos usando o comando itemgetter para ordenar o dicionário tendo como referencia os valores sorteados, valores da posição "1"
rank = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('Computando os resultados...\n')
sleep(2)
print('Ranking geral')

#Loop para informar o ranking do maior para o menor
for j, n in enumerate(rank):
    print(f'{j+1}º Lugar {n[0]} com {n[1]} pontos'.center(40))

#Desafio concluído