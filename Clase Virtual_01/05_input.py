###
# 05 - Entrada de usuario (imput()) - versión simplificada
# La función input() permite obtener datos del usuario a travéz de la consola.
###

print("Hola, ¿como te llamas?")
nombre = input()

print(f"Hola {nombre}, escantado de conocerte")

# Para no hacerlo tan largo tambien funciona asi

nombre = input("Hola, ¿como te llamas?\n") # Si no pogo "/n" me queda en la misma linea

#  Existe algunos problemas al momento de solicitar otros datos ya que
#  Siempre todo lo que se pida en consola sera tomado como un str
#  Para pedir otro tipo se cecesita hacer la conversión.

age = input("¿Cuantos años tienes?\n")#Para hacer \ barrita se hace con option + ?
age = int(age) # Se cambia el tipo de age para que pueda volverlo un numero y pueda sumar
print(f"Dentro de 20 años tendras, {age + 20}")

# Puedo obtener varios datos

print("Obtener multiples valores a la vez")
country, city = input("¿En que pais y ciudad vives?\n").split() # Este split() lo que hace es detectar el espacio para asignar la cadena de texto 1 a la primra variable y la segunda (despues del espacio) asigna la segunda

print(f"vives en {country}, {city}")