# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles

# Importando o método sleep dentro da bibliotéca time
from time import  sleep

# Paleta de cores
cores = {'azul'     : '\033[1;34m',
         'limpa'    : '\033[1;m',
         'amarelo'  : '\033[1;33m',
         'negativo' : '\033[7;340m'}

# Mensagem ínicial do programa.
print('{}{:=^150}{}'.format( cores['azul'],' Contador de final de ano V 2.0 ', cores['limpa'] ))
print(cores['amarelo'])
input('{: ^150}'.format('Pressione a tecla enter para íniciar a contagem regressiva!!!'))


for c in range(10, 0, -1):
   print('')
   print('{: ^150}'.format(c))
   sleep(1)
print('{}{}'.format(cores['amarelo'],'''   #######   ######   ##       ##   ######          ######   ###      ##   ######          ###      ##   ######   ##           ##   ######          ##
   ##        ##       ##                #           ##  ##   ## #     ##   ######          ## #     ##   ######    ##         ##    ######          ##
   ##        ##       ##       ##      #            ##  ##   ##  #    ##   ##  ##          ##  #    ##   ##  ##     ##       ##     ##  ##          ##
   #####     ####     ##       ##     #             ######   ##   #   ##   ##  ##          ##   #   ##   ##  ##      ##     ##      ##  ##          ##
   ##        ##       ##       ##    #              ##  ##   ##    #  ##   ##  ##          ##    #  ##   ##  ##       ##   ##       ##  ##          ##
   ##        ##       ##       ##   #               ##  ##   ##     # ##   ######          ##     # ##   ######        ## ##        ######          
   ##        ######   ######   ##   ######          ##  ##   ##      ###   ######          ##      ###   ######          ##         ######          ##




'''))

# Desafio Concluído.

