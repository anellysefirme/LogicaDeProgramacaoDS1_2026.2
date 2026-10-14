"""
EXERCÍCIO 05: Feliz Nataaal!
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba um número inteiro I (nível de empolgação).
Utilize repetição para exibir a frase "Feliz natal!" repetindo a letra 'a'
da palavra natal exatamente I vezes (ex: I=5 -> "Feliz nataaaal!").
"""

# TODO: Desenvolva o algoritmo abaixo:
# EXERCÍCIO 05: Feliz Nataaal!

# Recebe o nível de empolgação (número inteiro)
I = int(input())

# Cria a repetição da letra 'a' multiplicando a string pelo valor de I
letras_a = "a" * I

# Exibe a mensagem final montando a palavra com a quantidade correta de 'a'
print(f"Feliz nat{letras_a}l!")
