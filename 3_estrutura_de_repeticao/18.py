"""
18. Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.
"""

qtd_num = int(input('Insira a quantidade de números: '))

menor = 0
maior = 0
soma = 0
count = 1

while count <= qtd_num:
    num = int(input(f'Insira o {count}º número: '))
    if count == 1:
        menor = num
    if maior <= num:
        maior = num
    if menor >= num:
        menor = num
    count += 1
    soma += num

print(f'O menor valor é: {menor}')
print(f'O maior valor é: {maior}')
print(f'A soma da quantidade de números é: {soma}')
