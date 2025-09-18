#! /usr/bin/env python

num = int(input("Escreva um inteiro positivo: "))
num_invert = 0
while num > 0:
    num, ultimo_digito = divmod(num, 10)
    num_invert = num_invert*10 + ultimo_digito

print("O número invertido é", num_invert)
