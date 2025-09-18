#!/usr/bin/env python

n_max = int(input("Qual o valor de n? "))
x = int(input("Qual o valor de x? "))

n = 1
factorial = 1
soma = 1
while n <= n_max:
    factorial *= n
    soma += x**n / factorial
    n += 1
print("O valor da soma é", soma)
