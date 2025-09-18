#!/usr/bin/env python

salario_p_hora = float(input("Por favor indique o salário "))
horas = float(input("Por favor indique a quantidade de horas trabalhadas: "))

horas_normais = min(horas, 40.0)
horas_extraordinarias = max(0, horas - 40.0) 

salario = horas_normais*salario_p_hora + horas_extraordinarias*salario_p_hora*2

print(f"O ordenado por esta semana é {salario}")
