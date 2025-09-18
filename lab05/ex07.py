#!/usr/bin/env python

def valor(q: float, j: float, n: int) -> float:
    if j <= 0 or j >= 1:
        raise ValueError("A taxa de juros tem que ser um valor entre 0 e 1")
    if q < 0:
        raise ValueError("A quantia depositada não pode ser negativa")
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
