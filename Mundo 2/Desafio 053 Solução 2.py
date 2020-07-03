# Resolução do desafio 53 sem o auxílio da instrução "for"

frase = str(input('Digite uma frase:  ')).strip().upper()
palavras = frase.split()
palavra = ''.join(palavras)
qtd = len(palavra)
teste = palavra[qtd:: -1]

print('O inverso da frase {} é {}'.format(palavra, teste))
if teste == palavra:
    print(''
          '\nA frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palindromo.')