# Desenvolva um programa que leia o primeiro termo e arazão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('\033[1;m'
      '\n')
qtd = int(input('Informe quantos termos deseja exibir da Progressão Aritimética: '))
if qtd < 2:
    print('Informe uma quantida maior que "1" para exiir a Progressão Aritimética')
    exit()
pt = int(input('Informe o primeiro termo da Progressão Aritimética: '))
rz = int(input('Informe a razão da Progressão Aritimética: '))


print('')

for c in range(0, qtd):
    pa = pt + c * rz
    print('O {}º termo da P.A. é   {}{}{}'.format(c + 1, '\033[1;32m', pa, '\033[m'))

# Desafio concluído