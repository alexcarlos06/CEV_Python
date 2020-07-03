'''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários para vencer. '''

from random import randint
''' Paleta de cores'''
cores = {'azul'      : '\033[34m',
         'amarelo'   : '\033[33m',
         'vermelho'  : '\033[31m',
         'limpa'     : '\033[m',
         'roxo'      : '\033[35m',
         'verde'     : '\033[32m',
         'nverde'    : '\033[1;32m',
         'namarelo'  : '\033[1;33m',
         'nvermelho' : '\033[1;31m',
         'negativo'  : '\033[7;30m'}

print('{}{:=^50}{}'.format(cores['amarelo'],' Jogo da Adivinhação ', cores['limpa']))
print('''{}
Vou pensar em um número inteiro entre 1 e 10,
Será que vc consegue adivinhar????
                  
                  Boa sorte!!!!!{}
{}{}{}'''.format(cores['roxo'], cores['limpa'], cores['amarelo'], '*' * 50,cores['limpa']))

ncomp = randint(1, 10)
palpite = 0
contagem = 0

while palpite != ncomp:
    if contagem == 0:
        palpite = int(input(''
                            '\nQual seu palpite?  '))
        contagem += 1
        print('')
    else:
        palpite = int(input('{}Errou...'
                            '\n'
                            '\n{}Qual seu novo palpite? '.format(cores['vermelho'], cores['limpa'])))
        contagem += 1
        print('')
if contagem == 1:
    print('{0}Parabéns!!!!'
          '\n{1}Você acerou de primeira. '
          '\n{0}A SORTE ESTA AO SEU LADO....{2}'.format(cores['nverde'], cores['verde'], cores['limpa']))
elif contagem <=3:
        print('{}Você acertou!!!'
            '\n{}Foram necessárias {}{}{} tentátias.'
            '\n{}Seu nível de sorte está em {}%'.format( cores['verde'], cores['limpa'],cores['verde'], contagem, cores['limpa'], cores['nverde'], (10 - contagem) * 10))
elif contagem <=5:
    print('{}Você acertou!!!'
          '\n{}Foram necessárias {}{}{} tentativas.'
          '\n{}ATENÇÃO seu nivel de sorte está em {}%'.format(cores['verde'], cores['limpa'], cores['verde'], contagem, cores['limpa'], cores['namarelo'], (10 - contagem) * 10))
elif contagem <=9:
    print('{0}Você acertou!!!'
          '\n{1}Foram necessárias {0}{2}{1} tentativas.'
          '\n{3}CUIDADO seu nível de sorte está em {4}%'.format(cores['verde'], cores['limpa'], contagem, cores['namarelo'], (10 - contagem) * 10))
else:
    print('{0}Eram apenas 10 possibilidades e você acertou em {2}        {1}'
          '\n{0}        Você entendeu o jogo??                            {1}'
          '\n{0}          Tente novamente....                             {1}'.format(cores['negativo'], cores['limpa'],contagem))

    # Desafio Concluído.