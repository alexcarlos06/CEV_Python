#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
#Se ele ainda vai se laistar ao serviço militar.
#Se é a hora de se alistar e se ja passou o tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Importando o método datetime dentro da biblioteca datetime que é reponsável por trazer as informações de ano, mês, dia, hora, minutos e segundos.
from datetime import date

#definindo a paleta de cores.
cores = {'amarelo'  : '\033[1;33m',
         'azul'     : '\033[1;34m',
         'vermelho' : '\033[1;31m',
         'negativo' : '\033[7;30m',
         'limpa'    : '\033[1;m',
         'verde'    : '\033[1;32m',
         'roxo'     : '\033[1;35m'}

# Definindo a variavel para calcular quantos anos o usuário tem

anoatual = date.today().year  # Variável 'date' com o metódo '.year' para extrair apenas o ano da data

# Menságem ínicial do programa
print('{}******************** MINISTÉRIO DA DEFESA, EXÉRCITO BRASILEIRO ********************{}'. format(cores['negativo'], cores['limpa']))

# Campo informativo com as datas de alistamento
print('{}***********************************************************************************{}'.format(cores['azul'], cores['limpa']))
print('{}Jovens que completam 18 anos no ano de {},'
      '\ndevem se alistar até o último dia do mês de Junho. {}'.format(cores['amarelo'], anoatual, cores['limpa']))
print('{}***********************************************************************************{}'.format(cores['azul'], cores['limpa']))

# Fazendo a leitura do sexo
print('Opções de sexo.'
      '\nMasculino ==> [ 1 ]'
      '\nFeminino ==> [ 2 ]')
print('***********************************************************************************')
sexo = int(input('Informe seu sexo: '))

# Montando a estrutura de condição para devinir um sexo válido.
if sexo not in [1, 2]:
    print('Selecione uma opção válida.!')
    exit()
elif sexo == 2:
    print(''
          '\n{}No brasil pessoas do sexo FEMININO não precisam se alistar obrigatóriamente.!{}'.format(cores['roxo'], cores['limpa']))
    exit()
elif sexo == 1:

    nascimento = int(input('Informe o seu ano de nascimento: '))

# Definindo a idade atual
idade = anoatual - nascimento

# Definindo uma variável para auxiliar o cálculo do tempo para se alistar
alist = 18

if idade > alist:
    if abs(alist - idade) == 1:
        print('{}'
              '\nVocê perdeu o prazo de alistamento, passou 1 ano,'
              '\nO alistamento devia ter sido feito no ano de {}.'
              '\nProcure a junta militar mais proxíma e regularize sua situação junto ao Exercito Brasileiro.'.format(cores['vermelho'], anoatual - 1))
    else:
        print('{}'
              '\nVocê perdeu o prazo de alistamento, passaram {} anos.'
              '\nO alistamento devia ter sido feito no ano de {}'
        '\nProcure a junta militar mais proxíma e regularize sua situação junto ao Exercito Brasileiro.!{}.'.format(cores['vermelho'], abs(alist-idade), anoatual-abs(alist-idade), cores['limpa']))
elif idade == alist:
    print('{}'
          '\nEste é o seu ano de alistamento.! '
          '\nProcure a junta militar mais proxíma de sua residência e faça parte das FORÇAS ARMADAS BRASILEIRAS.{}'.format(cores['verde'], cores['limpa']))
elif idade < alist:
    if abs(alist - idade) == 1:
        print('{}'
              '\nVocê ainda não está em fase de alistamento, falta {}1{} ano.'
              '\nSeu alistamento deverá ser feito no ano de {}{}{}.'.format(cores['azul'], cores['vermelho'], cores['azul'], cores['vermelho'], anoatual + 1, cores['limpa']))
    else:
        print('{1}'
              '\nVocê ainda não está em fase de alistamento, '
          '\nFique atento sobre o prazo máximo, faltam {2}{3}{1} anos para se alistar.'
              '\nSeu alistamento deverá ser feito no ano {2}{4}{0}'.format(cores['limpa'],cores['azul'],cores['vermelho'],abs(idade-alist), anoatual + abs(idade-alist)))

#Desafio Concluído