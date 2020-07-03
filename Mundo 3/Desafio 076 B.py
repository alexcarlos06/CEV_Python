print('''\nCrie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular''')
from tabulate import tabulate
print('_' * 105)
print('')


lista = [['Camisa Polo', 100.00], ['Meia Soquete', 29.90], ['Cueca Box', 29.90], ['Sapatênis', 99.90], ['Calça Jeans', 129.90], ['Calça Moleton', 99.90], ['Cueca Samba Canção', 19.90]]
cabeçalho = ['Produto', 'Preço']
print(tabulate(lista, cabeçalho, tablefmt='psql'))