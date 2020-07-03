#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

# Mensagem inicial do programa

print('xxxxxX Verificador de Ano Bissexto Xxxxxx')
print('========'*10)

#Colhendo a informação do ano consultado
ano = int(input('Informe qual ano deseja verificar: '))

#Montando a condição, se o resto da divisão por 400 do ano for 0 então o ano é bissexto, se o resto da divisão por 100 for 0 então ano não é bissexto por fim se o resto da divisão
#por 4 for igual a zero então o ano sera um ano bissexto .
if ano % 400 == 0:
    print('O ano {} é um ano bissexto.'.format(ano))
elif ano % 100 == 0:
    print('O ano {} não é um ano bissexto.'.format(ano))
elif ano % 4 == 0:
    print('O ano {} é um ano bissexto.'.format(ano))
else:
    print('O ano {} não é um ano bissexto.'.format(ano))

    # Desafio concluído
