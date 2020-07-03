#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#À vista em dinheiro ou cheque: 10% de desconto ; À vista no cartão: 5% de desconto ; Em até 2x no cartão: preço normal ; 3x ou mais no cartão: 20% de juros.

# Paleta de cores
cores = {'limpa'    : '\033[1;m',
         'azul'     : '\033[1;34m',
         'amarelo'  : '\033[1;33m',
         'negativo' : '\033[7;30m',
         'vermelho' : '\033[1;31m',
         'cinza'    : '\033[1;37m',
         'azulbebe' : '\033[1;36m',
         'verde'    : '\033[1;32m'}

# Mensagem inicial do programa.
print('\n'
      '{0}{1} ACSousa Sistema de Parcelamentos {1}{2}'
      '\n'.format(cores['cinza'], '*' * 20 , cores['limpa']))

# Informações referente a taxas de créditos e meios de pagamentos.
print('{}{}{}'.format(cores['azulbebe'], '-' * 74, cores['limpa']))
print('{}{}Catálogo de Opções de Parcelamento'.format(cores['amarelo'] ,' ' * 20 ))
print(' ')
print('        Descrição:                                              Opção:'
      '\n'
      '\nÀ vista no Dinheiro ou Cheque ----------------------------------( 1 )'
      '\nÀ vista no Cartão de Credito ou Débito -------------------------( 2 )'
      '\nEm 2 vezes no Cartão de Crédito --------------------------------( 3 )'
      '\nA partir de 3 vezes no Cartão Crédito --------------------------( 4 )'
      '\nPara sair ------------------------------------------------------( 0 )'
      '\n{}'.format(cores['limpa']))
print('{}{}{}'
      '\n'.format(cores['azulbebe'], '-' * 74, cores['limpa'] ))
# Fazendo a leitura dos dados referente as parcelas e valores
p = int(input('Informe a opção de parcelamento desejada: '))



if p not in [0, 1, 2, 3, 4]:
    print('{}Escolha uma opção válida.!{}'.format(cores['vermelho'], cores['limpa']))
    exit()

elif p == 0:
    print('{}Obrigado por usar o nosso sistema de parcelamento.{}'.format(cores['verde'], cores['limpa']))
    exit()
else:
    valor = float(input('Informe o valor do Produto / Serviço: '))

# Montando as variáveis para auxiliar a estrutura de condição
op1 = (90 / 100)*valor      # Preço do produto com 10% de desconto
op2 = (95 / 100)*valor      # Preço do produto com 5% de desconto
op3 = valor                 # Preço do produto sem desconto
op4 = (120 / 100)*valor     #Preço do protduto pago com acrescimo de 20%

if p == 1 and valor > 0:
    print('')
    print('{}O Produto / Serviço será pago À vista no valor de R${: .2f}{} '.format(cores['azul'], op1, cores['limpa']))


elif p == 2 and valor > 0:
    print('')
    print('{}O Produto / Serviço será pago À vista no valor de R${: .2f}{}'.format(cores['azul'], op2, cores['limpa']))

elif p == 3 and valor > 0:
    print('')
    print('{}O Produto / Serviço será pago em 2x no valor de R${: .2f} por parcela, totalizando R$ {: .2f}{} '.format(cores['azul'], op3 /2 ,op3, cores['limpa'] ))

elif p == 4 and valor > 0:
    parcelas = int(input('Informe quantas vezes será feito o parcelamento: '))
    if parcelas <=2:
        print('')
        print('{}Para parcelamentos em até 2x deve ser usado as opções 1, 2 ou 3.{}'.format(cores['amarelo'], cores['limpa']))
        print('')
        exit()
    print('')
    print('{}O Produto / Serviço será pago em {}x no valor de R${:.2f} por parcela, totalizando R$ {:.2f}{} '.format(cores['azul'],parcelas , op4 / parcelas, op4, cores['limpa']))
else:
    print('')
    print('{}Digite um valor válido para parcelamento.!{}'.format(cores['amarelo'], cores['limpa']))

print('\n'
      '{}Obrigado por usar o nosso sistema de parcelamento.{}'.format(cores['verde'], cores['limpa']))

# Desafio Concluído