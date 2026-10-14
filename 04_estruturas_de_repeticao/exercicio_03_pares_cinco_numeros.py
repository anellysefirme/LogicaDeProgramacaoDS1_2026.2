"""
EXERCÍCIO 03: Pares entre Cinco Números
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite 5 números inteiros ao usuário.
Utilize uma estrutura de repetição e um contador para verificar quantos números pares
foram digitados. Ao final, imprima a quantidade total.
"""

# TODO: Desenvolva o algoritmo abaixo:
# EXERCÍCIO 03: Pares entre Cinco Números

# Inicializa o contador de números pares
contador_pares = 0

# Laço de repetição para solicitar 5 números inteiros
for i in range(5):
    numero = int(input())
    
    # Verifica se o número digitado é par (resto da divisão por 2 igual a zero)
    if numero % 2 == 0:
        contador_pares += 1

# Imprime a quantidade total acumulada no contador
print(f"{contador_pares} valores pares")
