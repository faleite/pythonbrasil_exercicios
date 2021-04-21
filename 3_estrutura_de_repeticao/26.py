"""
26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

num_eleitores = int(input('Insira o número de eleitores: '))

cand_a = 0
cand_b = 0
cand_c = 0

i = 0

for i in range(num_eleitores):
    i += 1
    voto = str(input(f'Eleitor {i}, escolha um cadidato (A, B, ou C): ')).upper()
    if voto == 'A':
        cand_a += 1
    elif voto == 'B':
        cand_b += 1
    elif voto == 'C':
        cand_c += 1

print(f'Candidato "A" recebeu {cand_a} votos.')
print(f'Candidato "B" recebeu {cand_b} votos.')
print(f'Candidato "C" recebeu {cand_c} votos.')
