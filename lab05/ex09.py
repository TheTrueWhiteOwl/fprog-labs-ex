#!/usr/bin/env python

def dia_da_semana(dia: int, mes: int, ano: int) -> str:
    if mes < 1 or mes > 12:
        raise ValueError("Os meses apenas vao de 1 a 12")
    elif mes == 1 or mes == 2:
        mes += 12
        ano -= 1
    seculo, ano_seculo = divmod(ano, 100)
    int_dia_semana = cong_de_zeller(dia, mes, ano_seculo, seculo)
    return int_para_str_dia_semana(int_dia_semana)

def cong_de_zeller(q, m, K, J) -> int:
    return (q + int((13*(m + 1))/5) + K + int(K/4) + int(J/4) - 2*J) % 7

# A seguinte função pode ser escrita de forma muito melhor usando um tuplo
# (matéria da próxima aula)
def int_para_str_dia_semana(i: int) -> str:
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
    assert dia_da_semana(18, 1, 2014) == "sabado"
    assert dia_da_semana(21, 5, 2006) == "domingo"
