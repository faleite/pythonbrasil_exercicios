"""
13. Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7
"""

sexo = str(input('Insira seu sexo (M/F): '))
h = float(input('Insira sua altura: '))

if sexo == 'M':
    peso = (72.7 * h) - 58
else:
    peso = (62.1 * h) - 44.7

print(f'Seu peso ideal é: {peso:.3f}kg')
