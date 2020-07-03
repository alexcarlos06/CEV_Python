#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com as informações abaixo:
#Abaixo de 18.5: Abaixo do peso ; Entre 18.5 e 25: Peso ideal ; 25 até 30: Sobrepeso ; 30 até 40: Obesidade ; Acima de 40: Obesidade Mórbida.

# Paleta de cores
cores = {'vermelho' : '\033[1;31m',
         'verde'    : '\033[1;32m',
         'amarelo'  : '\033[1;33m',
         'azul'     : '\033[1;34m',
         'roxo'     : '\033[1;35m',
         'limpa'    : '\033[1;m',
         'negativo' : '\033[7;30m'}

# Mensagem ínicial do programa
print('{1}{0} Calculadora de IMC {0}{2}'.format('*' * 40, cores['negativo'], cores['limpa']))
print('')

# Tabela informativa:
print('#' *100)
print('{} Classificação IMC'.format(' ' * 35))
print('')
print('{}*Abaixo do peso: Índice de 0 a 18, 4 kg / m2 : Fadiga, stress, ansiedade.'
      '\n*Peso normal: Índice de 18, 5 a 24, 9 kg / m2 : Menor risco de doenças cardíacas e vasculares. '
      '\n*Sobre peso: Índice de 25 a 29, 9 kg / m2 : Fadiga, má circulação, varizes. '
      '\n*Obesidade: Índice acima de 30 kg / m2 Diabetes, angina, infarto, aterosclerose, '
      '\n     apneia do sono, falta de ar, refluxo, dificuldade para se mover, escaras, AVC.{}'.format(cores['roxo'], cores['limpa']))
print('')
print('#' * 100)
print('')
# Colhendo as informações necessárias:
h = float(input('Informe a sual altura (m): '))
m = float(input('Informe o seu peso (kg): '))
print('')
# Definindo as variáveis para auxiliar os cálculos:
imc = (m) / h ** 2

ap = 18.5 # Faixa 'abaixo do peso'
pi = 25   # Faixa 'peso ideal'
sb = 30   # Faixa 'sobrepeso'
o  = 40   # Faixa 'obesidade'

if imc < ap:
    print('{} Atenção você está Abaixo do peso, seu IMC é {: .1f}{}'.format(cores['roxo'], imc, cores['limpa']))
elif imc < pi:
    print('{}Parabéns você está no Peso ideal, seu IMC é {: .1f}{}'.format(cores['verde'], imc, cores['limpa']))
elif imc < sb:
    print('{}Atenção você está na faixa de Sobre peso, seu IMC é{: .1f}{}'.format(cores['amarelo'], imc, cores['limpa']))
elif imc < o:
    print('{}Atenção você está na faixa de Obesidade, seu IMC é {: .1f}{}'.format(cores['vermelho'], imc, cores['limpa']))
else:
    print('{}Cuídado você está na faixa de Obesidade morbida, seu IMC é {: .1f}{}'.format(cores['vermelho'], imc, cores['limpa']))

    # Desafio Concluído