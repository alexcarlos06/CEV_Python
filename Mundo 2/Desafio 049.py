# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um loço for.


# Paleta de cores
cores = {'azulbebe'  : '\033[1;36m',
         'limpa'     : '\033[1;m',
         'amarelo'   : '\033[1;33m'}

# Mensagem inicial:
print('{}'
      '\n{:=^39}{}'
      '\n'.format(cores['azulbebe'], ' Gerador de tabuadas ACSousa ', cores['limpa']))

# Lendo qual tábuada o usuário deseja exibir:
t = int(input('Infome qual tabuada deseja exibir: '))

# Definindo a variável responsável por contar quantos valores estão dentro do laço de repetição,
# para este caso vamos usar está variável para fazer a multiplicação entre o valor solicitado pelo usuário e a quantidade de laços de repetição.
cont = 0

# Print para melhorar a identificação visual do programa
print('{}{}'
      '\n'.format(cores['azulbebe'], '*' * 39))
print('{}{}{} x 0 = 0'.format(cores['amarelo'] ,' '*15, t))


# Montando a estrutura de repetição para montar a tabuada.
for c in range(0, 10):
    cont = cont +1 # Quantidade de vezes que o laço de repetição foi feito.
    res = t *cont  # Variável para mltiplicar o valor da tabuada solicitado pelo usuário vezes a quantidade de laços de repetição.
    print('{}{} x {} = {}'.format(' ' *15, t, cont, res)) # Este print é feito a cada laço de repetição, nele estão contidos as variáveis armazenadas a cada laço.
print('{}'
      '\n{}'.format(cores['azulbebe'], '*' * 39))

# Desafio concluído