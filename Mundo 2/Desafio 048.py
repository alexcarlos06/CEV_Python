# Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontrem no intervalo de 1 até 500

soma = 0     # Variável responsável pela somatória de todos os valores gerados através do laço de repetição
contador = 0 # Variável responsável peal contagem de todos os valores gerados através do laço de repetição
for c in range(1, 501,2): # Laço de repetição ( Para cada valor contido no intervalo entre 1 e 500 com o passo de 2 em 2)
    if c % 3 == 0: # Se o valor obtido a cada laço de repetição tiver o resultado do rsto da divisão igual a zero entao o valor é armazenado caso contrario não pe armazenado.
        soma = soma+c # Acumula (soma) todos os valores contidos através da estrutura condicional e o laço de repetição
        contador = contador +1 # Conta todos os valores gerados através do laço de repetição.
print('A soma dos {} valores impares contidos na sequência entre 1 e 500 é {}'.format(contador, soma)) # Usando o recurso do print no começo da instrução apenas os valores totais são gerados.