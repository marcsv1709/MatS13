# Solicita os dados de entrada do usuário
salario_fixo = float(input("Digite o salário fixo: R$ "))
comissao_por_carro = float(input("Digite a comissão por carro vendido: R$ "))
num_carros_vendidos = int(input("Digite o número de carros vendidos: "))

# Inicializa o total de vendas
total_vendas = 0.0

# Se o número de carros vendidos for maior que zero, solicita o total de vendas
if num_carros_vendidos > 0:
    total_vendas = float(input("Digite o valor total das vendas: R$ "))

# Calcula o salário final
salario_final = salario_fixo

if num_carros_vendidos > 0:
    salario_final += comissao_por_carro * num_carros_vendidos
    salario_final += 0.05 * total_vendas  # Adiciona 5% sobre o total de vendas
    if num_carros_vendidos > 10:
        salario_final += 0.10 * total_vendas  # Adiciona bônus de 10% sobre o total de vendas

# Exibe o salário final formatado com duas casas decimais
print(f"O salário final é: R$ {salario_final:.2f}")
