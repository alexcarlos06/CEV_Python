'''Crie um programa que tenha uma tupla com várias palávras ( não usar acentos). Depos disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

nomes = ('Alex', 'Renato', 'Patricia', 'Jose', 'Nibera', 'Marcelina', 'Anusha', 'Secreto', 'Lourdes', 'Daniel', 'Beth',
         'Roberto', 'Tia Raimunda', 'Tiu David', 'Iurbe', 'Cinira',
         'Jandira', 'Ana Paula', 'Lorena', 'Tia Ka', 'Fabio')

vogais = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u')



# Este comando mostra todos os nomes em listas e quais vogais tem nos nomes, desta forma as vogais não são repetidas.
for pos, n in enumerate(nomes):
    print(f'\nO nome {n} tem as vogais : ', end='')

    for posv, v in enumerate(vogais):
        if v in nomes[pos]:
            print(f' "{v}"', end='')

print('')
