"""
EXERCÍCIO 02: Tupla de Coordenadas e Imutabilidade
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma tupla com as cidades ("Tianguá", "São Benedito").
Tente alterar a posição 1 e use try-except para capturar o TypeError,
exibindo uma mensagem explicativa sobre imutabilidade.
"""

# TODO: Desenvolva o algoritmo abaixo:
# Criando uma tupla com as cidades
cidades = ("Tianguá", "São Benedito")
try:
    # Tentando alterar a posição 1 da tupla
    cidades[1] = "Ubajara" # type: ignore

except TypeError:
    print("Erro: Não é possível alterar os elementos de uma tupla, pois ela é imutável!")

# Exibindo a tupla original
print("Tupla de cidades:", cidades)