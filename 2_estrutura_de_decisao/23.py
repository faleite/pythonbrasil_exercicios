"""
23. Faça um Programa que peça um número
e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
"""

numero = float(input(f'Insira um número: '))

if round(numero) == numero:
    print(f'{int(numero)} é um número inteiro.')
else:
    print(f'{numero} é um número decimal.')
