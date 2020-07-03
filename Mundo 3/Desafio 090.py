'''Faça um programa que leia nome e média de um aluno, guardando também a situaçãoem um dicionário.
No final, mostre o conteúdo da estrutura na tela'''

print(f'{"~" * 50}\n{"Análisador de Notas Escolares":^50}\n{"~" * 50}')

'''Fazendo a leitura do nome e da média do aluno'''
n = str(input('\nNome: ')).capitalize()
m = float(input(f'Média de {n}: '))

'''De acordo com a média informada registrando no dicionário a situação do aluno'''
if m < 4:
    s = 'REPROVADO'
elif m < 7:
    s = 'RECUPERAÇÃO'
else:
    s = 'APROVADO'

'''Validando o valor informado para a média'''
while m < 0 or m >10:
    m = float(input(f'A média infromada não é válida'
                    f'\nInforme a média entre 0 e 10: '))

'''Declarando o dicionário "dados" e informando que ele irá receber os dados coletados do usuários'''
dados = {'Nome': n, 'Média': m, 'Situação': s}

print(f'\n{"-*" * 25}\n')

'''Informando os resultados na tela com um laço '''

for k, v in dados.items():
    print(f'{k} é igual a {v}')

# Desafio concluído

