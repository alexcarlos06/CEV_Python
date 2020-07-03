'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''


par = list()
ex = str(input('\nInforme uma expressão a ser análisada: '))
valida = [1]
for c in range(0, len(ex)):
    if ex[c] == '(':
        par.append(ex[c])
    elif ex[c] ==')' and len(par) == 0:
       valida[0] = [0]
       break
    elif ex[c] == ')':
        par.pop()

print('Expressão válida.!' if valida[0]== 1 else 'Expressão inválida\nVerifique, pois faltou fechar algum dos parenteses.!')

#Desafio Concluído.