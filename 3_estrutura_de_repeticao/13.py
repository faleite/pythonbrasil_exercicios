"""
13. Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""

base = int(input(f'Isira o número base: '))
expoente = int(input(f'Isira o expoente: '))

potencia = 1
count = 1

while count <= expoente:
    count += 1
    potencia *= base

print(potencia)


"""Com for"""
# potencia = 1
#
# for count in range(expoente):
#     count += 1
#     potencia *= base
#
# print(potencia)
