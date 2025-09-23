#!/usr/bin/env python

def implode(t: tuple[int]) -> int:
    n = 0
    for i in t:
        n = n*10 + i
    return n


if __name__ == "__main__":
    assert implode((1,2,3,4,5)) == 12345
    assert implode((9,9,8,7,0)) == 99870
