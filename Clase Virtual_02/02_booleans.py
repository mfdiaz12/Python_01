###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales en el control de flujo y la lógica en programación.
###

print("\nValores booleanos básicos:")
print(True)
print(False)

print("\nOperaciones de comparación")
print("5 > 3:", 5 > 3)          # True
print("5 < 3:", 5 < 3)          # False
print("5 == 5:", 5 == 5)        # True (igualdad)
print("5 != 3:", 5 != 3)        # type: ignore # True (desugualdad)
print("5 >= 5:", 5 >= 5)        # True (mayor o igual que)
print("5 <= 3:", 5 <= 3)        # False (desmenor o igual que)

print("\nComparariones de cadenas")
print("'Manzana' < 'Pera':", "Manzana" < "Pera") # True ya que lo hace por orden alfabetico y como la M esta primero que la P es true en caso de inicial por la misma letra evalua la siguiente
print("'Hola' == 'hola':", "Hola" == "hola") # type: ignore # False, ya que tambien es sensible a las mayusculas

print("\nOperadores Lógicos:")
print("True and True:", True and True)      # True
print("True and False:", True and False)    # False
print("True or False:", True or False)      # True
print("False or False:", False or False)    # False
print("not True:", not True)                # False
print("not False:", not False)              # True

print("\nTablas de la verdad")

print("\nand:")
print("A    B      A and B")
print("True True:", True and True)      # True
print("True False:", True and False)    # False
print("False True:", True and False)    # True
print("False False:", False and False)  # False

print("\nor:")
print("A    B      A or B")
print("True True:", True or True)      # True
print("True False:", True or False)    # False
print("False True:", True or False)    # True
print("False False:", False or False)  # False

print("\n not:")
print("A           not A")
print("True:", not True)        # False
print("False:", not False)      #True