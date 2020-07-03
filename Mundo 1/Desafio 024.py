
# Crie um programa que leia o nome de uma cidade e diga se ele começa ou não com o nome "santo"

#Lendo a variável retirando os espaçõs digitados antes e depois do nome com o método split e tranformando em uma lista de módulos com a método split
cidade = str(input('Informe o nome de uma cidade: ')).strip().split()

# Fatiando a string para obter o primeiro nome

# Mostrando na tela se o primeiro módulo da palvra digitada inicialmente é igual "==" a palavra "santo"
print('O nome da cidade digitada começa com a palavre "SANTO" ?  {}\n\nTrue = Sim, False =  Não.  '.format('santo' == cidade[0].lower() ))

#Desafio concluído