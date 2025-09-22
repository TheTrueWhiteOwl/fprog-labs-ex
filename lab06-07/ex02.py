#!/usr/bin/env python

def explode(n: int) -> tuple[int]:
    n_exploded = ()
    while n > 0: 
        n, last_digit = divmod(n, 10)
        n_exploded = (last_digit,) + n_exploded
    return n_exploded

if __name__ == "__main__":
    assert explode(12345) == (1, 2, 3, 4, 5)
    assert explode(99870) == (9, 9, 8, 7, 0)
