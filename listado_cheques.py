import csv
import sys
import datetime

#Se definen variables para filtrar las filas del archivo según distintos argumentos

def buscarPorDniTipo():
    '''Devuelve una lista con los resultados de filtrar 
    las filas del archivo por los argumentos dni y tipo de cheque.'''
    
    resultado = []
    with open(archivo, 'r', newline='') as file:
        reader = csv.reader(file)
        resultado.append(next(reader, None))
        for fila in reader:
            if dni==fila[8] and tipoCheque==fila[9]:
                resultado.append(fila)
    return resultado

def buscarPorDniTipoEstado():
    '''Devuelve una lista con los resultados de filtrar 
    las filas del archivo por los argumentos dni, tipo de cheque y estado de cheque.'''
    
    resultado = []
    with open(archivo, 'r', newline='') as file:
        reader = csv.reader(file)
        resultado.append(next(reader, None))
        for fila in reader:
            if dni==fila[8] and tipoCheque==fila[9] and estadoCheque==fila[10]:
                resultado.append(fila)
    return resultado

def cambiarFecha():
    '''Cambia las fechas de formato string a timestamp, 
    además separa las fechas'''

    fechasIngresadas = rangoFecha.split(':')
    fechaSalida = []
    for fecha in fechasIngresadas:
        #Cambia formato string a formato fecha
        formatoFecha = datetime.datetime.strptime(fecha, '%d-%m-%Y')
        #Cambia formato fecha a timestamp en segundos enteros
        timestamp = int(datetime.datetime.timestamp(formatoFecha))
        fechaSalida.append(timestamp)
    return fechaSalida

def buscarPorDniTipoFecha():
    ''' Devuelve una lista con los resultados de filtrar las filas 
    del archivo por los argumentos fecha, dni y tipo de cheque.
    Usa la funcion para tener la fecha ingresada en formato timestamp entero.'''
    
    fechas = cambiarFecha()
    fechaUno = fechas[0]
    fechaDos = fechas[1]
    #filtra las filas
    resultado = []
    with open(archivo, 'r') as file:
        reader = csv.reader(file)
        resultado.append(next(reader, None))
        for fila in reader:
            if fechaUno<int(fila[6]) and fechaDos>int(fila[6]) and dni==fila[8] and tipoCheque==fila[9]:
                resultado.append(fila)
    return resultado

def buscarPorDniTipoEstadoFecha():
    '''Devuelve una lista con los resultados de
    filtrar las filas del archivo por los argumentos fecha, dni, tipo de cheque y estado de cheque.
    Cambia las fechas de formato string a timestamp.'''

    fechas = cambiarFecha()
    fechaUno = fechas[0]
    fechaDos = fechas[1]
    #filtra las filas
    resultado = []
    with open(archivo, 'r', newline='') as file:
        reader = csv.reader(file)
        resultado.append(next(reader, None))
        for fila in reader:
            if fechaUno<int(fila[6]) and fechaDos>int(fila[6]) and dni==fila[8] and tipoCheque==fila[9] and estadoCheque==fila[10]:
                resultado.append(fila)
    return resultado

def chequeRepetido():
    '''La función busca si dentro del resultado hay un cheque repetido.
    Si hay alguno imprime error por pantalla indicando el número de cheque.'''
    
    repetidos = []
    unicos = []
    for fila in resultado:
        cheque = fila[0]
        if cheque not in unicos:
            unicos.append(cheque)
        elif cheque not in repetidos:
            repetidos.append(cheque)
    if len(repetidos) == 0:
        return False
    else:
        for error in repetidos:
            print('Error, el cheque número {0} del DNI {1} está repetido.'.format(error, dni))

def descargar():
    '''Crea una archivo csv con nombre <dni>-<timestampactual>.csv
    Guarda la primera linea del archivo csv'''
    #Filtra el resultado denuevo, para que solo queden ciertas columnas
    nuevoResultado = []
    for fila in resultado:
        nuevoResultado.append((fila[3], fila[5], fila[6], fila[7]))
    #Genera el nombre del archivo
    fecha = datetime.datetime.now()
    timestampActual = int(datetime.datetime.timestamp(fecha))
    nuevoArchivo = ('{0}-{1}.csv'.format(dni,timestampActual))
    #Escribe el header y resultado en un nuevo archivo
    with open(nuevoArchivo, 'w', newline='') as newFile:
        writer = csv.writer(newFile)
        writer.writerows(nuevoResultado)
    print('Archivo descargado con nombre: "{0}"'.format(nuevoArchivo))

def tipoDeSalida(resultado):
    '''Si el resultado está vacio imprime un mensaje por pantalla.
    El resultado se muestra en un .csv o en pantalla'''
    if len(resultado) == 1:
        print('No hay resultados que cumplan esas condiciones...')
    #Imprime por pantalla las filas del resultado.
    elif salida == "PANTALLA":
        #Revisa si hay algún cheque repetido.
        chequeRepetido()
        for fila in resultado:
            print(fila)
    #Descarga las filas en un nuevo archivo.
    elif salida == "CSV":
        #Revisa si hay algún cheque repetido.
        chequeRepetido()
        print('Preparando archivo...')
        descargar()
    else:
        print('Tipo de salida no reconocido.')

#Aca empieza la lógica del script.
if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Es obligatorio colocar al menos cuatro argumentos")
        print("El orden de los argumentos son los siguientes:\
        \n  a. Nombre del archivo csv.\
        \n  b. DNI del cliente donde se filtraran.\
        \n  c. Salida: PANTALLA o CSV.\
        \n  d. Tipo de cheque: EMITIDO o DEPOSITADO.\
        \n  e. Estado del cheque: PENDIENTE, APROBADO, RECHAZADO. (Opcional)\
        \n  f. Rango fecha: xx-xx-xxxx:yy-yy-yyyy. (Opcional)\
        \nEjemplo: >python listado_cheques.py test.csv 42180335 PANTALLA EMITIDO")

    #Guarda los valores de los argumentos ingresados por consola.
    if len(sys.argv) >= 5:
        archivo = sys.argv[1]
        dni = sys.argv[2]
        salida = sys.argv[3]
        tipoCheque = sys.argv[4]

    if len(sys.argv) == 5:
        resultado = buscarPorDniTipo()
        tipoDeSalida(resultado)

    if len(sys.argv) == 6:
        arg = sys.argv[5]
        if arg == "PENDIENTE" or arg == "APROBADO" or arg == "RECHAZADO":
            estadoCheque = sys.argv[5]
            resultado = buscarPorDniTipoEstado()
        else:
            rangoFecha = sys.argv[5]
            resultado = buscarPorDniTipoFecha()
        tipoDeSalida(resultado)

    if len(sys.argv) == 7:
        estadoCheque = sys.argv[5]
        rangoFecha = sys.argv[6]
        resultado = buscarPorDniTipoEstadoFecha()
        tipoDeSalida(resultado)