# Escreva um programa para aprovar o empréstimo bancário para comprar uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ele nao pode exceder 30% do salário ou então o empréstimo será negado.

# Importando o método sleep dentro da bibliotéca time e o método randint dentro da bibliotéca random
from time import sleep
from random import  randint
# Montando a paleta de cores
cores = {'azul' : '\033[1;34m',
         'amarelo' : '\033[1;33m',
         'preto' : '\033[7;30m',
         'vermelho' : '\033[1;31m',
         'verde' : '\033[1;32m',
         'limpa' : '\033[m',
         'negrito' : '\033[1m'}

# Mensagem inicial do Programa
print('{}xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'.format(cores['amarelo']))
print('{}                                             *Aprovador de Emprestimo Imobiliário*'.format(cores['azul']))
print('{}xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx{}{}'
      .format(cores['amarelo'] , cores['limpa'] , cores['negrito']))

# Colhendo os inputs
valor = float(input('Informe qual valor do imóvel a ser financiado: R$ '))
período = float(input('Informe em quantos anos o comprador deseja pagar: '))
salário = float(input('Informe o salário atual do comprador: R$ '))

# Definindo variáveis para facilitar a elaboração das condições e possíveis manutenções nas condições.
percentual = 30 / 100                   # Está variável é reponsável pela porcentagem aceita para emprestimo
limite     = salário*percentual             # O limite é a quantidade maxíma em reais que o usuário pode fazer a parcela respeitando o percentual estabelecido na variável percentual.
parcela    = período * 12                  # O período é a quantiade de anos que usuário deseja pagar o emprestimo.
prestação  = valor / parcela

print('\n{}Sua solicitação está sendo processada em nosso banco de dados.\n\nAguarde alguns segundos................{}'.format(cores['azul'] , cores['negrito']))
sleep(3)


# Montando a condição para informar se o emprestimo sera permitido ou não
if prestação > limite:
    print('{}Você está sem margem para realizar o emprestimo. \nSolicite um valor mais baixo ou aumente o número de parcelas.{}'.format(cores['vermelho'] , cores['negrito']))

else:
    print('{}Parabéns, o seu emprestimo foi aceito,'
          '\nSão {: .0f} parcelas de R${: .2f} .'
          '\nEntre em contato com os nossos corretores e informe o número de acesso "{}"{}'.format(cores['verde'] , parcela , prestação ,randint(10000,99999) , cores['negrito']))

print('\nObrigado por utilizar o nosso sistema de financiamento imobiliário.')

#Desafio Concluído