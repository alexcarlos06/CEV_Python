#Crie um programa que faça o computador jogar jokenpô com você.


# Importando os métodos choice e sleep
from random import  choice
from time import sleep

# Paleta de cores
cores = {'azul'     : '\033[1;34m',
         'amarelo'  : '\033[1;33m',
         'vermelho' : '\033[1;31m',
         'verde'    : '\033[1;32m',
         'negativo' : '\033[7;30m',
         'azulbebe' : '\033[1;36m',
         'roxo'     : '\033[1;35m',
         'limpa'    : '\033[1;m'}

# Mensagem inicial do programa:
print(''
      '\n{}          JoKenPô         {}'
      '\n'.format(cores['negativo'], cores['limpa']))
print('{}{}{}'.format(cores['azul'], '*' * 26, cores['limpa']))

# Tabela com as opções para o usuário
print('Tabela de Opções:'
      '\n')
print('Papel    ==> {0}[ 1 ]{1}'
      '\nTesoura  ==> {0}[ 2 ]{1}'
      '\nPedra    ==> {0}[ 3 ]{1}'.format(cores['vermelho'],cores['limpa']))
print('{}{}{}'.format(cores['azul'], '*' * 26 , cores['limpa']))
print('')

# Colhendo a jogada do jogador.
njog = int(input('Informe sua jogada: '))
print('')

# Definindo a jogada do computador
jc = ['PAPEL', 'TESOURA', 'PEDRA']
jcomp = choice(jc)

# Caso o jogador escolha uma opção inválida o jogo sera encerrado.
if njog not in [1, 2, 3]:
    print('{}Use alguma das opções destacadas em vermelho para poder jogar.!{}'.format(cores['amarelo'], cores['limpa']))
    exit()

# Definindo as variáveis para ajudar na estrutura de decisão
if   jcomp == 'PAPEL':
    ncomp = 1
elif jcomp == 'TESOURA':
    ncomp = 2
elif jcomp == 'PEDRA':
    ncomp = 3

if   njog == 1:
    jjog = 'PAPEL'
elif njog == 2:
    jjog = 'TESOURA'
elif njog == 3:
    jjog ='PEDRA'

# Tempo para simular a dinâmica do jogo

print('{}Jó{}'
      '\n'.format(cores['azulbebe'], '.' * 20))
sleep(1.5)
print('Ken{}'
      '\n'.format('.' * 19))
sleep(1.5)
print('Pô{}{}'
      '\n'.format('.' * 20, cores['limpa']))

# Definindo a estrutura condicional para determinar quem ganha o jogo.
if jcomp == jjog:
    print('O Computador escolheu {0}{1}{3}'
          '\nVocê escolheu {0}{2}{3}'
          '\n'
          '\n{4}O jogo empatou.!{3}'.format(cores['roxo'], jcomp, jjog, cores['limpa'], cores['azul']))
elif ncomp == 1 and njog == 2:
    print('O Computador escolheu {0}{3}{2}'
          '\nVocê escolheu {0}{4}{2}'
          '\n'
          '\n{1}Você Venceu.!{2} '.format(cores['roxo'], cores['verde'], cores['limpa'],jcomp ,jjog))

elif ncomp == 1 and njog == 3:
    print('O Computador escolheu {0}{3}{2}'
          '\nVocê escolheu {0}{4}{2}'
          '\n'
          '\n{1}O Computador Venceu.!{2} '.format(cores['roxo'], cores['vermelho'], cores['limpa'],jcomp, jjog))

elif ncomp == 2 and njog == 1:
    print('O Computador escolheu {0}{3}{2}'
          '\nVocê escolheu {0}{4}{2}'
          '\n '
          '\n{1}O Computador Venceu.!{2}'.format(cores['roxo'], cores['vermelho'], cores['limpa'], jcomp, jjog))

elif ncomp == 2 and njog == 3:
    print('O Computador escolheu {0}{3}{2}'
          '\nVocê escolheu {0}{4}{2}'
          '\n'
          '\n{1}Você Venceu.!{2}'.format(cores['roxo'] ,cores['verde'] ,cores['limpa'] ,jcomp, jjog))

elif ncomp == 3 and njog == 1:
    print('O computador escolheu {0}{3}{2}'
          '\nVocê escolheu {0}{4}{2}'
          '\n'
          '\n{1}Você Venceu.!{2}'.format(cores['roxo'], cores['verde'], cores['limpa'], jcomp, jjog))

elif ncomp == 3 and njog == 2:
    print('O Computador escolheu {0}{3}{2}'
          '\nVocê escolheu {0}{4}{2}'
          '\n'
          '\n{1}O Computador Venceu.!{2}'.format(cores['roxo'], cores['vermelho'], cores['limpa'], jcomp, jjog))

    # Desafio Concluído
