"""
8. Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

soma = 0

for i in range(1, 6):
    num = float(input(f'Insira o {i}º numero: '))
    soma += num

media = soma / 5

print(f'Soma dos números: {soma:.2f}')
print(f'Média dos números: {media:.2f}')
