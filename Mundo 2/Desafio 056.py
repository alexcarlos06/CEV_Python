# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo, Qual é o nome do homem mais velho e Quantas mulheres tem menos de 20 anos.

nome = ''
idade = 0
csexof = 0
idadem = 0

print(''
      '\n{:-^50}'
      '\n'.format(' Análisador de Grupo de Pessoas '))
for c in range(1, 5):
    print('')
    print('{}{}{}{}'.format('-------- ', c, 'º Pessoa', ' --------'))
    n = str(input('Qual o nome : '))
    i = int(input('Qual a idade: '))
    if i < 1:
        print('Informe uma idade maior que zero.')
        exit()
    s = str(input('Qual sexo { M ] / [ F }: ')).strip().upper()
    if s not in ['M', 'F']:
        print('Somente é aceito "F" para sexo Feminino ou "M" para sexo Masculino.'
              '\nTENTE NOVAMENTE.!')
        exit()
    idade += i
    mediaidade = int(idade / c)

    if i > idadem and s == 'M':
        idadem = i
        nome = n
    if s == 'F' and i < 20:
        csexof += 1

print(''
      '\nA média de idade do grupo é {} anos'.format(mediaidade))

if nome == '':
    print('Não existe pessoa do sexo masculino informada no grupo.')
else:
    print('O Homem mais velho do grupo é o Sr {} que tem {} anos'.format(nome.upper(), idadem))
if csexof == 0:
    print('Não existe pessoa do sexo feminino menor de 20 anos no grupo.')
elif csexof == 1:
    print('Existe apenas uma pessoa do sexo Feminino com idade inferior a 20 anos no grupo.')
else:
    print('Existem {} pessoas do sexo feminino com idade inferior a 20 anos no grupo'.format(csexof))

# Desafio Concluído