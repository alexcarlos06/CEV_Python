'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou nao continuar. No final, mostre:
a) Quantas pessoas tem mais de 18 anos. b) Qantos homens foram cadastrados. c)Quantas mulheres tem mais de 20 anos .'''

print('\n{:^100}\n'.format(' \033[1;4mCadastro de Pessoas \033[m'))

c = ''
maior = homens = mulheres = 0

while c != 'N':
    print('{}\n'.format('-' * 100))
    s = str(input('Informe o sexo [M / F]: ')).upper().strip()[0]
    while s not in 'F,M':
        s = str(input('Informe "M" para Masculino e "F" para Feminino: ')).upper().strip()[0]

    i = int(input('Informe a idade: '))
    while i not in range(1, 1000):
        i = int(input('Informe a idade entre 1 e 999: '))
    if i > 18:
        maior += 1
    if s == 'M':
        homens +=1
    if s == 'F' and i > 20:
        mulheres += 1

    c = str(input('Deseja cadastrar mais [S / N]: ')).upper().strip()[0]

    while c not in 'S,N':
        c = str(input('Deseja cadastrar mais [S / N]: ')).upper().strip()[0]

    if c == 'N':
        print('~' * 100, '\033[1;32m')
        break

if maior == 0:
    print('\nNão foi Cadastrado nenhuma pessoa com idade superior a 18 anos.')
elif maior == 1:
    print('\nFoi cadastrada uma pessoa com idade superior a 18 anos.')
else:
    print(f'\nforam cadastradas {maior} pesoas com idade superior a 18 anos.')

if homens == 0:
    print('Não foi cadastrado nenhuma pessoa do sexo masculino.')
elif homens == 1:
    print('Foi cadastro uma pessoa do sexo masculo.')
else:
    print(f'Foram cadastradas {homens} pessoas do sexo masculino.')

if mulheres == 0:
    print('Não foi cadastrada nenhuma pessoa do sexo femino com idade superior a 20 anos.')
elif mulheres == 1:
    print('Foi cadastrada uma pessoa do sexo feminino com idade superior a 20.')
else:
    print(f'Foram cadastradas {mulheres} pessoas com sexo feminino e idade superior a 20 anos.')

print('\n\n\n\033[m{:=^110}'.format(' \033[1;4mObrigado por utilizar o sistema de cadastro ACSistemas\033[m '))

# Desafio Concluído.