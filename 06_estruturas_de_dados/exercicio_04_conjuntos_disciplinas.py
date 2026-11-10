"""
EXERCÍCIO 04: Conjuntos (Set) de Disciplinas
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie 2 sets de estudantes (alunos_web e alunos_banco).
Calcule e imprima a Interseção (&) e a Diferença (-).
"""

# TODO: Desenvolva o algoritmo abaixo:
"""
EXERCÍCIO 04: Conjuntos (Set) de Disciplinas
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie 2 sets de estudantes (alunos_web e alunos_banco).
Calcule e imprima a Interseção (&) e a Diferença (-).
"""

# Criando os conjuntos de estudantes
alunos_web = {"Ana", "João", "Maria", "Pedro"}
alunos_banco = {"Maria", "Pedro", "Carlos", "Lucas"}

# Calculando a interseção
intersecao = alunos_web & alunos_banco

# Calculando a diferença
diferenca = alunos_web - alunos_banco

# Imprimindo os resultados
print("Interseção:", intersecao)
print("Diferença:", diferenca)