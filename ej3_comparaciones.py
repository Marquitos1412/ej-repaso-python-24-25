#Raiz de 20
    #Importamos la funcion de la raiz cuadrada y calculamos la raiz de 20

from math import sqrt

raiz_20 = sqrt(20)

    #La comparamos con 5

comparacion_5 = raiz_20 > 5
print(f"¿Es la raiz de 20 mayor que 5?: {comparacion_5}")

    #La comparamos con 5 y con 4

comparacion_5_y_4 = 5 > raiz_20 > 4
print(f"¿Es la raiz de 20 mayor que 5?: {comparacion_5_y_4}")

#endregion

#region Circumferencia
    #Importamos el numero pi
from math import pi
    #Calculamos la longitud de las circunferencias de radios 5 y 0
longitud_circunferencia_radio_5 = 2 * pi * 5
longitud_circunferencia_radio_0 = 2 * pi * 0
    #Comparamos las longitud de radio 5 con 30
comparacion_longitud5 = longitud_circunferencia_radio_5 > 30
print(f"¿Es la longitud de la circunferencia de una esfera de radio 5 mayor que 30?: {comparacion_longitud5}")


#endregion 