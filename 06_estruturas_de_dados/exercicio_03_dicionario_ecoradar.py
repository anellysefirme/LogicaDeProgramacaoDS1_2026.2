"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Estruture um dicionário com 3 membros (matrícula -> cargo).
Leia uma matrícula via terminal e exiba a função correspondente cadastrada.
"""

# TODO: Desenvolva o algoritmo abaixo:
# Dicionário da equipe EcoRadar
equipe = {
    "101": "Desenvolvedor",
    "102": "Analista de Sistemas",
    "103": "Gerente de Projeto"
}

# Solicita a matrícula ao usuário
matricula = input("Digite sua matrícula: ")

# Verifica se a matrícula está cadastrada
if matricula in equipe:
    print("Cargo correspondente:", equipe[matricula])
else:
    print("Matrícula não encontrada!")