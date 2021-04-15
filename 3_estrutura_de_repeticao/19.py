"""
19. Altere o programa anterior para que ele
aceite apenas números entre 0 e 1000.
"""

qtd_num = int(input('Insira a quantidade de números: '))

menor = 0
maior = 0
soma = 0
count = 1

while count <= qtd_num:
    num = int(input(f'Insira o {count}º número: '))
    if num < 0 or num > 1000:
        print('Número inválido, insira um número entre 0 e 1000')
    else:
        if count == 1:
            menor = num
        if num >= maior:
            maior = num
        if num < menor:
            menor = num
        soma += num
        count += 1

print(f'O menor valor é: {menor}')
print(f'O maior valor é: {maior}')
print(f'A soma da quantidade de números é: {soma}')
