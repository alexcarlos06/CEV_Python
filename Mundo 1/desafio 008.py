#Escreva um programa que leia um valor em metros e o exiba convertido em centimentros e milimetros
m=int(input('Informe a quantidade de metros que desja converter: '))
mm=int(1000)
cm=int(100)
mmconverte=m*mm
cmconverte=m*cm
print(' Em {} metros existem {} centimetros e {} milimetros.'.format(m, cmconverte, mmconverte))
#Desafio concluído