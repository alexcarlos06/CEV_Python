#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
#Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais , o aumento é de 15%

#Mensagem inicial
print('                                  ----__Cálculo de Salário com aumento__----')
print('-----' * 20)

#Lendo o salário

s = float(input('Informe o salário atual: '))

s1 = 10 #percentual de aumento 1º faixa
s2 = 15 #percentual de aumento 2º faixa

# definindo o novo salário de acordo com a faixa salarial atual

if s > 1250.00:
    print('Seu novo salário será R$ {:.2f}'.format(s+(s*(s1/100))))
else:
    print('Seu novo salário será R$ {:.2f} '.format(s+(s*(s2/100))))

    # Desafio concluído