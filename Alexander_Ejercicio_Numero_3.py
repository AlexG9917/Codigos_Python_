print (""" Pagina Oficial del Banco Consolidado de la Republica.

Registro: """)

name = input('''
Nombre de ususario:''')

nGuardado = name

password = input("Contraseña: ")

# Registramos la contraseña en una variable.

cGuardada = (password)

print ('''
Registro exitoso''')

#solicitamos nombre al usuario al usuario.
nIntroducido = input('''
Nombre de ususario: ''')


# Solicitamos la contraseña al usuario.
cIntroducida = input("introduce la contraseña: ")

# Comparamos el usuario y las contraseñas utilizando las condicionales para validar o denegar el acceso.
if cIntroducida == cGuardada and nIntroducido == nGuardado:
    print("¡Contraseña y usuario correctos! Acceso concedido.")
    print ("""
Bienvenido al Banco Consolidado de la Republica

Estado de cuenta: 0,005Bs

""")
else:
    print("Usuario o Contraseña incorrecta. Acceso denegado.")
