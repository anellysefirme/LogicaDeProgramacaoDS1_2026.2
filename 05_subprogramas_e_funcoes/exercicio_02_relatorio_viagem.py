"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
# ==========================================
# 1. DEFINIÇÃO DAS FUNÇÕES (MÓDULOS)
# ==========================================

def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    """Calcula o custo total gasto com combustível na viagem."""
    litros_necessarios = distancia_km / consumo_kml
    custo_transporte = litros_necessarios * preco_combustivel
    return custo_transporte


def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    """Calcula o custo total de alimentação para todo o grupo."""
    custo_alimentacao = qtd_pessoas * dias * diaria_alimentacao
    return custo_alimentacao


# ==========================================
# 2. PROGRAMA PRINCIPAL
# ==========================================
print("--- SIMULADOR DE CUSTOS DE VIAGEM ---")

# Leitura dos dados de transporte
distancia = float(input("Distância total da viagem (em KM): "))
consumo = float(input("Consumo médio do veículo (KM por Litro): "))
preco_litro = float(input("Preço do litro do combustível: R$ "))

# Leitura dos dados de alimentação
pessoas = int(input("Quantidade de pessoas na viagem: "))
dias_viagem = int(input("Quantidade de dias de duração: "))
valor_diaria = float(input("Custo diário estimado de alimentação por pessoa: R$ "))

# Execução das funções e cálculos dos custos
custo_combustivel = calcular_custo_transporte(distancia, consumo, preco_litro)
custo_comida = calcular_custo_alimentacao(pessoas, dias_viagem, valor_diaria)
custo_total_viagem = custo_combustivel + custo_comida

# Exibição do relatório final formatado
print("\n" + "="*40)
print("          RELATÓRIO DE CUSTOS          ")
print("="*40)
print(f"Custo de Transporte:  R$ {custo_combustivel:.2f}")
print(f"Custo de Alimentação: R$ {custo_comida:.2f}")
print("-"*40)
print(f"CUSTO TOTAL ESTIMADO: R$ {custo_total_viagem:.2f}")
print("="*40)
