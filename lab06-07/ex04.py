#!/usr/bin/env python

def filtra_pares(t: tuple[int]) -> tuple[int]:
    result = ()
    for i in t:
        if i % 2 == 0:
            result += (i,)
    return result

if __name__ == "__main__":
    assert filtra_pares((1,2,3,4,5,6,7,8,9)) == (2,4,6,8)
    assert filtra_pares((9,9,8,7,0)) == (8, 0)
