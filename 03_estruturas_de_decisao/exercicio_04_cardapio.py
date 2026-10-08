"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
codigo = int(input("digite o codigo do item: "))
quantidade = int(input("digite a quantidade: "))
if codigo == 1:
    total = quantidade * 4.00
elif codigo == 2:
    total = quantidade * 4.50
elif codigo == 3:
    total = quantidade * 5.00
elif codigo == 4:
    total = quantidade * 2.00
elif codigo == 5:
    total = quantidade * 1.50
    print(f"Total: R$ {total:.2f}")
else:
    print("Código inválido!")
    print(f"Total: R$ {total:.2f}")
