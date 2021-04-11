"""
17. Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas
e os respectivos preços em 3 situações:
 - comprar apenas latas de 18 litros;
 - comprar apenas galões de 3,6 litros;
 - misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima,
isto é, considere latas cheias.
"""

M2_POR_LITRO = 6
LITRO_LATA = 18
VALOR_LATA = 80
LITRO_GALAO = 3.6
VALOR_GALAO = 25
MARGEM_FOLGA = 1.1

m2 = float(input('Insira o tamanho da área: '))
consumo_litro = m2 / M2_POR_LITRO * MARGEM_FOLGA

qtd_lata = int(consumo_litro / LITRO_LATA)  # Pode usar o metodo math.ceil que arredonda para cima
if consumo_litro % LITRO_LATA != 0:
    qtd_lata += 1
valor_lata = qtd_lata * VALOR_LATA

qtd_galao = int(consumo_litro / LITRO_GALAO)
if consumo_litro % LITRO_GALAO != 0:
    qtd_galao += 1
valor_galao = qtd_galao * VALOR_GALAO

qtd_lata_misto = int(consumo_litro / LITRO_LATA)
qtd_galao_misto = int((consumo_litro - qtd_lata_misto * LITRO_LATA) / LITRO_GALAO)
if consumo_litro % LITRO_GALAO != 0:
    qtd_galao_misto += 1
valor_galao_misto = qtd_galao_misto * VALOR_GALAO
valor_lata_misto = qtd_lata_misto * VALOR_LATA

print()
print('Apenas latas:')
print()
print(f'Quantidade de latas: {qtd_lata}')
print(f'Valor a pagar: R$ {valor_lata}')
print()
print('Apenas galões:')
print()
print(f'Quantidade de galões: {qtd_galao}')
print(f'Valor a pagar: R$ {valor_galao}')
print()
print('Compra mista:')
print()
print(f'Latas: {qtd_lata_misto}')
print(f'Galões: {qtd_galao_misto}')
print(f'Valor a pagar: R$ {valor_lata_misto + valor_galao_misto}')
