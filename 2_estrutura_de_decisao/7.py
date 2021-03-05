""" 7. Faça um Programa que leia três números
e mostre o maior e o menor deles.
"""

num1 = float(input(f'Insira o primeiro número: '))
num2 = float(input(f'Insira o segundo número: '))
num3 = float(input(f'Insira o terceiro número: '))

if num2 < num1 > num3:
    maior = num1
    if num2 > num3:
        menor = num3
    else:
        menor = num2
elif num1 < num2 > num3:
    maior = num2
    if num3 > num1:
        menor = num1
    else:
        menor = num3
else:
    maior = num3
    if num1 > num2:
        menor = num2
    else:
        menor = num1

print(f'O maior número é: {maior:.2f}')
print(f'O menor número é: {menor:.2f}')

""" Outra forma: """
# numeros = [num1, num2, num3]
#
# num_maior = max(numeros)
# num_menor = min(numeros)
#
# print(f'O maior número é: {num_maior:.2f}')
# print(f'O menor número é: {num_menor:.2f}')
