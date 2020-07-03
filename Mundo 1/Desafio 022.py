# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas, o nome com todas maiúsculas,
# Quantas letras ao todo sem considerar espaços e quantas letras tem o primeiro nome

# Lendo o nome completo e retirando os espaços que foram digitados antes e depois do nome.
n = str(input('Infome um nome completo: ')).strip()

# mostrando na tela o nome em letras maiusculas e minusculas
print('Analisando seu nome........... ')
print('Seu nome em letras maiusculas é: {}'.format(n.upper()))
print('Seu nome em minusculas é: {} '.format(n.lower()))

# Contando a quantidade de caracteres existentes na string subtraindo a quantidade de espaços
print('Seu nome possui {} letras'.format(len(n) - n.count(' ')))

# Exibindo o primeiro nome digitado antes do espaço e a quantidade de caracteres encontrada no primeiro nome
print('O primeiro nome digitado foi: {} e contem {} letras'.format(n[:n.find(' ')], len(n[:n.find(' ')])))

#Desafio concluído