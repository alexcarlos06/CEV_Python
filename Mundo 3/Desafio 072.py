'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado ( entre 0 e 20) e mostrá-lo por extenso.'''

numeral = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
           'Dezessei', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

print('\n{:-^100}\n'.format(' Leitor de Números '))

while True:
    n = int(input('Informe um número inteiro entre 0 e 20: '))
    while n not in range(0, len(numeral)):
        n = int(input('São aceito apenas números inteiros entre 0 e 20 ou 999 para sair.'
                      '\nInforme um número  '))
        if n == 999:
            print('{:~^50}'.format(' Programa Finalizado '))
            exit()
    print(f'\nO número digitado foi {numeral[n]}')
    r = str(input('\nDeseja continuar [S / N]: ')).upper().strip()[0]
    while r not in 'NS':
        r = str(input('Digite "S" para continuar ou "N" Para sair: ')).upper().strip()[0]
        if r == 'N':
            print('\n{:~^50}'.format(' Programa Finalizado '))
            break



