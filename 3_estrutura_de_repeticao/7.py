"""
7. Faça um programa que leia 5 números e informe o maior número.
"""

maior = 0

for n in range(1, 6):
    numero = int(input(f'Insira o {n}º número: '))

    if n > maior:
        maior = n

print(f'{n} é o maior número.')
