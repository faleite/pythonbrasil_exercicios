"""
32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5!= 5.4.3.2.1=120
"""


def fatorial(num):
    print('{}!='.format(num), end=' ')
    f = 1
    for c in range(num, 0, -1):
        f *= c
        print(c, end='')
        print('.' if c > 1 else '=', end='')
    return f


n = int(input('Fatorial de: '))
print(fatorial(n))

"""Com while"""
# n = int(input('Fatorial de: '))
# f = 1
# print('{}!='.format(n), end=' ')
# while n > 0:
#     print(n, end='')
#     print('.' if n > 1 else '=', end='')
#     f *= n
#     n -= 1
# print(f)
