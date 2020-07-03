'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
   Caso esteja errado peça a digitação novamente até ter um valor correto, '''



sexo = str(input(''
                 '\nInforme "M" para Masculino ou "F" para Feminino : ')).upper().strip()[0]

while sexo not in ['M', 'F']:
    print(''
          '\nSomente são aceito as letras M para masculino e F para Feminino.')
    sexo = str(input('Informe "M" para Masculino ou "F" para Feminino : ')).strip()

if sexo in ['m', 'M']:
    print(''
          '\nO sexo informado foi o sexo Masculino representado pela letra {}.'.format(sexo.upper()))
elif sexo in ['f', 'F']:
    print(''
          '\nO sexo informado foi o sexo Feminino representado pela letra {}.'.format(sexo.upper()))


print(''
      '\nObrigado.!')

# Desafio Concluído