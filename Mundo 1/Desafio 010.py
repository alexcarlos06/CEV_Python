#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ele pode comprar "Considere US$ 1,00 = R$ 3,27"
din=float(input(' Informe quanto Reais possui: '))
td=float(3.27)
cd=din/td
print('O valor que você pode comprar em dólares é {:.2f} Dólares \n O valor de compra do dólar usado é {} Reais' .format(cd,td))
#Desafio concluído