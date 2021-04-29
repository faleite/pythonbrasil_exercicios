"""
35. Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário.
"""
num = int(input('Insira um número: '))

for n in range(1, num + 1):
    mult = 0
    for i in range(1, n + 1):
        if n % i == 0:
            mult += 1
    if mult == 2:
        print(f'{i} é um número primo')
    else:
        print(f'{i} não é um número primo')
