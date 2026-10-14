"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:
# 1. Função para calcular o preço final com desconto e imposto
def calcular_preco_final(preco_base, taxa_desc, taxa_imp):
    # Aplica o desconto (ex: 10% de desconto -> multiplica por 0.90)
    preco_com_desconto = preco_base * (1 - taxa_desc)
    # Aplica o imposto sobre o valor já com desconto
    preco_final = preco_com_desconto * (1 + taxa_imp)
    return preco_final


# 2. Procedimento para exibir o relatório do item no terminal
def exibir_relatorio_item(numero_item, preco_final):
    print(f"| Item nº {numero_item:02d} | Preço Final: R$ {preco_final:.2f} |")


# 3. Teste das funções refatoradas
print("-" * 40)
print("       RELATÓRIO DE PREÇOS FINAIS       ")
print("-" * 40)

# Dados de teste (Preço Base, Desconto %, Imposto %)
itens_teste = [
    (100.00, 0.10, 0.05),  # Item 1: R$100, 10% desc, 5% imposto
    (250.50, 0.15, 0.08),  # Item 2: R$250.50, 15% desc, 8% imposto
    (50.00, 0.00, 0.12),   # Item 3: R$50, sem desc, 12% imposto
]

# Loop para processar e exibir cada item de forma dinâmica
for i, (preco, desc, imp) in enumerate(itens_teste, start=1):
    resultado = calcular_preco_final(preco, desc, imp)
    exibir_relatorio_item(i, resultado)

print("-" * 40)
