'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

# Paleta de cores:
cores = {'azul': '\033[1;34m',
         'vermelho': '\033[1;31m',
         'limpa': '\033[m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m'}

# Mensagem ínicial
print('{:^60}{}{}'.format(cores['azul'], ' Gerador de PA ', cores['limpa']))
print('{}{}{}'.format(cores['amarelo'], '=' * 120, cores['limpa']))
print('')
r = int(input('Informe a razão da PA: '))
n = int(input('Informe o primeiro termo: '))


print('')

c = 0
pa = n
nt = ''
termos = 10
print('')

while c <= termos:
    if c == termos:
        print(' = = = Foram gerados {}{}{} termos até o momento'.format(cores['vermelho'], c, cores['limpa']))
        nt = int(input('\nPressione 0 para sair ou informe mais quantos termos deseja exibir:  '))
        if nt == 0:
          print('\n{}Obrigado por utilizar o Gerador de PA ACSistemas.{}'.format(cores['verde'], cores['limpa']))
          exit()
        else:
            termos += nt
            print('{}{}{}'.format( cores['vermelho'],pa, cores['limpa']), end='')
            c += 1
            pa += r
            print('{} -->{} '.format(cores['azul'], cores['limpa'])if c <= termos - 1 else '{}'.format(cores['limpa']), end='')

    else:
        print('{}{}{}'.format(cores['vermelho'], pa, cores['limpa']), end='')
        c += 1
        pa += r
        print('{} -->{} '.format(cores['azul'], cores['limpa']) if c <= termos - 1 else '{}'.format(cores['limpa']), end='')

# Desafio Concluído.