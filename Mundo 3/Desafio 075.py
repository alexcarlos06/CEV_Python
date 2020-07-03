print('''\nDesenvolva um programa que leia quatro valores pelo teclado e guarde -os em uma tupla. No final mostre,
a) quantas vezes apareceu o valor 9 
b) em que posição foi digitado o primeiro valor 3 
c) quais foram os números pares.''')

print('~' * 100)
npar = ''
n1 = int(input('\ninforme um valor: '))
n2 = int(input('informe um valor: '))
n3 = int(input('informe um valor: '))
n4 = int(input('informe um valor: '))

n = (n1, n2, n3, n4)
contagem = n.count(9)
cont3 = n.count(3)
contpar = 0
print('')
if 3 in n:
    posição = n.index(3)
    if cont3 == 1:
        print(f'A) O número "3" foi o {posição +1}º valor digitado.')
    else:
        print(f'A) O número "3" apareceu primeiro no {posição + 1}º valor digitado.')
else:
    print('A) Não foi digitado o número "3" nenhuma vez.')

if contagem == 0:
    print('\nB) O número "9" não foi digitado nenhuma vez.')
elif contagem == 1:
    print(f'\nB) O número "9" foi digitado uma vez.')
else:
    print(f'\nB) O número "9" foi digitado {contagem} vezes')

for c in n:
    if c % 2 == 0:
        contpar += 1
        npar += str(c)
if contpar == 0:
    print('\nC) Não foi digitado nenhum número par.')
elif contpar == 1:
    print(f'\nC) Foi digitado apenas um número para o {npar}')
elif contpar == 2:
    print(f'\nC) Foram digitados {contpar} números pares e são os números {npar[0]} e {npar[1]}')
elif contpar == 3:
    print(f'\nC) Foram digitados {contpar} números pares e são os números {npar[0]}, {npar[1]} e {npar[2]}')
else:
    print(f'\nC) Foram digitados {contpar} números pares e são os números {npar[0]}, {npar[1]}, {npar[2]} e {npar[3]}  ')

# Desafio Concluído.