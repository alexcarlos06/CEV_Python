'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

#Paleta de Cores.
cores = {'azul': '\033[1;34m',
        'amarelo': '\033[1;33m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'negrito': '\033[1m',
         'roxo': '\033[1;35m',
         'azulbebe': '\033[1;36m',
         'cinza': '\033[1;37m',
         'limpa': '\033[m'}
#Listas necessárias.
cadastro = list()
temp = list()
opção = list()

#Variáveis necessárias.
cont = méd = 0
op = ''
#Bibliotécas
from time import sleep

#Mensagem inicial
print(f'\n{cores["roxo"]}{" Cadastro de Notas Escolares ":~^80}{cores["negrito"]}\n')

#Inicio da interação do usuário com o programa
while True:
    while True:
        nome = str(input('Nome: ')).strip().upper()
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        méd = (nota1 + nota2)/2
        cadastro.append([nome, méd, [nota1, nota2]])
        resp = str(input('Deseja continuar? [S / N] ')).upper().strip()
        while resp not in 'NS':
            resp = str(input(f'{cores["vermelho"]}"S" para SIM ou "N" para NÃO: {cores["negrito"]}')).upper().strip()
        if resp == 'N':
            break

    for c in range(0, len(cadastro)):
        if c == 0:
            print(f'{cores["amarelo"]}{"_"*32}'
                  f'\n|{cores["azulbebe"]}{"Cod":^5}{"Nome":<20}{"Média":<5}{cores["negrito"]}{cores["amarelo"]}|'
                  f'\n|{cores["negrito"]}{c+1:^5}{cadastro[c][0]:<20}{cadastro[c][1]:<5}{cores["amarelo"]}|')
        else:
            print(f'|{cores["negrito"]}{c+1:^5}{cadastro[c][0]:<20}{cadastro[c][1]:<5}{cores["amarelo"]}|')
    print(f'{"_"*34}{cores["negrito"]}')

    for c in range(0, len(cadastro)+1):
        opção.append(str(c))
        if "999" not in opção:
            opção.append("999")
    while True:
        op = str(input('\nInforme o código do aluno para vizualiar as notas, "999" para cadastrar mais alunos ou "0" para sair: '))
        while op not in opção:
            op = str(input(f'{cores["vermelho"]}Informe um código válido ou "0" para sair: ')).strip().upper()
        if op != "999" and op != "0":
            print(f'\n{cores["azulbebe"]}{cadastro[int(op)-1][0]}{cores["negrito"]} obteve as notas {cores["azulbebe"]}{cadastro[int(op)-1][2]}{cores["negrito"]}.')
        elif op == "0":
            print(f'\n{cores["negrito"]}Finalizando...')
            sleep(0.8)
            print(f'{cores["roxo"]}{" Obrigado por utilizar o sistema de médias ACSistemas ":~^80}')
            exit()
        else:
            break