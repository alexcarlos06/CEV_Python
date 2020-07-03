'''Crie uma tupla preenchida com 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
 na ordem de colocação. Depois mostre:
a) apenas os 5 primeiros colocados b) os últimos 4 colocados da tabela c) uma lista com os times em ordem alfabética.
 d) Em que posição da tabela esta o time da chapecoense'''

times = ('França', 'Croácia', 'Bélgica', 'Inglaterra', 'Uruguai', 'Brasil', 'Suécia', 'Rússia', 'Colômbia', 'Espanha',
         'Dinamarca', 'México', 'Portugal', 'Suíça', 'Japão', 'Argentina', 'Senegal', 'Irã', 'Coreia do Sul', 'Peru',
         'Nigéria', 'Alemanha', 'Sérvia', 'Tunísia', 'Polônia', 'Arábia Saudita', 'Marrocos', 'Islândia', 'Costa Rica',
         'Austrália', 'Egito', 'Panamá')
times2 = ('Franca', 'Croacia', 'Belgica', 'Inglaterra', 'Uruguai', 'Brasil', 'Suecia', 'Russia', 'Colombia', 'Espanha',
          'Dinamarca', 'Mexico', 'Portugal', 'Suica', 'Japao', 'Argentina', 'Senegal', 'Ira', 'Coreia do Sul', 'Peru',
          'Nigeria', 'Alemanha', 'Servia', 'Tunisia', 'Polonia', 'Arabia Saudita', 'Marrocos', 'Islandia', 'Costa Rica'
          , 'Australia', 'Egito', 'Panama')

print('\n\033[1;4;36m{:~^100}\033[m'.format(' Análisador de Classificação Copa do Mundo 2018 '))

menu = f'''
\033[1;4;34m{'~'* 35}\033[m
\033[1;4m{'Menu':^35}\033[m

[1] Classificação Geral
[2] Os 4 primeiros Colocados
[3] Os 4 Últimos Colocados
[4] Colocação por Seleção
[5] Nome da Seleção por Colocação
[6] Todos os Participantes
[0] Sair

\033[1;4;34m{'~'* 35}\033[m
'''
print(menu)
while True:
    o = str(input('\nInforme a opção desejada: ')).strip()
    print('')
    while o not in '0123456':
        o = str(input('Informe uma das opções do menu acima: ')).strip()
        print('')
    if o == '1':
        print('\033[1;4m{:~^35}\033[m\n'.format(' Classificação Geral '))
        for pos, t in enumerate(times):
            if pos < 4:
                print(f'\033[1;32m{pos + 1}º  {t}')
            elif pos < 16:
                print(f'\033[1;33m{pos + 1}º  {t}' if pos <= 8 else f'\033[33m{pos + 1}º {t}')
            else:
                print(f'\033[1;31m{pos + 1}º {t}')
        print(menu)

    if o == '2':
        print('\033[1;4m{:~^35}\n'.format(' Os Quatro primeiros Colocados '))
        for pos, t in enumerate(times[:4]):
            print(f'\033[1;32m{pos + 1}º {t}')
        print(menu)

    if o == '3':
        print('\033[1;4m{:~^35}\n'.format(' Os Quatro Últimos Colocados '))
        for pos, t in enumerate(times[len(times)-4:]):
            print(f'\033[1;31m{len(times)- 3 + pos}º {t}')
        print(menu)

    if o == '4':
        print('\033[1;4m{:~^35}\n\033[m'.format(' Colocação por Seleção'))
        seleção = str(input('Informe o nome da Seleção: ')).strip().capitalize()
        if seleção not in times2:
            while seleção not in times2 and seleção != '999':
                print('\n\033[1;31m{}\033[m'.format('_' * 70))
                print('\n{0}Desculpa, mas não encontramos a seleção que foi digitada.\n\n{1}Por Favor digite o nome da '
                      'seleção sem usar "ç" e sem usar acentos.{0}\n'
                      '\nEX: Para {2}"França"{0} escreva {2}"Franca"{0}, para {2}"Rússia"{0} escreva {2}"Russia"'
                      '\n{5}{3}{4}\n'.format('\033[1m', '\033[1;4;33m', '\033[1;35m', '_' * 70, '\033[m', '\033[1;31m'))
                seleção = str(input('Informe o nome da Seleção ou tecle \033[1;35m999'
                                    '\033[m para voltar: ')).strip().capitalize()
        if seleção in times2:
            colocação = times2.index(seleção) + 1
            if colocação <= 4:
                print(f'\n\033[1;32m{times[colocação -1]} ficou em {colocação}º colocado ao término da Copa do Mundo.')
            elif colocação <= 16:
                print(f'\n\033[1;33m{times[colocação -1]} ficou em {colocação}º colocado ao término da Copa do Mundo.')
            else:
                print(f'\n\033[1;31m{times[colocação -1]} ficou em {colocação}º colocado ao término da Copa do Mundo.')
        print(menu)

    if o == '5':
        print('\033[1;4m{:~^35}\033[m\n'.format('Seleção por Colocação'))
        colocação = str(input('Informe a colocação: ')).strip()
        coloc = int(colocação)
        while coloc > len(times) and colocação !='999':
            print('\033[1;31m{}\033[1m'.format('_' * 70))
            print(f'\nExistem apenas {len(times)} times na copa do mundo.')
            print('\033[1;31m{}\033[1m'.format('_' * 70))
            colocação = str(input(f'\nInforme uma posição menor que {len(times)}º ou 999 para voltar: '))
            coloc = int(colocação)
        if coloc <= 4:
            print(f'\033[1;32m\n{times[coloc - 1]} ficou em {colocação}º lugar.')
        elif coloc <= 16:
            print(f'\033[1;33m\n{times[coloc - 1]} ficou em {colocação}º lugar.')
        elif coloc <= len(times):
            print(f'\033[1;31m\n{times[coloc - 1]} ficou em {colocação}º lugar.')
        print(menu)

    if o == '6':
        print('\033[1;4m{:~^35}\033[1;37m\n'.format(' Todos os times da Copa do Mundo '))
        for t in sorted(times):
            print(t)
        print(menu)

    if o == '0':
        break
print('\n{:=^100}\n'.format(' Programa encerrado '))
print('\033[1;4;36m{:~^100}'.format(' Obrigado por utilizar a ACSistemas'))

# Desafio concluído.
