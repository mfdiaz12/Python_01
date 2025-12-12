###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("\nEjercicio 1")
##print("\nPor favor introducir 2 numeros")

## num1, num2 = input("Número 1 y numero 2\n").split() # Funciona pero con solo un digito
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"{num1} Es mayor que {num2}")
elif num1 == num2:
    print(f"{num1} en igual a {num2}")
else:
    print(f"{num1} es menor que {num2}")


#print("\nEjercicio 1:")
#num1 = int(input("Introduce el primer número: "))
#num2 = int(input("Introduce el segundo número: "))

#if num1 > num2:
    #print(f"{num1} es mayor que {num2}")
#elif num2 > num1:
    #print(f"{num2} es mayor que {num1}")
#else:
    #print("Los números son iguales")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

print("\nEjercicio 2")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = (input("Introduce la operacíon (+, -, *, /): "))

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = num1 / num2
else:
    print("Operación no válida.")

if 'resultado' in locals(): #Comprueba si la variable resultado existe.
    print(f"El resultado es: {resultado}") # type: ignore

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("\nEjercicio 3:")
anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0: # % signo de residuo, quiere decir que el residuo de la division sea 0
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")

# año % 4 == 0: El año debe ser divisible por 4 para ser potencialmente bisiesto.
# año % 100 != 0: Si el año es divisible por 100, no es bisiesto, a menos que....
# año % 400 == 0: ...también sea divisible por 400, en cuyo caso sí es bisiesto.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("\nEjercicio 4")

edad = int(input("Ingresa tu edad: "))

if 0 <= edad <= 2: # Se establece un rango si es mayor o igual que 0 la variable y menor igual que 2 
    print("Bebé") # Cambia la estructura no se pone primero la variable se deja en la mitad 
elif 3 <= edad <= 12: # Otra solucion - if edad >= 3 and edad <= 12: - esta fue la que inicialmente pense. 
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
else:
    print("Edad no válida.")