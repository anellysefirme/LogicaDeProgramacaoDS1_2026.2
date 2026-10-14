"""
EXERCÍCIO 03: Gerador de Alertas da Cagece
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Desenvolva um procedimento `emitir_alerta_fatura(nome_cliente, valor, data_vencimento)`
que imprima a mensagem:
"Prezado(a) [nome], sua fatura da Cagece no valor de R$ [valor] vence no dia [data]."
"""

# TODO: Desenvolva o procedimento abaixo:
# Definição do procedimento emitir_alerta_fatura
def emitir_alerta_fatura(nome_cliente, valor, data_vencimento):
    # Imprime a mensagem formatada com os dados recebidos
    print(f"Prezado(a) {nome_cliente}, sua fatura da Cagece no valor de R$ {valor:.2f} vence no dia {data_vencimento}.")

# Testes do procedimento com diferentes clientes
print("--- SISTEMA DE NOTIFICAÇÕES CAGECE ---")

# Teste 1: Cliente João
emitir_alerta_fatura("João Silva", 85.50, "15/11/2026")

# Teste 2: Cliente Maria
emitir_alerta_fatura("Maria Santos", 120.00, "20/11/2026")

# Teste 3: Cliente Carlos
emitir_alerta_fatura("Carlos Souza", 45.90, "22/11/2026")
