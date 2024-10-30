# Cálculo de Salário e Análise de Idades em Python

## Cálculo de Salário com Comissões

### Descrição
Este script solicita ao usuário o salário fixo, a comissão por carro vendido, o número de carros vendidos, e, caso aplicável, o valor total das vendas realizadas. Com essas informações, o programa calcula o salário final do vendedor, levando em consideração:
- **Comissão por Carro Vendido**: adicionada ao salário para cada carro vendido.
- **Bônus sobre Total de Vendas**: 5% de comissão sobre o valor total das vendas.
- **Bônus Adicional**: 10% de bônus sobre o valor total das vendas, se o vendedor tiver vendido mais de 10 carros.

# Tabela Verdade - Cálculo de Salário Final

| Salário Fixo (R$) | Comissão por Carro (R$) | Número de Carros Vendidos | Total de Vendas (R$) | Salário Final (R$) |
|-------------------|-------------------------|---------------------------|-----------------------|---------------------|
| 2000              | 200                     | 0                         | 0                     | 2000.00             |
| 2000              | 200                     | 5                         | 10000                 | 3500.00             |
| 2000              | 200                     | 15                        | 20000                 | 8000.00             |
| 2000              | 200                     | 5                         | 5000                  | 3250.00             |
| 3000              | 300                     | 0                         | 0                     | 3000.00             |
| 3000              | 300                     | 5                         | 15000                 | 5250.00             |
| 3000              | 300                     | 15                        | 25000                 | 11500.00            |
| 3000              | 300                     | 15                        | 0                     | 7500.00             |


## Análise de Idades


## Objetivo
Desenvolver um algoritmo que, ao receber as idades de dois homens e duas mulheres, seja capaz de:
1. Calcular a **soma das idades** do homem mais velho com a mulher mais nova.
2. Calcular o **produto das idades** do homem mais novo com a mulher mais velha.

Este exercício envolve lógica condicional e manipulação de variáveis para identificar e calcular as idades de interesse.

## Descrição do Problema
Em um estudo antropológico, busca-se relacionar variáveis demográficas seguindo uma regra específica: 
- Para o cálculo da idade total, é necessário **somar a idade do homem mais velho com a da mulher mais nova**.
- Também deve-se calcular o **produto entre a idade do homem mais novo e a idade da mulher mais velha**.

Esses cálculos podem revelar padrões de interação entre as idades, conforme as relações estabelecidas pelo estudo.

## Regras de Negócio

1. O algoritmo deve **identificar o homem mais velho e o homem mais novo**, assim como a **mulher mais velha e a mulher mais nova**, com base nas idades fornecidas.
2. A **idade do homem mais velho** deve ser **somada** à **idade da mulher mais nova**.
3. A **idade do homem mais novo** deve ser **multiplicada** pela **idade da mulher mais velha**.

# Tabela Verdade - Análise de Idades

| Idade Homem 1 | Idade Homem 2 | Idade Mulher 1 | Idade Mulher 2 | Homem Mais Velho | Homem Mais Novo | Mulher Mais Velha | Mulher Mais Nova | Soma das Idades | Produto das Idades |
|---------------|---------------|----------------|----------------|------------------|-----------------|-------------------|------------------|-----------------|---------------------|
| 30            | 25            | 22             | 30             | 30               | 25              | 30                | 22               | 52              | 750                 |
| 25            | 30            | 20             | 18             | 30               | 25              | 20                | 18               | 48              | 500                 |
| 40            | 20            | 30             | 35             | 40               | 20              | 35                | 30               | 70              | 700                 |
| 50            | 45            | 40             | 25             | 50               | 45              | 40                | 25               | 75              | 1800                |
| 18            | 20            | 50             | 40             | 20               | 18              | 50                | 40               | 60              | 900                 |
| 35            | 40            | 32             | 25             | 40               | 35              | 32                | 25               | 65              | 800                 |
| 60            | 50            | 21             | 30             | 60               | 50              | 30                | 21               | 81              | 1050                |
| 45            | 40            | 60             | 20             | 45               | 40              | 60                | 20               | 65              | 2400                |


