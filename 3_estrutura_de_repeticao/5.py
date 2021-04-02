"""
5. Altere o programa anterior permitindo ao usuário informar
as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""
a = 0
b = 0
taxa_a = 0
taxa_b = 0
anos = 0

while a < 1:
    a = int(input('Infrome a quantidade de habitantes do país A: '))
    if a < 1:
        print('Valor inválido, tente novamente.')

while taxa_a <= 0:
    taxa_a = float(input('Informe a taxa de crescimento do país A: '))  # 3%
    if taxa_a <= 0:
        print('Valor inválido, tente novamente.')

while b < a:
    b = int(input('Infome a quantidade de habitantes do país B: '))  # 200000
    if b < a:
        print('Valor inválido, tente novamente.')

while taxa_b <= 0:
    taxa_b = float(input('Informe a taxa de crescimento do país B: '))  # 1.5%
    if taxa_b > taxa_a:
        print('Valor inválido, tente novamente.')

while a <= b:
    a = (a * taxa_a / 100) + a
    b = (b * taxa_b / 100) + b
    anos += 1

print(f'Em {anos} anos a população do país A será maior que a população do país B.')
