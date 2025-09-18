#!/usr/bin/env python

seconds: int = int(input("Escreva um numero de segundos? "))

dias, rest = divmod(seconds, 86400)
horas, rest = divmod(rest, 3600)
mins, segs = divmod(rest, 60)

print(f"dias: {dias}; horas: {horas}; mins: {mins}; segs: {segs}")
