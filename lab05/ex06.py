#!/usr/bin/env python

from ex05 import bissexto

def dias_mes(mes: str, ano: int) -> int:
    if mes == "jan":
        return 31
    elif mes == "fev":
        if bissexto(ano):
            return 29
        else:
            return 28
    elif mes == "mar":
        return 31
    elif mes == "abr":
        return 30
    elif mes == "mai":
        return 31
    elif mes == "jun":
        return 30
    elif mes == "jul":
        return 31
    elif mes == "ago":
        return 31
    elif mes == "set":
        return 30
    elif mes == "out":
        return 31
    elif mes == "nov":
        return 30
    elif mes == "dez":
        return 31
    else:
        raise ValueError(f"Invalid Month: {mes}")

if __name__ == "__main__":
    print(dias_mes("fev", 2024))
    print(dias_mes("jan", 1972))
