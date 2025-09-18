#!/usr/bin/env python

num = int(input("Escreva um inteiro: "))
num, ultimo_digito = divmod(num, 10)
zeros_seguidos = 0
while num > 0:
    num, digito = divmod(num, 10)
    if ultimo_digito == 0 and digito == 0:
        zeros_seguidos += 1
    ultimo_digito = digito

print("O número tem", zeros_seguidos, "zeros seguidos")
