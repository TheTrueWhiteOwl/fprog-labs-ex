#!/usr/bin/env python

n = int(input("Numerator: "))
d = int(input("Denominator: "))

result = 0
while n > d:
    n -= d
    result += 1

print("Resultado:", result)
