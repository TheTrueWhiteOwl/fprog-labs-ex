#!/usr/bin/env python

from ex03 import *

def area_coroa(r1: float, r2: float) -> float:
    if r1 > r2:
        raise ValueError("The inner circle entered was larger than the outer circle")
    return area_circulo(r2) - area_circulo(r1)

if __name__ == "__main__":
    print(area_coroa(3.0, 5.0))
    print(area_coroa(5.0, 3.0))
