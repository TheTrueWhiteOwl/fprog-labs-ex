#!/usr/bin/env python

PI = 3.14

def area_circulo(r: float) -> float:
    return PI * r**2

if __name__ == "__main__":
    print(f"Area de um circulo com raio 5 = {area_circulo(5.0)}")
