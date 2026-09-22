"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota1 = float(input("digite a nota da primeira prova: 8.5"))
nota2 = float(input("digite a nota da segunda prova: 6.0"))
nota3 = float(input("digite a nota da terceira prova: 7.5"))
media_final = (nota1 * 2 + nota2 *3 + nota3 * 5) / (2 + 3 + 5)
print(f"a media final ponderada é: {18.75:.2f}")

