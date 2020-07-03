'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

cores = {'azul': '\033[1;34m',
        'amarelo': '\033[1;33m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'negrito': '\033[1m',
         'roxo': '\033[1;35m',
         'azulbebe': '\033[1;36m',
         'cinza': '\033[1;37m',
         'limpa': '\033[m'}

menu = f'''{" "*16}{cores['cinza']}||||||||||||||||||||||||||||
{" "*16}||                        ||
{" "*16}|| {cores['verde']}LOTOFÁCIL ------ [ 1 ] {cores['cinza']}||
{" "*16}|| {cores['verde']}MEGA-SENA ------ [ 2 ] {cores['cinza']}||
{" "*16}|| {cores['verde']}QUINA ---------- [ 3 ] {cores['cinza']}||
{" "*16}|| {cores['verde']}LOTOMANIA ------ [ 4 ] {cores['cinza']}||
{" "*16}|| {cores['verde']}DUPLA-SENA ----- [ 5 ] {cores['cinza']}||
{" "*16}|| {cores['verde']}DIA DE SORTE --- [ 6 ] {cores['cinza']}||
{" "*16}|| {cores['vermelho']}SAIR ----------- [ 0 ] {cores['cinza']}||
{" "*16}||                        ||
{" "*16}||||||||||||||||||||||||||||{cores['amarelo']}

{'='*60}{cores['limpa']}'''

#Listas necessárias.
jogos = ['SAIR', 'LOTOFÁCIL', 'MEGA-SENA', 'QUINA', 'LOTOMANIA', 'DUPLA-SENA', 'DIA DE SORTE']
lista = []
jogo = []
opção = ("0", "1", "2", "3", "4", "5", "6")
mes = ('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO')
#Bibliotéca necessária
from random import randint
from random import choice
from time import sleep

#Mensagem final
mf = f'''
\n{cores["roxo"]}{ " Programa encerrado.! ":=^60}
\n{cores["azul"]}{" Obrigado por utilizar a ACSistemas ":~^60}'''

#Mensagem inicial do programa
print(f'\n{cores["amarelo"]}{" Palpitador de Jogos da Loteria ":=^60}{cores["limpa"]}\n')

#Ínicio da interação do usuário
while True:
    print(menu)
    op = str(input(f'\n{cores["negrito"]}Qual a opção desejada? ')).strip()
    while op not in opção:
        op = str(input('Informe uma opção válida.! '))
    if op == '0':
        break
    pergunta = int(input(f'Quantos jogos de "{jogos[int(op)]}" você deseja exibir? '))
    if op in opção:
        for c in range(0, pergunta):
            sleep(0.8)
            if op == '1':
                while len(jogo) < 15:
                    núm = randint(1, 25)
                    if núm not in jogo:
                        jogo.append(núm)
                lista.append(jogo[:])
                jogo.clear()
            elif op == '2':
                while len(jogo) < 6:
                    núm = randint(1, 60)
                    if núm not in jogo:
                        jogo.append(núm)
                lista.append(jogo[:])
                jogo.clear()
            elif op == '3':
                while len(jogo) < 5:
                    núm = randint(1, 80)
                    if núm not in jogo:
                        jogo.append(núm)
                lista.append(jogo[:])
                jogo.clear()
            elif op == '4':
                while len(jogo) < 50:
                    núm = randint(0, 99)
                    if núm not in jogo:
                        jogo.append(núm)
                lista.append(jogo[:])
                jogo.clear()
            elif op == '5':
                while len(jogo) < 6:
                    núm = randint(1, 50)
                    if núm not in jogo:
                        jogo.append(núm)
                lista.append(jogo[:])
                jogo.clear()
            elif op == '6':
                while len(jogo) < 7:
                    núm = randint(1, 31)
                    if núm not in jogo:
                        jogo.append(núm)
                lista.append(jogo[:])
                jogo.clear()
            if op in '12345':
                lista[c].sort()
                print(f'O {c + 1}º Jogo da "{jogos[int(op)]}" sorteado foi {cores["azulbebe"]}{lista[c]}{cores["limpa"]}')
            else:
                print(f'O {c + 1}º Jogo do "{jogos[int(op)]}" sorteado foi {cores["azulbebe"]}{lista[c]}{cores["limpa"]},{cores["azulbebe"]} {choice(mes)}{cores["limpa"]}')
    sleep(0.5)
    print(f'\n{cores["amarelo"]}{" Boa Sorte ":-^60}{cores["limpa"]}\n')
    resp = str(input('\nDeseja continuar: [S / N] '))
    if resp not in 'SsNn':
        resp = str(input('Informe uma opção válida "S" para continuar ou "N" sair: '))
    if resp in 'Nn':
        break
print(mf)