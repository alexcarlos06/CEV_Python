'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas'''

print('\n')
impar = []
par = []
lista = []
valida = ''
while valida != 'N':
    n = int(input('Digite um número inteiro: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    valida = str(input('Deseja contnuar? [S / N]:  ')).upper().strip()
    while valida not in 'N, S':
        valida = str(input('Deseja contnuar? Para "Sim" digite "S", Para "NÂO" digite "N":  ')).upper().strip()
print(f'{"====X" * 10}\n')
print(f'Os números digitados foram{lista}')
if len(par)== 0:
    print('Não foram digitados números pares')
elif len(par)== 1:
    print(f'O número par digitado foi {par}')
else:
    print(f'Os números pares digitados foram {par}')
if len(impar)== 0:
    print('Não foram digitados números impares')
elif len(impar)== 1:
    print(f'O número impar digitado foi {impar}')
else:
    print(f'Os números impares digitados foram {impar}')


#Desafio Concluído
