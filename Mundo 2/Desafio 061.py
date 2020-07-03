'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while'''

# Paleta de cores:
cores = {'azul': '\033[1;34m',
         'vermelho': '\033[1;31m',
         'limpa': '\033[m'}

# Mensagem ínicial
print('{:^30}{}{}'.format(cores['azul'], ' Gerador de PA 10  termos', cores['limpa']))

print('')
r = int(input('Informe a razão da PA: '))
n = int(input('Informe o primeiro termo: '))


print('')

c = 0
pa = n

print('')
while c < 10:
    print('{}'.format(pa), end='')
    c += 1
    pa += r
    print(' --> ' if c <= 9 else '', end='')
print(' FIM!')

# Desafio Concluído.