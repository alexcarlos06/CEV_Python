# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


from datetime import date

contagem = 0
maioridade = 21
ano = date.today().year
print('')
reg = int(input('Informe quantos anos de nascimento deseja análisar: '))
if reg <= 0:
    print('Digite um valor maior que "1" para ser análisado.')
    exit()
for n in range(0, reg):
    nasc = int(input('Informe o ano de nascimento: '))
    idade = ano - nasc
    if idade > maioridade:
        contagem += 1
print('{}'.format('*' * 50))


if contagem == 0:
    print('De todas as dastas de nascimento das pessoas informadas nenhuma completou a maior idade que é de {} anos'.format(maioridade))
elif contagem == 1:
    print('Apenas uma pessoa completou a maior idade que é de {} anos.'.format(maioridade))
else:
    print(''
          '\nForam informados {} datas de nascimento.'
          '\n{} Pessoas atingiram a maioridade e '
          '{} Pessoas não atingiram a maioridade.'.format(reg,contagem, reg - contagem))

    # Desafio Concluído.