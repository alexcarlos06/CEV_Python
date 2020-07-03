'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

print('\033[1;33m\n{:=^100}\033[m\n'.format(' Verificador de Médias ACSistemas '))

n = int(input('\033[1;36mDigite um valor inteiro: \033[m '))

c = 1
valida = ''
soma = n
maior = n
menor = n

while valida != 'N':
    if c <= 1:
        n = int(input('\033[1;36mDigite outro valor inteiro: \033[m '))
        soma += n
        c += 1
        if n > maior:
            maior = n
            menor = menor
        else:
            maior = maior
            menor = n

    else:
        valida = str(input('\033[1;33mDeseja continuar { S / N ]: \033[m')).upper().strip()
        print('')
        if valida not in 'N , S':
            print('\033[1;31mVocê digitou {} !\n\033[1mDigite "S" para continuar ou "N" para sair.\033[m\n'.format(valida))
        elif valida == 'S':
            n = int(input('\033[1;36mDigite outro valor inteiro: \033[m'))
            soma += n
            c += 1
            if n > maior:
                maior = n
                menor = menor
            elif n < menor:
                maior = maior
                menor = n
média = soma / c
print('Você digitou {0}{2}{1} valores.\nA soma foi {0}{3: .2f}{1} e a média é {0}{4: .2f}{1}'.format('\033[1;36m', '\033[m', c, soma, média))

if menor == maior:
    print('Os Valores digitados são iguas, por tanto não existe valor maior nem menor')
else:
    print('O maior valor é {0}{2}{1} e o menor valor é {0}{3}{1}'.format('\033[1;36m', '\033[m', maior, menor))

print('\n\033[3;31m{:=^100}'.format(' Obrigado por utilizar nosso Sistema de Análise de números.! '))


# Desafio Concluído