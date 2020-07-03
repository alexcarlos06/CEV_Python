#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
#Equilátero: todos os lados iguais ; Isóceles: dois lados iguais ; Escaleno: todos os lados diferentes.
#Se os 3 seguimentos de retas formarem o triângulo o programa precisa responder qual o tipo de triangulo montado.

# montando a paleta de cores
cores = {'azul'     : '\033[1;34m',
         'amarelo'  : '\033[1;33m',
         'verde'    : '\033[1;32m',
         'vermelho' : '\033[1;31m',
         'limpa'    : '\033[1;m'}

# Mensagem ínicial do programa
print('{1}{0} Validador de possibilidade e Conferência do tipo do Triângulo {0}{2}'.format('*' * 20, cores['azul'],cores['limpa'] ))
print('')

a = int(input('Informe o primeiro seguimento de reta: '))
b = int(input('Informe o segundo seguimento de reta: '))
c = int(input('Informe o terceiro seguimento de reta: '))
print('')
print('{}{}{}'.format(cores['azul'], '*' *80, cores['limpa']))
print( '{}Triângulo Isósceles. Tem dois lados iguais e um diferente. '
       '\nTriângulo Equilátero. Todos os lados são iguais.'
       '\nTriângulo Escaleno. Nenhum dos lados é igual.{}'.format(cores['amarelo'], cores['limpa']))
print('{}{}{}'.format(cores['azul'], '*' * 80, cores['limpa']))
print('')

# Montando a estrura de condição para validar se é possível montar um triangulo retângulo e qual o tipo de triângulo montado
if abs(c - b) < a < (c + b) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    if a == b == c:
        print('{0}É possível montar um Triângulo do {2}tipo Equilátero{0} com os seguimentos de reta que foram informados{1}'.format(cores['verde'], cores['limpa'], cores['vermelho']))
    elif a == b or b == c or a == c:
        print('{0}É possível montar um Triângulo do {2}tipo Isóceles{0} com os seguimentos de reta que foram informados{1}'.format(cores['verde'],cores['limpa'], cores['vermelho']))
    else:
        print('{0}É possível montar um Triângulo do {2}tipo Escaleno{0} com os seguimentos de reta que foram informados{1}'.format(cores['verde'], cores['limpa'], cores['vermelho']))
else:
    print('{}Não é possível montar um Triângulo  com os seguimentos de reta apresentados{}'.format(cores['vermelho'],cores['limpa']))

# Desafio Concluído
