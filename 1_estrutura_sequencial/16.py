""" 16. Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.
"""
# from math import ceil (pode usar método ceil de math para arredondar acima)

tamanho = float(input(f'Insira o tamanho da área: '))
litros = tamanho / 3
latas = int(litros / 18)  # ceil(tamanho / lata)
if litros % 18 != 0:
    latas += 1

preco = latas * 80

print(f'Quantidade de latas: {latas}')
print(f'Preço total: R$ {preco:.2f}')
