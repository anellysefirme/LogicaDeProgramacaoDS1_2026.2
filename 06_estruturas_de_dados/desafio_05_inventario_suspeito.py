"""
DESAFIO 05: O INVENTÁRIO SUSPEITO DO LABORATÓRIO
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
Elimine duplicatas usando conjuntos (set) e previna o erro KeyError em dicionários
usando o método .get().

SUA MISSÃO:
1. Obtenha a lista de itens únicos a partir de uma lista com duplicatas.
2. Consulte chaves no dicionário de forma segura sem quebrar o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:
# DESAFIO 05: O INVENTÁRIO SUSPEITO DO LABORATÓRIO

# 1. Criando uma lista com itens duplicados
inventario = ["Microscópio", "Notebook", "Teclado", "Notebook", "Mouse", "Teclado"]

# 2. Eliminando as duplicatas usando set
itens_unicos = set(inventario)

print("Inventário sem duplicatas:", itens_unicos)

# 3. Criando um dicionário com informações dos itens
laboratorio = {
    "Microscópio": 5,
    "Notebook": 3,
    "Teclado": 10,
    "Mouse": 8
}

# 4. Consultando chaves de forma segura usando get()
print("Quantidade de notebooks:", laboratorio.get("Notebook", "Item não encontrado"))

print("Quantidade de impressoras:", laboratorio.get("Impressora", "Item não encontrado"))