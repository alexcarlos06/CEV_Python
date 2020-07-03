# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para headecimal.

# Montando a paleta de cores
cores = {'azul'      : '\033[1;34m',
         'verde'     : '\033[1;32m',
         'negativo'  : '\033[7;30m',
         'amarelo'   : '\033[1;33m',
         'vermelho'  : '\033[1;31m',
         'limpa'     : '\033[1;m'}

# Exibindo a mensagem inicial do programa
print(cores['verde'],'+++++' * 10,'      Calculadora de conversão de números decimais para as bases BINÁRIA, OCTAL E HEXADECIMAL    ','+++++' * 10, cores['limpa'])
print('#####' * 40)

# Fazendo a leitura da base a ser convertida
print(cores['azul'],'Para base BINÁRIA pressione "1"'
      '\n Para base OCTAL pressione "2"'
      '\n Para base HEXADECIMAL pressione "3"'
      '\n Para sair tecle "0"' , cores['limpa'])
print('#####'*40)

# Fazendo a leitura da opção de conversão desejada.
opção = int(input(' Selecione a opção desejada: '))

# Fazendo a estrutura de decisão para validar a opção escolhida caso seja uma opção inválida o processo é abortado, caso seja uma opção válida o programa segue a próxima instrução.
if   opção == 0:
    print(cores['amarelo'],'Processo de conversão abortado',cores['limpa'])
    exit()

elif opção not in [1, 2, 3]:
    print(cores['vermelho'],'Escolha uma opção valida.'
          '\n Processo de conversão abortado.!', cores['limpa'])
    exit()

# Fazendo a leitura do número a ser convertido
num = int(input(' Digite um número inteiro a ser convertido: '))

# definindo variáveis para facilitar a conversão dos números.
binario     = str.upper(bin(num))
octal       = str.upper(oct(num))
hexadecimal = str.upper(hex(num))

# Fazendo a estrutura de decisão de acordo com a opção selecionada.
if   opção == 1:
    print(cores['verde'], 'O número {} na base BINÁRIA é: {} '.format(num , binario[2:]))

elif opção == 2:
    print(cores['verde'], ' O número {} na base OCTAL é: {} '.format(num , octal[2:]))

elif opção == 3:
    print(cores['verde'], ' O número {} na base HEXADECIMAL é: {} '.format(num , hexadecimal[2:]))
print('\n ')
print(cores['negativo'],'*****' * 14,'Obrigado por usar a CALCULADORA DE CONVERSÃO GREGORIANA','*****' * 14)

# Desafio Concluído.