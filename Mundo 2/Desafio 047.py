# Crie um programa que mostre na tela todos os numeros pares que estão em um intervalo entre 1 e 50.


#Paleta de cores:
cores = {'limpa'     : '\033[1;m',
         'amarelo'   : '\033[1;33m',
         'azulbebe'  : '\033[1;36m',
         'vermelho'  : '\033[1;31m',
         'azul'      : '\033[1;34m',
         'verde'     : '\033[1;32m'}

# Mensagem ínicial do programa.
print('{}{:=^50}{}'
      '\n'.format(cores['azulbebe'],' Verificador de números inteiros pares ou ímpares ', cores['limpa']))

# Montando a estrutura visual da tela de opções.
print('{}{}{}'
      '\n{: ^50}'
      '\n'.format(cores['azul'], '*' * 50, cores['limpa'], 'Lista de Opções', ))

# Variável para determinar qual item foi escolhido de acordo com a opção selecionada.
itens = ('Pares', 'Ímpares')

print('''[ 1 ] Para números pares 
[ 2 ] Para números ímpares
[ 0 ] Para sair''')
print(''
      '\n{}{}{}'
      '\n'.format( cores['azul'], '*' * 50, cores['limpa']))

# Lendo a opção escolhida
o = int(input('Informe a opção desejada: '))

# Montando a estrutura condicional para determinar se opção escolhida é uma opção válida.
if o == 0:
    print(''
          '\n{}Obrigado por utilizar o nosso verificador de números.{}'.format(cores['verde'], cores['limpa']))
    exit()
elif o not in [1, 2]:
    print(''
          '\n{}Escolha uma opção válida.!{}'.format(cores['amarelo'], cores['limpa']))
    exit()

# Lendo as informações para determinar a sequência a ser analisáda
i = int(input('Informe o primeiro número da sequência: '))
f = int(input('Informe o ultimo número da a sequência: '))

print(''
      '\nOs números {1}{2}{0} dentro da sequência entre {1}{3}{0} e {1}{4}{0} são os números:  '.format(cores['limpa'], cores['vermelho'], itens[o-1], i, f))
for c in range(i, f+1):
    if o == 1:
        if c % 2 == 0 and c != 0:
            print(c, end=', ')
    else:
        if c % 2 == 1 and c != 0:
            print(c, end=', ')
print('')

# Desafio concluído