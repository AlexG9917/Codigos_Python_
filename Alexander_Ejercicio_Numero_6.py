# Iniciamos como es de costumbre, preguntandole al ususario sus datos personales.
# Y metemos un poco de labia XD.
nombre = input ('''Bienvenido a la Zapateria Rs21 Yuka y flan

En esta tienda encontraras los mejores precios del mercado, ademas estamos haciendo ofertas al mayor, muy llamativas.

Porfavor introduce tu nombre para registrarte en nuestra pagina.

Nombre: ''')

# Imprimimos un mensaje explicando como funciona el programa.
print ('''
Ok''', nombre, ''', Te cuento un poco sobre las ofertas que estamos haciendo.

Si tu compras más de diez unidades, se les dará un 10% de descuento sobre el total de la compra.
Si el número de unidades es mayor de veinte pero menor de treinta, se le otorga un 20% de descuento.
Y si son más treinta unidades se otorgará un 40% de descuento.

Y Sabes cual es la mejor parte?, El precio de cada unidad es de $80. Que baratooooooo

''')

# Precio por zapato.
pZapato = 80

# El usuario ingresa la cantidad de zapatos a comprar.

cZapatos = int(input(nombre + """ Por favor Ingresa las unidades que deseas comprar: """))

# Se ingresa el valor de cZapatos en tZapatos.

tZapatos = cZapatos

# Calculamos el descuento utilizando condicionales.

if 10 <= cZapatos < 20:
    descuento = 0.1

elif 20 <= cZapatos < 30:
    descuento = 0.2

elif cZapatos >= 30:
    descuento = 0.4

else:
    descuento = 0

# Calcular total con descuento.

tCompra = cZapatos * pZapato

tDescuento = tCompra * (1 - descuento)

# Imprimimos los resultados que deseamos.

print('''
Sr.''', nombre, ''' El total sin descuento es: $''', tCompra,

'''

Descuento es de : ''', descuento,

'''

El total con descuento es: $''',tDescuento )

respuesta = input ('''
Sr.'''+ nombre + ' Es una gran oferta no crees? : ')

# Utilizamos condicionales para que responda si quiere comprar o no

if respuesta == "si" :
    print ('''
Genial disfruta tu compra''', nombre )
elif respuesta == "no":
    print ('''
Conchale, quizas la proxima''')
else:
    print ('''
Respuesta no válida Sr.''', nombre, ". Por favor, ingresa 'Sí' o 'No'.")
