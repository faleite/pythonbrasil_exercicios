"""
35. Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário.
"""
num = int(input('Insira um número: '))

# for i in range(1, num + 1):
#     cont = 0
#     for n in range(1, i + 1):
#         if i % n == 0:
#             cont += 1
#     if cont == 2:
#         print(f'{n} é um número inteiro')
#     else:
#         print(f'{n} não é um número inteiro')


def num_primo():
    for i in range(1, num + 1):
        cont = 0
        for n in range(1, i + 1):
            if i % n == 0:
                cont += 1
        if cont == 2:
            print(f'{n} é um número inteiro')
        else:
            print(f'{n} não é um número inteiro')


num_primo()
