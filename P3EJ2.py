import sys
#Pida al usuario el espacio recorrido por un coche y el tiempo que ha tardado en horas y que calcule
#a qué velocidad media había realizado el recorrido.
d = float(input("Escriba la distancia recorrida (en kilometros) "))
t = int(input("¿Cuanto tiempo ha tardado? (en horas) "))
#v = ((d/t)/1000)*60
v = d/t
print('La velocidad media es de ', v,)

sys.exit()
