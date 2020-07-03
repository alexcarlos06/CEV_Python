#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para a viagens de até 200Km e R$0,45 para viagens mais longas

#mensagem inicial do programa
print('===x=== Cálculo de Preço de Passagem ===x===')

#Leitura da distância
km = float(input('Informe a distância em Km até o destino: '))

#Definindo as condições
if km >= 200:
    print('O valor da passagem será R$ {:.2f} '.format(km*0.45))
else:
    print('O valor da passagem será R$ {:.2f} '.format(km*0.5))

#Desafio concluído