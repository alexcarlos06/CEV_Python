#Faça um programa que que leia três números e mostre qual é o maior e qual é o menor.

#Mensagem incial do programa.
print('xxxxX__Verificador de números maiores e menores__Xxxxx ')
print('-----'*20)

#lendo os números inseridos
n1 = int(input('Informe o primeiro núumero: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

#montando a lista para ferificação

maior = max(n1 , n2 , n3 )
menor = min(n1 , n2 , n3)

print('====='*20)

print('Entre os numeros {}, {} e {} o maior é {} e o menor é {}'.format(n1, n2, n3, maior, menor))

# Desafio concluído