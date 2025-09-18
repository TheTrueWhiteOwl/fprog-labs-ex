#!/usr/bin/env python

def media_digitos(num: int) -> float:
    if num < 0:
        raise ValueError("Esta funcao so aceita numeros naturais")
    soma_digitos: int = 0
    numero_digitos: int = 0
    while num > 0:
        num, digito = divmod(num, 10)
        soma_digitos += digito
        numero_digitos += 1
    return soma_digitos / numero_digitos

if __name__ == "__main__":
    print(media_digitos(12345))
