#!/usr/bin/env python

num_notas = int(input("Quantas notas de aluno vai introduzir? "))
i = num_notas
notas_positivas = 0
while i > 0:
    nota = int(input("Introduza a próxima nota: "))
    if nota < 0 or nota > 20:
        raise ValueError("A nota introduzida tem que ser de 0 a 20")
    if nota >= 10: # Eu não faço ideia o que é considerado nota positiva...
        notas_positivas += 1
    i -= 1

print("A quantidade de notas positivas é", notas_positivas)
print(f"A percentagem de notas positivas é {notas_positivas/num_notas:.0%}")
