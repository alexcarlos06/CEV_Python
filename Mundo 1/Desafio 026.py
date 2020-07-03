# Faça um programa que leia uma frase pelo teclado e mostre
#quantas vezes aparece a letra desejada e em que posição ela aparece a primeira vez e em que posição ela aparece a úlitma vez

# Lendo o nome informado excluindo os espaços do inicio e do final da frase e transformando todos os caracteres da sting em letra maiuscula e retirando os espaços digitados no inicio e no final da frase
# Lendo a letra a ser procurada dentro da frase e retirando os espaços antes e depois da letra
f = str(input('Digite uma frase: ')).upper().strip()
c = str(input('Qual letra deseja contar dentro da frase? ')).upper().strip()

# Mostrando na tela os resultados obtidos
print('Foram encontradas "{1}" letras "{0}" dentro da frase.\nA letra "{0}" aparece na {2}º posição e por último na {3}º posição".'.format(c, f.count(c), f.find(c)+1,f.rfind(c)+1))

#Desafio concluído