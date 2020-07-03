#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#Só irá existir um triângulo se, somente, os seus lados obedeceram à seguinte regra:
# um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados

#Montando a paleta de cores usadas no programa
cores = {'azul' : '\033[4;34m',
         'amarelo' : '\033[1;33m',
         'vermelho' : '\033[1;31m',
         'limpa' : '\033[m' ,
         'negativo' : '\033[7;30m' ,
         'verde' : '\033[1;32m'}

#Mensagem de inicialização
print('{}====================___Verificador de possibilidade de montagem de um Triângulo___===================={}'.format(cores['negativo'] , cores['limpa']))

#fazendo a leitura dos seguimentos de reta
a = float(input('Informe o primeiro seguimento: '))
b = float(input('Informe o segundo seguimento: '))
c = float(input('Informe o terceiro seguimento'))
print('{}****************************************************************************************************{}'.format(cores['amarelo'] , cores['limpa']))
#Montando a condição de acordo com a regra
if abs (b-c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b)< c < (a + b):
    print('{}Os seguimentos informados formam um triângulo.!{}'.format(cores['verde'] , cores['limpa']))
else:
    print('{}Os seguimentos informados não formam um triângulo.!{}'.format(cores['vermelho'] , cores['limpa']))
print('{}****************************************************************************************************{}'.format(cores['amarelo'] , cores['limpa']))
print('{}Para validar as informações entenda a regra: \n'
      'Um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados'.format(cores['azul']))


