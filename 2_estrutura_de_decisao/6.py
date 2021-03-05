""" 6. Faça um Programa que leia
três números e mostre o maior deles
"""

num1 = float(input(f'Insira o primeiro número: '))
num2 = float(input(f'Insira o segundo número: '))
num3 = float(input(f'Insira o terceiro número: '))

if num2 < num1 > num3:  # num1 > num2 and num1 > num3:
    print(f'O maior número é: {num1:.2f}')
elif num1 < num2 > num3:
    print(f'O maior número é: {num2:.2f}')
else:
    print(f'O maior número é: {num3:.2f}')


""" Outra forma: """
# numeros = [num1, num2, num3]
#
# num_maior = max(numeros)
#
# print(f'O maior número é: {num_maior:.2f}')
