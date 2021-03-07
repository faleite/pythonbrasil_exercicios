""" 9. Faça um Programa que leia três números
e mostre-os em ordem decrescente.
"""

num1 = int(input(f'Insira o primeiro número: '))
num2 = int(input(f'Insira o segundo número: '))
num3 = int(input(f'Insira o terceiro número: '))

numeros = [num1, num2, num3]
numeros.sort(reverse=True)

print(f'Ordem decrescente: {numeros}')
