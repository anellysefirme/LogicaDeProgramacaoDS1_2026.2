"""
EXERCÍCIO 05: Gestão de Escopo Global e Local
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Declare a variável global total_inscritos = 0.
Crie a função `inscrever_aluno(quantidade)` utilizando a diretiva `global`
para atualizar a variável. Demonstre o valor de total_inscritos antes e depois da chamada.
"""

# TODO: Desenvolva o algoritmo abaixo:
# Declarando a variável global conforme o enunciado
total_inscritos = 0

# Definição da função para inscrever novos alunos
def inscrever_aluno(quantidade):
    # A diretiva global avisa o Python para usar e modificar a variável criada fora da função
    global total_inscritos
    total_inscritos += quantidade
    print(f"[Função] Inscrição de {quantidade} aluno(s) realizada com sucesso.")

# ==========================================
# DEMONSTRAÇÃO DO ESCOPO DO PROGRAMA
# ==========================================
print("--- SISTEMA DE GESTÃO DE INSCRIÇÕES ---")

# 1. Demonstração do valor ANTES da chamada
print(f"Total de inscritos (ANTES da chamada): {total_inscritos}")
print("-" * 40)

# Executando a chamada da função para adicionar alunos
inscrever_aluno(5)

# 2. Demonstração do valor DEPOIS da chamada
print("-" * 40)
print(f"Total de inscritos (DEPOIS da chamada): {total_inscritos}")

# Nova chamada para mostrar a acumulação dos valores
print("\nRealizando mais uma inscrição...")
inscrever_aluno(3)
print(f"Total de inscritos atualizado: {total_inscritos}")
