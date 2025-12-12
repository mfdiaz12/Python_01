###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

# Creación de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # Lista de enteros
lista2 = ["manzanas", "peras", "bananos", "maracuyas", "fresas"] # Lista de cadenas
lista3 = [1, "hola", 3.14, True] # type: ignore # Lista de tipos mixtos
#lista3: list[int | str | foat | bool] = [1, "hola", 3.14, True] # Lista de tipos mixtos forma correcta para que no salga error pero la otra funciona

lista_vacia = []
lista_de_listas = [[1, 2], [3, 4]]
matrix = [[1, 2], [3, 4], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

#Acceso a elementos por índice
print("\nAcceso a elementos por índice")
print(lista2[0]) # manzanas, el primer elemento es igual a 0
print(lista2[1]) # peras
print(lista2[-1]) # fresas, lo que hace con el - es que va al final y va restando asi podemos traer el ultimo elemento sin necesidad de saber en que posicion especifica esta
print(lista_de_listas[1][0]) # Esto primero entra a la lista en posicion 1 [3,4] y luego trae el elemento en posición 0 (3)

# Slicing (Rebanado)
print(lista1[1:4]) # [2, 3, 4] cuenta desde el inicio de la posición 1 que es el 2 hasta el inicio de la posicion 4 que es el 5 pero no lo incluye.
print(lista1[:3]) # [1, 2, 3] traigame de la lista hasta la tercera posición.
print(lista1[3:]) # [4, 5] trae de la tercera posicion en adelante
print(lista1[:]) # [1, 2, 3, 4, 5] trar una copia de toda la lista esto para poder modificar la copia.

# MAS MAGIA se puede usar otro parametro
#print(lista1[desde:hasta:paso])#

lista4 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista4[::2]) # Salta de 2 en 2 = [1, 3, 5, 7] 
print(lista4[::3]) # Salta de 3 en 3 = [1, 4, 7] 
print(lista4[::-1]) # Devuelve la lista en sentido contrario [8, 7, 6, 5, 4, 3, 2, 1]

# Modificar una lista
lista1[0] = 20 # Se define la lista y la posición que quiero cambiar luego = y asigno nuevo valor
print(lista1)

# Añadir alementos a la lista 2 formas
lista5 = [1, 2, 3]

lista5 = lista5 + [4, 5, 6] # Lo que hace es añadir crea una lista a la que le añade estos valores
print("Lista 5 contiene:",(lista5))

# Forma corta y mas eficiente ya que lo que hace es directamente modificar la lista 
lista5 += [7, 8, 9]
print("Lista 5 contiene:",(lista5))

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

print("\nEjercicio 1:")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
#print(mensaje[7:]) Esta fue mi solución no es la más correcta pero funciona
secreto = mensaje[7:] # En este caso se define una variable para secreto con eso se hace aparte de mensaje
print(secreto)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
#numeros[0] = 50 funciona pero nuevamente no es la mejor
#numeros[4] = 10 funciona pero nuevamente no es la mejor
numeros[0], numeros[-1] = numeros[-1], numeros[0] # Intercambio en una sola línea, identifica los 2 campos
print(numeros)                                    # Luego les dice que = y los invierte.



# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
#pan = ["pan arriba"]
#ingredientes = ["jamón", "queso", "tomate"]
#pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
print("\nEjercico 3:")
sandwich = pan + ingredientes + pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

print("\nEjercio 4:")
lista = [1, 2, 3]
lista_duplicada = lista + lista
print(lista_duplicada)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

print("\nEjercicio 5:")
lista = [10, 20, 30, 40, 50]
centro = len(lista) // 2
print(lista[centro])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

print("\nEjercicio 6:")
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]
print(lista_invertida) #Este si no tenia ni idea
