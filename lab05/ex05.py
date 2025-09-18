#!/usr/bin/env python

def bissexto(ano: int) -> bool:
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


if __name__ == "__main__":
    print(f"2024 = {bissexto(2024)}")
    print(f"2025 = {bissexto(2025)}")
    print(f"1200 = {bissexto(1200)}")
    print(f"1100 = {bissexto(1100)}")
