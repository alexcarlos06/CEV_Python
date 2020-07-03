#Crie um algoritimo que leia um número e mostre seu dobro, triplo e raiz quadrada
n=int(input('Informe um número: '))
n2=n*2
n3=n*3
import math
nr= math.sqrt(n)
print(' O dobro de {} é {} \n O triplo de {} é {} \n A raiz quadrada de {} é {:.3f}'.format(n, n2, n, n3, n, nr))
#Desafio concluído