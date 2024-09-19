# El usuario ingresa sus datos personales en las variables mencionadas.

nombre = input('''Estimado usuario. Bienvenido a la plataforma de calculo porcentual de la empresa Hyserca.

Para verificar si su Proyecto es factible economicamente hablando y estar seguro de desarrollarlo, favor ingresar los siguientes datos.

Ingrese su nombre: ''')

# El usuario ingresa el nombre del proyecto.

nProyecto = input ('''
Ok ''' + nombre + ', ahora ingresa el nombre del proyecto que deseas desarrollar: ')


# Solicitamos al usuario ingresar el presupuesto y el precio del proyecto.

presupuesto = float(input('''
Ingresa el presupuesto del proyecto llamado ''' + nProyecto + ':'))

pProyecto = float(input('''
Ingrese el costo de desarrollo de ''' + nProyecto + ':'))

# Realizamos las operaciones necesarias para sacar el porcentaje requerido.

dPorcentual = ((pProyecto - presupuesto) / presupuesto) * 100

# Verificamos con las condicionales si la diferencia es menor al 75% del presupuesto

if dPorcentual < 75:
    print(nombre , 'La diferencia porcentual es de', dPorcentual,'%' ' Es decir, el proyecto es factible para ser desarrollado desde el punto de vista economico.')
else:
    print(nombre , 'La diferencia porcentual es de', dPorcentual,'%' ' El proyecto no es factible para ser desarrollado desde el punto de vista economico.')
