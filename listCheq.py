import csv
import sys
import datetime

#Se definen variables para filtrar las filas del archivo según distintos argumentos

def buscarPorDniTipo():
    #Filtra las filas del archivo por los argumentos dni y tipo de cheque.
    resultado = []
    with open(archivo, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)
        for fila in reader:
            if dni==fila[8] and tipoCheque==fila[9]:
                resultado.append(fila)
        return resultado

def buscarPorDniTipoEstado():
    #Filtra las filas del archivo por los argumentos dni, tipo de cheque y estado de cheque.
    resultado = []
    with open(archivo, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)
        for fila in reader:
            if dni==fila[8] and tipoCheque==fila[9] and estadoCheque==fila[10]:
                resultado.append(fila)
        return resultado

def buscarPorDniTipoEstadoFecha():
    #Filtra las filas del archivo por los argumentos fecha, dni, tipo de cheque y estado de cheque.
    #cambia las fechas de formato string a timestamp
    fechasIngresadas = rangoFecha.split(':')
    fechaSalida = []
    for fecha in fechasIngresadas:
        formatoFecha = datetime.datetime.strptime(fecha, '%d-%m-%Y')
        timestamp = int(datetime.datetime.timestamp(formatoFecha))
        fechaSalida.append(timestamp)
    fechaUno = fechaSalida[0]
    fechaDos = fechaSalida[1]
    #filtra las filas
    resultado = []
    with open(archivo, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)
        for fila in reader:
            if fechaUno<int(fila[6]) and fechaDos>int(fila[7]) and dni==fila[8] and tipoCheque==fila[9] and estadoCheque==fila[10]:
                resultado.append(fila)
    return resultado

def chequeRepetido():
    #La funcion busca si dentro del resultado hay un cheque repetido.
    #Si hay alguno imprime error por pantalla indicando el número de cheque.
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
            print('Error, el cheque número {0} del dni {1} está repetido.'.format(error, dni))

def descargar():
    #Guarda el header del archivo csv
    with open(archivo, 'r') as mainFile:
        reader = csv.reader(mainFile)
        for fila in reader:
            header = ((fila[6], fila[7], fila[5], fila[4]))
            break
    #Genera el nombre del archivo
    fecha = datetime.datetime.now()
    timestampActual = int(datetime.datetime.timestamp(fecha))
    nuevoArchivo = ('{0}-{1}.csv'.format(dni,timestampActual))
    #Filtra el resultado denuevo, para que solo queden ciertas columnas
    nuevoResultado = []
    with open(nuevoArchivo, 'w', newline='') as newFile:
        writer = csv.writer(newFile)
        writer.writerow(header)
        for fila in resultado:
            nuevoResultado.append((fila[6], fila[7], fila[5], fila[4]))
        writer.writerows(nuevoResultado)
    print('Archivo descargado con nombre: "{0}"'.format(nuevoArchivo))

def tipoDeSalida(resultado):
    #Si el resultado está vacio imprime un mensaje por pantalla.
    if not resultado:
        print('No hay resultados que cumplan esas condiciones...')
    #Imprime por pantalla las filas del resultado.
    elif salida == "PANTALLA":
        for fila in resultado:
            print(fila)
    #Descarga las filas en un nuevo archivo.
    elif salida == "CSV":
        print('Preparando archivo...')
        descargar()
    else:
        print('Tipo de salida no reconocido.')

#Aca empieza la lógica del script.
if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Es obligatorio colocar al menos cuatro argumentos")
        print("-Debes ingresar primero el nombre del archivo csv.\n-Despues el DNI del cliente.\n-Despues la forma de salida que puede ser: PANTALLA O CSV.\n-Despues el tipo de cheque que puede ser: EMITIDO O DEPOSITADO\n Ejemplo: test.csv 42180335 PANTALLA EMITIDO ")

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
        else:
            rangoFecha = sys.argv[5]
        resultado = buscarPorDniTipoEstado()
        tipoDeSalida(resultado)

    if len(sys.argv) == 7:
        estadoCheque = sys.argv[5]
        rangoFecha = sys.argv[6]
        resultado = buscarPorDniTipoEstadoFecha()
        tipoDeSalida(resultado)