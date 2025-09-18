#!/usr/bin/env python

def dia_da_semana(dia: int, mes: int, ano: int) -> str:
    if mes < 1 or mes > 12:
        raise ValueError("Os meses apenas vao de 0 a 12")
    elif mes == 1 or mes == 2:
        mes += 12
        ano -= 1
    seculo, ano_seculo = divmod(ano, 100)
    int_dia_semana = cong_de_zeller(dia, mes, ano_seculo, seculo)
    return int_para_dia_semana(int_dia_semana)

def cong_de_zeller(q, m, K, J) -> int:
    return (q + int((13*(m + 1))/5) + K + int(K/4) + int(J/4) - 2*J) % 7

def int_para_dia_semana(i: int) -> str:
    if i == 0:
        return "sabado"
    elif i == 1:
        return "domingo"
    elif i == 2:
        return "segunda"
    elif i == 3:
        return "terca"
    elif i == 4:
        return "quarta"
    elif i == 5:
        return "quinta"
    elif i == 6:
        return "sexta"
    else:
        raise ValueError("O inteiro i tem que ser um valor de 0 a 6")

if __name__ == "__main__":
    print(dia_da_semana(18, 1, 2014))
    print(dia_da_semana(21, 5, 2006))
