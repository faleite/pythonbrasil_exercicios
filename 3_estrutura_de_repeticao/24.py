"""
24. Faça um programa que calcule o mostre a média aritmética de N notas.
"""

n_notas = int(input('Insira o número de notas: '))

soma = 0
media = 0

for i in range(1, n_notas + 1):
    nota = float(input(f'Insira a {i}ª nota: '))
    soma += nota
    media = soma / n_notas

print(f'Média: {media:.1f}')
