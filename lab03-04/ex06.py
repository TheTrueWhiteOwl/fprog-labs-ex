#! /usr/bin/env python

QUANTIDADE_NUMS = 3

i = 0
maior_num = float(input("Introduza um número: "))
while i < QUANTIDADE_NUMS - 1:
    num = float(input("Introdza outro número: "))
    maior_num = max(maior_num, num)
    i += 1

print(f"O maior número foi {maior_num}")
