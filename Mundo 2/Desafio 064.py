'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999. que é a condição de parada.
 No final mostra quantos números foram digitados e qual foi a soma entre eles ( desconsiderando o flag)'''

print('\n{:*^50}'.format(' Calculadora de Soma ACSistemas '))

n = float(input('\nDigite um número ou 999 para sair: '))
c = 0
soma = 0
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite novamente um número ou 999 para sair: '))
print('\nForam digitados {} números.\nA soma dos números digitados foi {}'.format(c, soma))

# Desafio Concluído
