# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.


f = str(input('Informe a frase: ')).strip().upper()
fr = f.split()
frase = ''.join(fr)
inverso = ''
qtd = len(frase)

for c in range(qtd -1, -1, -1):
     inverso +=frase[c]
print('O contrário da frase {} é {}.'.format(frase, inverso))
if inverso == frase:
    print('Portanto é um Palíndromo.')
else:
    print('Portanto não é um palíndromo.')