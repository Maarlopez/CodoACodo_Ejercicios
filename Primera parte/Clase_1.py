print("Hola mundo desde Python")

#Esto es un comentario

#Tipos de datos
cadena = "Hola mundo" #Cadena de texto (str)
entero = 78 #Entero (int)
real = 3.14 #Real (float)
booleano = True #Booleano (bool). Puede ser True o False
none = None #None (NoneType)

#cadena = 12 #cambio el valor y tipo de cadena

# Len(cadena)
print("La longitud de la cadena es:",len(cadena))
print(entero)
print(real)
print(booleano)
print(none)

# count(subcadena) 
# retorna el numero de veces que se repite una subcadena 
# dentro de la cadena de texto
print("La subcadena se repite la siguiente cantidad de veces:", cadena.count("a"))

# Capitalize()
# Retorna una copia de la cadena con el primer carácter en 
# mayúsculas y el resto en minúsculas
print("Imprimir en letra capital:",cadena.capitalize())

# title()
# Retorna la primera letra de cada palabra en mayúsculas 
# y el resto en minúsculas
print("Imprimir como titulo:",cadena.title())

# lower()
# Retorna una copia de la cadena de caracteres con todas 
# las letras en minúsculas
print("Imprimir todas las letras en minúsculas:",cadena.lower())

# upper()
# Retorna una copia de la cadena de caracteres con todas 
# las letras en mayúsculas
print("Imprimir todas las letras en minúsculas:",cadena.upper())

# isalpha()
#  Retorna True si todos los caracteres de la cadena son alfabéticos y hay,
# al menos, un caracter. En caso contrario, retorna False
print("Imprimir isalpha:",cadena.isalpha())

# isdigit()
# Retorna True si todos los caracteres de la cadena son digitos y hay,
# al menos, un caracter. En caso contrario, retorna False
print("Imprimir isdigit:",cadena.isdigit())

# endswitch(subcadena)
# Retorna True si la cadena finaliza con la subcadena pasada 
# como parametro
print("Imprimir endswitch:",cadena.endswith("o"))

# startswitch(subcadena)
#  Retorna True si la cadena inicia con la subcadena pasada
# como parametro
print("Imprimir startswitch:",cadena.startswith("H"))

# Extraer parte de una cadena
print(cadena[5:]) #desde la posición 5 hasta el final

# print(dir(cadena))

#____________________________________________________#

########### Conversión de tipos ###############
# edad = int(input('Ingrese su edad: '))
# print('Dentro de un año usted tendrá: ', edad+1)

# var = str(19)

# precio = float(input('Ingrese un precio: '))
# precio_final = precio * 0.9

# print('Precio final es ', precio_final)

###############################################

''' Comentario en bloque

print(type(cadena))
print(type(entero))
print(type(real))
print(type(booleano))
print(type(none))
'''