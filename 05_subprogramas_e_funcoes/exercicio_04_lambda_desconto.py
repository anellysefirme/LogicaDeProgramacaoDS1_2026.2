"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:
# Criação da função lambda de desconto
calcular_desconto_casas_paulino = lambda valor: valor * 0.85

# Testes da expressão lambda com valores de exemplo
print("--- SISTEMA DE VENDAS: CASAS PAULINO ---")

# Teste 1: Produto de R$ 100,00
preco_original_1 = 100.00
preco_final_1 = calcular_desconto_casas_paulino(preco_original_1)
print(f"Produto 1 -> De: R$ {preco_original_1:.2f} | À Vista (15% OFF): R$ {preco_final_1:.2f}")

# Teste 2: Produto de R$ 250,00
preco_original_2 = 250.00
preco_final_2 = calcular_desconto_casas_paulino(preco_original_2)
print(f"Produto 2 -> De: R$ {preco_original_2:.2f} | À Vista (15% OFF): R$ {preco_final_2:.2f}")

# Teste 3: Smartphone de R$ 1500,00 (executando direto no print)
print(f"Smartphone -> De: R$ 1500.00 | À Vista (15% OFF): R$ {calcular_desconto_casas_paulino(1500):.2f}")
