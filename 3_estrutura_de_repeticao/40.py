"""
40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:
a. Código da cidade;
b. Número de veículos de passeio (em 1999);
c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e. Qual a média de veículos nas cinco cidades juntas;
f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""

c_menor_acid = menor_acid = 0
c_maior_acid = maior_acid = 0

for i in range(1, 4):
    cid = int(input('Informe o código da cidade: '))
    veic = int(input('Informe o número de veículos de passeio: '))
    acid = int(input('Informe o número de acidentes de trânsito com vítimas: '))

    if i == 1:
        c_menor_acid = cid
        menor_acid = acid
    if acid > maior_acid:
        c_maior_acid = cid
        maior_acid = acid
    if acid < menor_acid:
        c_menor_acid = cid
        menor_acid = acid

print()
print(f'O maior índice de acidentes de transito é: {maior_acid}, e pertence a cidade: {c_maior_acid} ')
print(f'O menor índice de acidentes de transito é: {menor_acid}, e pertence a cidade: {c_menor_acid} ')
print()
print(f'Média de veículos nas cinco cidades juntas: ')
print(f'Média de acidentes de trânsito nas cidades com menos de 2.000: ')
