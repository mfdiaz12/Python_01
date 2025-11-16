###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen siertas condiciones.
###

import os
os.system("clear") # con esto importamos un modulo de la biblioteca y lo que hace es limpiar cada que le damos play

print("Mi mensaje")

print("\n Sentencia simple condicional")

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicitaciones!")

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicitaciones!")

print("\n Sentencia simple condicional con else")
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n Sentencia simple condicional con elif")
nota = 7

if nota >= 9:
    print("¡Sobresaliente!") # Cuando la condicion se cumple ya no ejecuta los otros por eso se puede hacer asi y no establecer rangos
elif nota >= 7:
    print("¡Notable!")
elif nota >= 5:
    print("¡Aprobado!")
else:
    print("¡No estas calificado!")

print("\n Condiciones multiples")
edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puede manejar🚗")
else:
    print("POLICIA 🚓")
    
