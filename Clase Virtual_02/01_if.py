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
edad = 17
tiene_carnet = True

if edad >= 18 and tiene_carnet: # Tiene que cumplir las 2 condiciones para que sea true
    print("Puede manejar🚗")
else:
    print("POLICIA 🚓")

if edad >= 18 or tiene_carnet: # Con que una de las 2 condiciones se cumpla ya la sentencia es true
    print("Puedes conducir en la Isla Margarita🚗")
else:
    print("Paga al policia y de deja conducir")

es_fin_de_semana = False
if not es_fin_de_semana: # El not nos sirve para darle la vuelta a la condición si cambia la condicion a True no imprime nada
    print("Venga vamos a trabajar")

print("\n Anidar condicionales") # Poner un condicional dentro de otro, a mas condicionales internos mas complejo es el codigo.
edad = 20 # lo mprimero que evalua es si tienes la edad y luego si tienes dinero.
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la farra")
    else:
        print("Quedate en casa")
else:
    print("No puedes entrar a la disco")

# Intentar simplificar, es este caso seria asi mas facil
 
if edad <= 18:
    print("No pueds ir a la farra")
elif tiene_dinero:
    print("Puedes ir a la discoteca")
else:
    print("Quedate en casa")