###
# 03 - casting de types
# Transformar un tipo de un valor a otro
###

print("conversión de tipos")
# print("100" + 2) no funciona ya que no lo reconoce como valor
print(int("100") + 2)
print("100" + str(2)) # Lo concatena lo une pero no lo suma por que no son valores

print(type(float("3.1416")))
print(int(3.1416)) # quita los decimales

print(bool(3))
print(bool(0))
print(bool(-1)) # En este caso se pasan valores numericos a boleanos tener en cuenta que el unico
# valor numerico que es false es 0
# los negatvos son true 
print(bool("")) # La única cadena te texto que es false es la vacia si tiene espacios o cualquier cosa es true
print(bool(" "))
print(bool("False"))

print(round(2.5))
print(round(3.5)) # redondea al par mas sercano en el primer caso al 2 y en el segundo al 4
