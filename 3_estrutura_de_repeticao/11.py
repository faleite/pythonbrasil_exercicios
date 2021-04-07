"""
11. Altere o programa anterior para mostrar no final a soma dos números.
"""

num1 = int(input(f'Insira o primeiro número: '))
num2 = int(input(f'Insira o segundo número: '))

soma = 0

for i in range(num1, num2):
    print(i)
    soma += i
print(f'A soma dos numeros é: {soma}')

