# print por defecto luego de escribir en pantalla su 
# argumento realiza un salto de linea

# print("Hola")
# print("Mundo")

# si quisieramos que los ponga en la misma linea separados 
# por un espacio podemos usar el parametro end y pasarle 
# como valor ese espacio

# print("Hola", end=" ")
# print("Mundo", end=" ")

nombre = "Yoselin"
profesion = "estudiante"
nacimiento = 2010

# print("Hola mi nombre es", nombre, "y soy", profesion, "naci en", nacimiento)

# print("Hola, mi nombre es {} y soy {} nací en {}".format(nombre, profesion, nacimiento))

# print(f"Hola, mi nombre es {nombre} y soy {profesion} nací en {nacimiento}")
 
 #Imprimo en bloque
# print(
#     f'''
#     Hola, mi nombre es {nombre} 
#     y soy {profesion} 
#     nací en {nacimiento}
#     '''
# )

######################################################################

salarioMensual = 3560
salarioDiario = salarioMensual/30

# print(f"Mi salario mensual es de {salarioMensual} y mi salario diario es de {salarioDiario}")

# print(f"Mi salario mensual es de {salarioMensual:.3f} y mi salario diario es de {salarioDiario:.2f}")

# con .3f le estoy diciendo "dejame 3 decimales"

numero = 0.123456789
# print(f'Formatear el valor con cuatro digitos: {numero:.4f}')
# print(f'Formatear el valor como un porcentaje: {numero:.2%}')
# print(f'Formato exponencial: {numero:e}')

# print(f"{'Opcion 1':20}{numero:5.2f}")
# print(f"{'Opcion 2':20}{numero:.2f}")


#Escapando caracteres

# print("Estoy 'trabajando'")
#print("Estoy "trabajando"") ERROR!
# print('Estoy "trabajando"')

# print("Estoy \"trabajando\"") LO QUE VIENE DESPUÉS DE LA 
#                               BARRA TOMALO COMO CADENA

# Nueva linea
print("Hola \nqué tal?")
# Tabulacion
print("Hola \tqué tal?")

#¿CÓMO REPETIR EL MISMO TEXTO?
print("Hola "*40)