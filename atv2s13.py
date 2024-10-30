def leia_idade(mensagem):
    while True:
        try:
            idade = int(input(mensagem))
            if idade <= 0:
                print("A idade deve ser um número inteiro positivo. Tente novamente.")
            else:
                return idade
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro positivo.")

# Leitura das idades dos homens
print("Digite as idades dos dois homens:")
idade_homem1 = leia_idade("Idade do primeiro homem: ")
idade_homem2 = leia_idade("Idade do segundo homem: ")

# Leitura das idades das mulheres
print("\nDigite as idades das duas mulheres:")
idade_mulher1 = leia_idade("Idade da primeira mulher: ")
idade_mulher2 = leia_idade("Idade da segunda mulher: ")

# Identificando o homem mais velho e o mais novo
if idade_homem1 >= idade_homem2:
    homem_mais_velho_idade = idade_homem1
    homem_mais_velho_label = "primeiro homem"
    homem_mais_novo_idade = idade_homem2
    homem_mais_novo_label = "segundo homem"
else:
    homem_mais_velho_idade = idade_homem2
    homem_mais_velho_label = "segundo homem"
    homem_mais_novo_idade = idade_homem1
    homem_mais_novo_label = "primeiro homem"

# Identificando a mulher mais velha e a mais nova
if idade_mulher1 >= idade_mulher2:
    mulher_mais_velha_idade = idade_mulher1
    mulher_mais_velha_label = "primeira mulher"
    mulher_mais_nova_idade = idade_mulher2
    mulher_mais_nova_label = "segunda mulher"
else:
    mulher_mais_velha_idade = idade_mulher2
    mulher_mais_velha_label = "segunda mulher"
    mulher_mais_nova_idade = idade_mulher1
    mulher_mais_nova_label = "primeira mulher"

# Cálculo da soma e do produto conforme as regras
soma_idades = homem_mais_velho_idade + mulher_mais_nova_idade
produto_idades = homem_mais_novo_idade * mulher_mais_velha_idade

# Exibição dos resultados
print(f"\nO homem mais velho é o {homem_mais_velho_label} com {homem_mais_velho_idade} anos.")
print(f"O homem mais novo é o {homem_mais_novo_label} com {homem_mais_novo_idade} anos.")
print(f"A mulher mais velha é a {mulher_mais_velha_label} com {mulher_mais_velha_idade} anos.")
print(f"A mulher mais nova é a {mulher_mais_nova_label} com {mulher_mais_nova_idade} anos.")

print(f"\nSoma das idades do homem mais velho e da mulher mais nova: {soma_idades}")
print(f"Produto das idades do homem mais novo e da mulher mais velha: {produto_idades}")
