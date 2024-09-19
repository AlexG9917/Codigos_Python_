# print para imprimir mensaje que informe de que trata el programa.
# Recordar el uso de 3ple comillas para poder imprimir mensaje entre lineas sin necesidad de repetir codigo.

print ("""Calculadora de Area rectangular

Binvenido a Calculadora de Area Rectangular.
Para calcular el area de un rectangulo por favor introducir los datos correspondientes
como lo son medida de base y medida de altura en Metros.

Pero primero que nada introduce tu nombre para conocerte: """)

# Pedimos al usuario ingrasar el nombre.

nombre = input (" ")

#pedimos al usuario valor numerico de la base del rectangulo.

base = float(input( nombre + " por favor ingresa la base del rectángulo en metros : "))

# pedimos al usuario el valor numerico de la altura del rectangulo.

altura = float(input( nombre + " por favor ingresa la altura del rectángulo en metros: "))

# Calculamos el área del rectángulo utilizando los valores que el usuario le asigno a cada variable.

area = base * altura

# Verificamos las condiciones y mostramos el mensaje correspondiente

if area > 40 and altura > 10:
    print('''
Wow''', nombre, "¡El área del rectángulo es de", area, "metros cuadrados, osea que es mayor a 40 metros cuadrados y la altura es de", altura, "metros que es mayor a 10 metros!")
else:
    print('''
Vaya! , su area es de ''', area, " mts cuadrados y su altura es de", altura, "mts de altura, Impresionante!" )
