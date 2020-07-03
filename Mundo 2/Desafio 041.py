#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM ; Até 14 anos: INFANTIL ; Até 19 anos: JUNIOR ; Até 20 anos: SÊNIOR ; Acima: MASTER.

# Importando o metodo date dentro da bibliotéca detetime
from datetime import  date

# Paleta de cores
cores = {'negrito' : '\033[7;30m',
         'limpa'   : '\033[1;m',
         'azul'    : '\033[1;34m',
         'amarelo' : '\033[1;33m',
         'verde'   : '\033[1;32m'}





from datetime import date

# Mensagem ínicial do programa
print('{1}{0}CONFEDERAÇÃO NACIONAL DE NATAÇÃO {0}{2}'.format('*' * 30, cores['negrito'], cores['limpa']))
print('')
print('{}{}{}'.format(cores['azul'], '***' * 31, cores['limpa']))
print('{}ATENÇÃO.!'
      '\nPara a classificação não é levado em conta o mês e nem o dia de nascimento, '
      '\nÉ usado apenas o ano como base.{}'.format(cores['amarelo'], cores['limpa']))

print('{}{}{}'.format(cores['azul'], '***' * 31, cores['limpa']))



print('')
# Fazendo a leitura da data de nascimento  do atleta
ano = int(input('Informe o seu ano de nascimento:  '))
print(cores['verde'])

# Montando a variavel para auxíliar o cálculo da idade.
idade = date.today().year - ano

# Montando a estrutura condicional para definir a classe de acordo com o ano de nascimento.
if idade <= 9 :
    print('O atleta tem {} anos.'
          '\nSua categoria é MIRIM.'.format(idade))
elif idade <= 14 :
    print('O atleta tem {} anos.'
          '\nSua categoria é INFANTIL.'.format(idade))
elif idade <= 19 :
    print('O atleta tem {} anos.'
          '\nSua categoria é JÚNIOR.'.format(idade))
elif idade <= 20 :
    print('O atleta tem {} anos.'
          '\nSua categoria é SENIOR.'.format(idade))
elif idade > 20:
    print('O atleta tem {} anos.'
          '\nSua categoria é MASTER.'.format(idade))

#Desafio Concluído