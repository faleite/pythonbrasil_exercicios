"""
23. Faça um programa que mostre todos os primos entre 1 e N
sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele
executou para encontrar os números primos. Serão avaliados o funcionamento,
o estilo e o número de testes (divisões) executados.
"""

n = int(input('Insira um número: '))

quant = 0

for num in range(1, n + 1):
    count = 0
    for i in range(1, num + 1):
        quant += 1
        if num % i == 0:
            count += 1

    if count <= 2:
        print(num)
print(quant)
