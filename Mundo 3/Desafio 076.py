print('''\nCrie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular''')

print('_' * 105)
print('')


lista = ('Camisa Polo', 100.00, 'Meia Soquete', 29.90, 'Cueca Box', 29.90, 'Sapatênis', 99.90, 'Calça Jeans',
         129.90, 'Calça Moleton', 99.90, 'Cueca Samba Canção', 19.90,
         'Saia Jeans', 199, 'Casaco de Pele', 1999)

print('-' * 40)
print('{:^40}'.format('Lista de Preços'))
print('-' * 40)
for pos, c in enumerate(lista):
    if pos % 2 == 0:
        asterisco = 28 - len(lista[pos])
        print('{}{}{}{:>4}{:>8.2f}'.format(lista[pos], 1 * ' ', '*' * asterisco, ' R$', lista[pos + 1]))

# Desafio Concluído