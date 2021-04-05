"""
10. Faça um programa que receba dois números inteiros
e gere os números inteiros que estão no intervalo compreendido por eles.
"""

num1 = int(input(f'Insira o primeiro número: '))
num2 = int(input(f'Insira o segundo número: '))

for i in range(num1, num2):
    print(i)

"""
Outra forma:
"""
# lista = list(range(num1, num2))
# print(lista)

