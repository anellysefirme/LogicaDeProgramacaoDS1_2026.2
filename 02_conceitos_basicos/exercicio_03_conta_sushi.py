"""
EXERCÍCIO 03: Conta do Nagoya Sushi House
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie um programa que:
1. Leia o valor total consumido no restaurante (em R$).
2. Aplique a taxa de 10% de serviço do garçom.
3. Exiba o valor final da conta a pagar com mensagem formatada.
"""

# TODO: Desenvolva o algoritmo abaixo:
valor_consumido=250.00
taxa_servico= valor_consumido * 0.10
valor_final= valor_consumido + taxa_servico
print (f"valor consumido: R$ {valor_consumido:float.f2}")
print (f"taxa de serviço (10%): R$ {taxa_servico:float.2f}")
print (f"valor final: R$ {valor_final:float.2f}")
