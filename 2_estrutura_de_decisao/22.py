"""
22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).
"""

numero = int(input(f'Insira um número inteiro: '))

par_impar = numero % 2

if par_impar == 0:
    print(f'{numero} é um número par.')
elif par_impar == 1:
    print(f'{numero} é um número impar.')
