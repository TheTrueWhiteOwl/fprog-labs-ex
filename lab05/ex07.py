#!/usr/bin/env python

def validar_taxa_de_juros(j: float):
    if not isinstance(j, float):
        raise TypeError("A taxa de juros tem que ser um float")
    if j <= 0 or j >= 1:
        raise ValueError("A taxa de juros tem que ser um valor entre 0 e 1")

def validar_quantia_depositada(q: int):
    if not isinstance(q, int):
        raise TypeError("A quantia depositada deve ser um número inteiro")
    if q < 0:
        raise ValueError("A quantia depositada não pode ser negativa")

def validar_numero_anos(n: int):
    if not isinstance(n, int):
        raise TypeError("O número de anos deve ser um número inteiro")
    if n < 0:
        raise ValueError("O número de anos não pode ser negativo")


def valor(q: int, j: float, n: int) -> float:
    validar_taxa_de_juros(j)
    validar_quantia_depositada(q)
    validar_numero_anos(n)
    return q * (1 + j)**n

def duplicar(q: float, j: float) -> int:
    dinheiro: float = 0.0
    n: int = 0
    while dinheiro < 2*q:
       n += 1
       dinheiro = valor(q, j, n)
    return n


if __name__ == "__main__":
    print(valor(100, 0.03, 24))
    print(duplicar(100, 0.03))
