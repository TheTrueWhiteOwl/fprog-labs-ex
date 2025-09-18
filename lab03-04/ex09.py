#!/usr/bin/env python

num = 0
while True:
    dig = int(input("Escreva um dígito (um número negativo para terminar) "))
    if dig < 0:
        break
    if dig // 10 != 0:
        raise ValueError("O número fornecido não é um dígito")
    num = num*10 + dig
print("O número é:", num)
