'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de "ZERO",
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

#Importando as bibliotécas necessárias
from datetime import datetime

#mensagem ínicial do progrma
print(' Cadastro de trabalhador '.center(40, "~"))

#Declarando o dicionário que irá conter os dados do trabalhador
dados = dict()

#Fazendo a leitura dos dados e adicionando ao dicionário

dados['Nome'] = input(str('Nome: ')).capitalize()
anoatual = datetime.now().year
nasc = int(input('Ano de nascimento: '))

while nasc >= anoatual:
    nasc = int(input(f'Informe um ano de nascimento menor ou igual a {datetime.now().year}: '))
dados['Idade'] = datetime.now().year - nasc

ctps = str(input('Informe o numero da CTPS (0 caso não possua)'))
if ctps != "0":
    dados['CTPS'] = ctps
    Ano_de_Contratação = int(input('Informe o ano de contratação: '))

    while Ano_de_Contratação < nasc or Ano_de_Contratação > datetime.now().year:
        Ano_de_Contratação = int(input('Informe o ano de contratação válido: '))

    dados['Ano_de_Contratação'] = Ano_de_Contratação
    dados['Salário'] = float(input('Informe o salario: R$ '))
    dados['Aposentadoria'] = (dados['Ano_de_Contratação'] + 35) - nasc

print(f'\n{"~" * 30}\n')
print(f'{dados["Nome"]} tem {dados["Idade"]} anos de idade')
print(f'Foi contratado no ano de {dados["Ano_de_Contratação"]} com salário de R$ {dados["Salário"]}\nSe aposentará com {dados["Aposentadoria"]} anos de idade'if ctps != "0" else "")

#Desafio concluído