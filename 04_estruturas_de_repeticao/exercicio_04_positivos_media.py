"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
# EXERCÍCIO 04: Positivos e Média

# Inicializa os contadores e acumuladores
quantidade_positivos = 0
soma_positivos = 0.0

# Laço para ler os 6 valores numéricos
for i in range(6):
    valor = float(input())
    
    # Verifica se o valor é estritamente positivo (> 0)
    if valor > 0:
        quantidade_positivos += 1
        soma_positivos += valor

# Imprime a quantidade de valores positivos
print(f"{quantidade_positivos} valores positivos")

# Se houver pelo menos um número positivo, calcula e exibe a média com 1 casa decimal
if quantidade_positivos > 0:
    media = soma_positivos / quantidade_positivos
    print(f"{media:.1f}")
