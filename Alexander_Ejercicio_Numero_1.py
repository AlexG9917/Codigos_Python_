# Hello, principalmente declaramos la variable "nombre" utilizando input para que el usuario pueda introducir su nombre.
nombre = input ("Introduce tu nombre:")
# Una vez introducido el nombre este se guardara en la variable ya mencionada "nombre" y este lo utilizaremos el el pritf para que el usuario se sienta mas cercano con el programa.
# Recordar que utilizamos 3ple comillas para que podamos imprimir texto entre lineas.
print ("""
Hola""",nombre,"""Espero te encuentres bien :)

¿Me indicas tu edad para saber si eres mayor o menor de edad?:""")
# solicitamos la edad de el ususario.
edad = int(input (" "))
# utilizamos las condicionales para ejecutar los procesos necesarios.
if edad < 18:
    print("""
OH, tienes""", edad, "Años, eres menor de edad.")
else:
        print ("""
OK que bueno, tienes""", edad, """ Años eso quiere decir que eres mayor de edad.""")
# listo el pollo.
