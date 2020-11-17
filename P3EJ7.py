# Pida al usuario tres número que serán el día, mes y año. Comprueba que la fecha
# introducida es válida.  Por ejemplo:
# 32/01/2017->Fecha incorrecta
# 29/02/2017->Fecha incorrecta
# 30/09/2017->Fecha correcta.
# Tienen 31 días: Enero, marzo, mayo, julio, agosto, octubre y diciembre.
# Tienen 30 días: Abril, junio, septiembre y noviembre.
# Tienen 28 días: Febrero.
dia = int(input("Digame un día "))
mes = int(input("Digame un mes "))
año = int(input("Digame un año "))

if (dia == 31) and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 9 or mes == 12):
    print('La fecha', dia, '/', mes, '/', año, 'es correcta')
elif (dia == 30) and (mes == 4 or mes == 6 or mes == 10 or mes == 11):
    print('La fecha', dia, '/', mes, '/', año, 'es correcta')
elif dia == 28 and mes == 2:
    print('La fecha', dia, '/', mes, '/', año, 'es correcta')
else:
    print('La fecha', dia, '/', mes, '/', año, 'es incorrecta')
