#! /usr/bin/env python

num = int(input("Escreva um inteiro: "))
digitos_impares = 0
n = 0
while num > 0:
    num, ultimo_digito = divmod(num, 10)
    if ultimo_digito % 2 == 1:
        digitos_impares += ultimo_digito * 10**n
        n += 1
print("Resultado:", digitos_impares)
