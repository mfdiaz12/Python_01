###
# 04 - Variables
# Las variables sirven para guardar datos en memoria
# Python es un lenguaje de tipado dinámico y de tipado fuerte
###
# Asignar variable
# solo hace falta ponerle nombre

my_name = "Manuel"
print(my_name)

age = 32
print(age)

age = 40
print(age) # si reasigno la variable se imprimen las 2

# Tipado dinamico: el tipo de datose determina en tiempo de ejecución
# que no tiene que declararlo exlicitamente

name = "Manuel"
print(type(name))

name = 32
print(type(name))

#Tipado fuerte: Python no realiza conversiones de tipo automatica
#print(10 + "2")

print(f"Hola {my_name}, tengo {age} años")

# Casos no recomendados al momento de crear variables
# primeras correcta las demas mejor no

mi_nombe_de_variable_123 = "ok"
apellido = "ok"

MiNombreDeVariable = "ko"
minombredevariable = "ko"
# 123_mi_nombre = "ko" # No pueden iniciar con número
# mi-variable = "ko" # No recibe - ni espacios

# Ni variables con palabras reservadas como tru, false, print 

# Las constantes no existe en Python pero se simulam
# para este caso es normal utilizar UPERCASE

MI_CONSTANTE = 5

# Para dejar una nota de en la clase tipo que quiro la variable
# se puede hacer asi
 
is_user_logged_in: bool = True
print(is_user_logged_in)

is_user_logged_in = 42
print(is_user_logged_in) # Funciona pero me da una alerta que me avisa, para activar o desactivar la alerta ir a
# ">preferences" en la barra de busqueda, buscar "typecheck" y prenderlo.


