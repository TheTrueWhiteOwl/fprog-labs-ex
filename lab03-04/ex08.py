#! /usr/bin/env python

while True:
    num = int(input("Escreva um número de segundos (um número negativo para terminar) "))
    if num < 0:
        break
    print(f"O número de dias correspondente é {num / (60*60*24)}")
