# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar desconsidere-o.

# Mensagem ínicial do programa
print(''
      '\n{:^50}'
      '\n'.format(' Calculadora de soma de números PARES '))

# Variáveis responsáveis pela contagem dos valores e pela soma dos valores pares.
cont = 0
soma = 0

# Laço de repetição que executa a instrução no intervalo que vai de 1 até 7, ou seja, o laço é feito 6 vezes.
for c in range(1, 7):
    num = int(input("Digite o {}º número inteiro: ".format(c))) # É feito o laço de repetição com a instução "num" todas as vezes dentro do intervalo do laço de repetição.
    if num % 2 == 0: # A estrutura condicional é responsável por por somar e contar apenas valores que tenham o resto da divisão por 2 = a 0, ou seja, apenas números pares.
        soma += num
        cont += 1

# Tratamento das mensagens de acordo com os valores digitados.
if soma == 0:
    print(''
          '\nVocê não informou nenhum número PAR para ser somado.!')
elif cont == 1:
    print(''
          '\nVocê informou apenas UM número para a soma que foi o número {}'.format(soma))
else:
    print(''
          '\nVocê informou {} números pares e a soma foi {}'.format(cont, soma))

# Desafio Concluído


