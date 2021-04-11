"""
12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""

num = int(input('Insira um número que deseja ver a tabuada: '))

for count in range(1, 11):
    print(f'{num} X {count} = {num * count}')


"""Com while"""
# count = 0
#
# while count < 10:
#     count += 1
#     tab = num * count
#     print(f'{num} X {count} = {tab}')
