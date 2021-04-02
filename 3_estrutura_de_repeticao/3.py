"""
3. Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
"""

print('Preencha os dados abaixo.')

while True:
    nome = str(input(f'Nome: '))
    if len(nome) > 3:
        break
    else:
        print('Valor inválido')

while True:
    idade = int(input(f'Idade: '))
    if 0 < idade <= 150:
        break
    else:
        print('Valor inválido')

while True:
    salario = float(input(f'Sálario: '))
    if salario > 0:
        break
    else:
        print('Valor inválido')

while True:
    sexo = str(input(f'Sexo (F-Feminino, M-Masculino): ')).upper()
    if sexo in 'FM':
        break
    else:
        print('Valor inválido')

while True:
    estado_civil = str(input(f'Estado Civil (S-Solteiro, C-Casado, V-Viúvo, D-Divorciado): ')).upper()
    if estado_civil in 'SCVD':
        break
    else:
        print('Valor inválido')
