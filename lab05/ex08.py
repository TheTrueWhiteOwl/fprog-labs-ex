#!/usr/bin/env python

def serie_geom(r: int, n: int) -> int:
    if n < 0:
        raise ValueError("O valor de n não pode ser negativo")
    serie: int = 1
    while n > 0:
        serie += r**n
        n -= 1
    return serie

if __name__ == "__main__":
    print(serie_geom(2, 4))
    print(serie_geom(100, 0))
    print(serie_geom(100, -1))
