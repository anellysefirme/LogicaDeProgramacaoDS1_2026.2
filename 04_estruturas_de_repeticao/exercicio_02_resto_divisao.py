"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
# EXERCÍCIO 02: Resto da Divisão por 5

# Leitura dos dois valores inteiros
X = int(input())
Y = int(input())

# Garante a ordem crescente definindo o menor e o maior valor para o intervalo
inicio = min(X, Y)
fim = max(X, Y)

# O laço percorre os números ENTRE X e Y (intervalo aberto, sem incluir as pontas)
for i in range(inicio + 1, fim):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
