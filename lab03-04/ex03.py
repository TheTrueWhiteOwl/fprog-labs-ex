#!/usr/bin/env python

seconds: float = float(input("Escreva um numero de segundos? "))
minutes: float = seconds / 60
hours: float = minutes / 60
days: float = hours / 60
years: float = days / 365.25

print(f"{seconds:.2f} segundos equivale a {days:.2f} dias")
