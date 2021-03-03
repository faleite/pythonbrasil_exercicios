""" 1. Faça um Programa que peça dois números e imprima o maior deles.
"""

num1 = float(input(f'Insira o primeiro número: '))
num2 = float(input(f'Insira o segundo número: '))

if num1 > num2:
    print(f'O número maior é: {num1:.2f}')
else:
    print(f'O número maior é: {num2:.2f}')

"""Outra forma:"""

# def maior(num1, num2):
#     if num1 > num2:
#         return num1
#     return num2
#
# numeros = [num1, num2]
# maior_num = maior(*numeros)
#
# print(f'O número maior é: {maior_num:.2f}')
