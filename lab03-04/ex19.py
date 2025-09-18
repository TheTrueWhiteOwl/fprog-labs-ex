#!/usr/bin/env python

n = 0
primeiro_termo = 0
while n < 9:
    n += 1
    primeiro_termo = primeiro_termo*10 + n
    print(primeiro_termo, "x 8 +", n, "=", primeiro_termo*8 + n)
