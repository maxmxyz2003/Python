v_A = float(input())
v_B = float(input())
v_C = float(input())
if v_B != 0:
    if v_C != 0:
        resul1 = v_A / v_B + v_C
        resul2 = v_A / v_B - v_C
        print(resul1, resul2)
    else:
        resul1 = v_A / v_B
        print(resul1)
else:
    print("indefinido")
