"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
# Definição da função calcular_pontuacao_total
def calcular_pontuacao_total(fase1, fase2, fase3):
    # Calcula a soma das pontuações das três fases
    pontuacao_total = fase1 + fase2 + fase3
    return pontuacao_total

# Testes da função com diferentes cenários de equipes
print("--- RELATÓRIO DE PONTUAÇÃO DAS EQUIPES ---")

# Teste 1: Equipe Alpha
pontos_alpha = calcular_pontuacao_total(85, 90, 95)
print(f"Equipe Alpha: {pontos_alpha} pontos")

# Teste 2: Equipe Beta
pontos_beta = calcular_pontuacao_total(70, 65, 80)
print(f"Equipe Beta: {pontos_beta} pontos")

# Teste 3: Equipe Gamma (com valores decimais)
pontos_gamma = calcular_pontuacao_total(92.5, 88.0, 99.1)
print(f"Equipe Gamma: {pontos_gamma:.1f} pontos")
