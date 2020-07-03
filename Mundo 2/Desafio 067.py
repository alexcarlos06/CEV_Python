'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo'''

print('\n\033[1;34m{:=^100}\033[m\n'.format(' \033[1;33mTabuada 3.0\033[1;34m '))

t = int(input('\033[4;32mInforme qual tabuada deseja exibir:\033[1m '))
print('')
c = 0
while True:
    if t <= 0:
        break
    else:
        while c <= 10:
            resultado = t * c
            print(f'{t} x {c} = {resultado}')
            c += 1
        c = 0
        t = int(input('\n\033[4;32mInforme qual tabuada deseja exibir:\033[1m '))
        print('')
print('\n\033[1;34m{:=^100}\033[m'.format('\033[1;33m Obrigado por utilizar O Gerador de Tabuadas ACSistemas\033[1;34m '))

# Desafio Concluído