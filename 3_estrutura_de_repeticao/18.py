"""
18. Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.
"""

qtd_num = int(input('Insira a quantidade de números: '))

count = 1
maior = 0
menor = 0
soma = 0

while count <= qtd_num:
    n = int(input(f'Insira o {count}º número: '))
    if count == 1:
        menor = n
    if n >= maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    count += 1

print(f'O menor valor é: {menor}')
print(f'O maior valor é: {maior}')
print(f'A soma da quantidade de números é: {soma}')
