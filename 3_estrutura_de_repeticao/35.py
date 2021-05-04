"""
35. Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário.
"""


def num_primo(num):
    lista = []
    for i in range(1, num + 1):
        count = 0
        for y in range(1, i + 1):
            if i % y == 0:
                count += 1
        if count == 2:
            lista.append(i)
    return lista


num = int(input('Insira um número: '))
print(num_primo(num))

