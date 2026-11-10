# TODO: Crie o dicionário do veículo e percorra com for
veiculo = {}

# Escreva o laço for com .items()
# Criando o dicionário do veículo

veiculo = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2024
}

# Percorrendo o dicionário com .items()
for chave, valor in veiculo.items():
    print(f"{chave}: {valor}")