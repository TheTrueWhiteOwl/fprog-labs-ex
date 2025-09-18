#! /usr/bin/env python

num = int(input("Escreva um número: "))
soma = 0
while num > 0:
    num, ultimo_digito = divmod(num, 10)
    soma += ultimo_digito

print("A soma dos digitos é", soma)
