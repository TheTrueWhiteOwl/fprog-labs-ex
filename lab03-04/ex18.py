#! /usr/bin/env python

valor: float = float(input("Valor em EUR: "))
valor_cent: int = int(valor * 100)

notas_50, resto_cent = divmod(valor_cent, 5000)
notas_20, resto_cent = divmod(resto_cent, 2000)
notas_10, resto_cent = divmod(resto_cent, 1000)
notas_5, resto_cent = divmod(resto_cent, 500)
moeda_2, resto_cent = divmod(resto_cent, 200)
moeda_1, resto_cent = divmod(resto_cent, 100)
moeda_0_5, resto_cent = divmod(resto_cent, 50)
moeda_0_2, resto_cent = divmod(resto_cent, 20)
moeda_0_1, resto_cent = divmod(resto_cent, 10)
moeda_0_05, resto_cent = divmod(resto_cent, 5)
moeda_0_02, moeda_0_01 = divmod(resto_cent, 2)

print(f"""O valor {valor} equivale a:
    {notas_50} notas de 50 EUR
    {notas_20} notas de 20 EUR
    {notas_10} notas de 10 EUR
    {notas_5} notas de 5 EUR
    {moeda_2} moedas de 2 EUR
    {moeda_1} moedas de 1 EUR
    {moeda_0_5} moedas de 0.5 EUR
    {moeda_0_2} moedas de 0.2 EUR
    {moeda_0_1} moedas de 0.1 EUR
    {moeda_0_05} moedas de 0.05 EUR
    {moeda_0_02} moedas de 0.02 EUR
    {moeda_0_01} moedas de 0.01 EUR""")
