#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

#Mensagem inicial
print('-_-_- X -_-_- Verificador de números pares -_-_- X -_-_-')

#Lendo o número a ser verificado
num = int(input('Digite um número inteiro para ser verificado: '))

#vericando se o número é par ou impar
check = num % 2

#Condição se o resultado da variável check for 0 então o número é par se nao é impar
if check == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} não é par.'.format(num))

#Desafio concluído
