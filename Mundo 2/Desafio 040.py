#Crie um programa que leia duas notas de um aluno e calcule a suam média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO ; Média entre 5.0 e 6.9: RECUPERAÇÃO ; Média 7.0 ou superior: APROVADO.


# Montando a peleta de cores:
cores = {'amarelo'     : '\033[1;33m',
         'vermelho'    : '\033[1;31m',
         'verde'       : '\033[1;32m',
         'limpa'       : '\033[1;m',
         'azul'        : '\033[1;34m'}

# Mensagem ínicial do programa
print('{}{} Verificador de Aprovação Escolar {}{}'.format(cores['azul'],'*' * 20,'*' * 20, cores['limpa']))
print('')

# Lendo as duas notas dos alunos
n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluno: '))
print('')

# Criando as variáveis necessárias para efetuar os cálculos
média = (n1+n2) / 2

# Montando a condição para verificar se o aluno foi reprovado, está de recuperação ou foi arovado.
if média >= 7:
    print('{}O aluno está APROVADO a média obtida foi {} .'.format(cores['verde'], média))
elif  média >= 5:
    print('{}O aluno está de RECUPERAÇÃO, a média obtida foi {} .'.format(cores['amarelo'], média))
else:
    print('{}O aluno está REPROVADO, a média obtida foi {}{}'.format(cores['vermelho'], média, cores['limpa']))

# Desafio Concluído