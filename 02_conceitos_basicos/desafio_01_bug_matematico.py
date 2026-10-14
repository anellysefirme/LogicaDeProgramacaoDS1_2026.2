"""
DESAFIO 01: O BUG MATEMÁTICO DA MÉDIA ESCOLAR
Disciplina: Lógica de Programação com Python
EEEP Professor Sebastião Vasconcelos Sobrinho

RELATÓRIO DA INVESTIGAÇÃO:
Um estagiário do sistema acadêmico tentou implementar o cálculo da média semestral
de um aluno, mas o sistema apresentou resultados bizarros devido a erros de tipagem
e precedência de operadores.

SUA MISSÃO:
1. Identifique e corrija os erros de tipagem (casting) e precedência.
2. Faça o programa calcular e exibir a média correta formatada com 1 casa decimal.
"""

# CÓDIGO ORIGINAL COM BUG (Analise e corrija):
# nota1 = input("Digite a primeira nota: ")
# nota2 = input("Digite a segunda nota: ")
# media = nota1 + nota2 / 2
# print("A média do aluno é:", media)

# TODO: Escreva aqui o código corrigido:
# CÓDIGO CORRIGIDO

# 1. Entrada de dados com a conversão de tipo (casting) para float
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# 2. Cálculo da média corrigindo a precedência com parênteses
media = (nota1 + nota2) / 2

# 3. Exibição da média formatada com 1 casa decimal (.1f)
print(f"A média do aluno é: {media:.1f}")
