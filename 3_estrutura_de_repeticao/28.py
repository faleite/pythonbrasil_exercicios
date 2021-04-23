"""
28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade
de CDs e o valor para em cada um.
"""
cd = int(input('Informe a quantidade de CDs: '))

v_total = 0
media = 0

for count in range(1, cd + 1):
    valor = float(input(f'Informe o valor do {count}º CD: '))
    v_total += valor
    media = v_total / cd

print(f'Valor total investido: $ {v_total:.2f}')
print(f'Valor médio gasto em cada CD: $ {media:.2f}')
