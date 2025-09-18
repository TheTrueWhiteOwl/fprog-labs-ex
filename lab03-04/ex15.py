#!/usr/bin/env python

num = int(input("Escreva um número: "))
capicua = num
while num > 0:
    num, ultimo_digito = divmod(num, 10)
    capicua = capicua*10 + ultimo_digito

print("A capicua do número é", capicua)
