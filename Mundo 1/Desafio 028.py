#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador.
#O programa devera escrever na tela se o usuário venceu ou perdeu.

#Importando as bibliotécas necessárias
#método randint dentro da bibliotéca rando para sortear um número aleatório inteiro entre 0 e 5
from random import randint

#método sleep dentro da bibliotéa time para calcular um tempo antes executar uma instrução de comando.
from time import sleep

#imprimindo uma mensagem de boas vindas:
print('Olá, Vou pensar em um número inteiro entre 0 e 5 sera que você consegue adivinhar?')
print('-----x-----' * 10 )

# Definindo o número sorteado pelo computador
comp = randint(0,5)

#Colhendo o palpite do usuário
palpite = int(input('Digite seu palpite: '))
print('Pensando.......................')
sleep(2)
print('Só mais um segundo.............')
sleep(1)
if comp == palpite:
    print("Parabéns, você acertou o número que eu pensei..!")
else:print('Você errou, o número que eu pensei foi o {} e o número que vc escolheu foi {}.\nTente novamente, boa sorte.'.format(comp,palpite))

#Desafio concluido