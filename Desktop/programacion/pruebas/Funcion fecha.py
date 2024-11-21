print("inicio")

def fecha_valida(dia, mes, año):
    if year%4==0 and year%100!=0 or year%400==0:
        if mes== (1,3,5,7,8,10,12):
            1<=dia<=31
        elif mes==(4,6,9,11):
            1<=dia<=30
        elif mes== 2:
            1<=dia<=29
    else:
         if mes== (1,3,5,7,8,10,12):
            1<=dia<=31
        elif mes==(4,6,9,11):
            1<=dia<=30
        elif mes== 2:
            1<=dia<=28
    
print("fin")