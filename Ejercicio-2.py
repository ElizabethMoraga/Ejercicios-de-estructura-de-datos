#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Elizabeth
#
# Created:     03/09/2023
# Copyright:   (c) Elizabeth 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Ejercicio 2
# Realizar una funcion que se llame area_circulo() que devuelva
# el area del circulo a partir de su radio.

# Se coloca lo solicitado, donde figure la funcion en este caso
# se multiplica el pi por el radio al cuadrado en
# el return esta el area del mismo circulo

def area_circulo(pi, radio):
    area=pi*radio**2
    return area

# Por pantalla sale el area solicitada,
print(area_circulo(3.14159, 10**2))




