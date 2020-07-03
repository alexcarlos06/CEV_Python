# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


# Paleta de cores
cores = {'cinza'    : '\033[1;37m',
         'amarelo'  : '\033[1;33m',
         'vermelho' : '\033[1;31m',
         'limpa'    : '\033[1;m'}

# Mensagem ínicial do programa.
print('\n{}{:=^100}{}'
      '\n'.format( cores['vermelho'],' Análisador de números primos', cores['limpa']))

print(cores['cinza'], ''''A definição mais comum é que "um número é primo se for divisível por 1 e por ele mesmo",
  ou então "é  todo o  número com dois e somente dois divisores, ele próprio e a unidade". 
  Sendo assim, por exemplo, o número 7 é primo por ser divisível apenas por 1 e por 7.''''', cores['limpa'])
print('\n'
      '{}{}{}'.format(cores['vermelho'],'*' * 100, cores['limpa']))

num = int(input('\nDigite um número inteiro: '))
cont = 0


if num == 1:
    print(cores['amarelo'],'\nO número ',cores['vermelho'], '1',cores['amarelo'],'NÃO É NÚMERO PRIMO.', cores['limpa'])
    exit()
elif num == -1:
    print(cores['amarelo'], '\nO número ',cores['vermelho'],'-1',cores['amarelo'],'NÃO É NÚMERO PRIMO.', cores['limpa'])
    exit()
for c in range(2, num):
        if num % c == 0:
           cont += 1
if cont  <= 1:
    print('\n{}O número {}{}{} É NÙMERO PRIMO.'.format(cores['limpa'], cores['vermelho'], num, cores['limpa']))
else:
    print('\n{}O número {}{}{} NÃO É NÚMERO PRIMO.{}'.format( cores['amarelo'], cores['vermelho'], num, cores['amarelo'], cores['limpa']))

# Desafio concluído.