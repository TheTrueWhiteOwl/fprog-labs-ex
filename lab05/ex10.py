#!/usr/bin/env python

def diferenca(a: float, b: float) -> float:
    return a - b if a > b else b - a

def inverso(num: int) -> int:
    if num < 0:
        raise ValueError("Esta funcao apenas aceita valores positivos")
    num_i = 0
    while num > 0:
        num, resto = divmod(num, 10)
        num_i *= 10
        num_i += resto
    return num_i


def misterio(num: int) -> int:
    if num > 999 or num < 100:
        raise ValueError("Apenas aceita números de três digitos")
    elif diferenca(num // 100, num % 10) < 1:
        raise ValueError("A diferenca entre o primeiro e ultimo digito tem que ser maior que 1")
    
    n_s = diferenca(num, inverso(num))
    n_s_i = inverso(n_s)

    return n_s + n_s_i

if __name__ == "__main__":
    print(diferenca(2,1))
    print(diferenca(1,2))
    print(inverso(123456789))
    print(misterio(358))
    print(misterio(981))

# Too lazy para explicar o misterio :c

