# Crie um programa que leia dois números e mostre a soma entre eles

cores = {'limpa' : '\033[m' , 'azul' : '\033[1;34m' , 'negativo' : '\033[7;30m'}

print('{} Soma entre dois números{}'.format(cores['azul'] , cores['limpa']))
print('{}***************************************************************************'
      '*******************************************************************{}'.format(cores['negativo'] , cores['limpa']))

n1 = int(input('Digite o primeiro número para somar: '))
n2 = int(input('Digite o segundo número para somar: '))
s = n1 + n2

print('A soma entre {} e {} é {}'.format(n1, n2, s))
# Desafio concluído
