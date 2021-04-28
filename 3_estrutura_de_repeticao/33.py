"""
33. O Departamento Estadual de Meteorologia lhe contratou para
desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""

maior = 0
menor = 0
i = 1
soma = 0
print('Digite 00 para sair.')

while True:
    temp = float(input('Temperatura: '))
    if temp == 00:
        break
    if i == 1:
        menor = temp
    if temp > maior:
        maior = temp
    if temp <= menor:
        menor = temp
    i += 1
    soma += temp
    media = soma / (i - 1)

print()
print(f'Menor temperatura: {menor:.2f}')
print(f'Maior temperatura: {maior:.2f}')
print(f'Temperatura média: {media:.2f}')
