import csv
import sys
import datetime
import time

#Se define variables para filtrar el archivo según distintos argumentos

def buscarPorDniTipo():
    resultado = []
    with open(archivo, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)
        for fila in reader:
            if dni==fila[8] and tipoCheque==fila[9]:
                resultado.append(fila)
        return resultado

def buscarPorDniTipoEstado():
    resultado = []
    with open(archivo, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)
        for fila in reader:
            if dni==fila[8] and tipoCheque==fila[9] and estadoCheque==fila[10]:
                resultado.append(fila)
        return resultado

def buscarPorDniTipoEstadoFecha():
    # procesa las fechas
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

''' ITEM 3 VERIFICAR CODIGO
def listaCheques():
    # Crea una lista de cheques para un número de dni
    
    csv_file = csv.reader(open(archivo, 'r'))
    for fila in csv_file:
        cheques = []
        if dni == fila[8]:
            cheque = fila[1]
            while cheque != '':
                cheques.append(cheque)
                cheque = fila[1]
    return cheques

def chequeRepetido():
    #La función busca si para un número de DNI hay cheques repetidos.
    #En caso afirmativo muestra un error por pantalla.
    
    nc = listaCheques()
    repetidos = []
    unicos = []
    for x in nc:
        if x not in unicos:
            unicos.append(x)
        elif x not in repetidos:
            repetidos.append(x)

    if len(repetidos) == 0:
        print('ERROR')
'''

def tipoDeSalida(resultado):
    if salida == "PANTALLA":
        if not resultado:
            print('No hay resultados que cumplan esas condiciones...')
        else:
            for fila in resultado:
                print(fila)
    elif salida == "CSV":
        if not resultado:
            print('No hay resultados que cumplan esas condiciones...')
        else:
            print('Preparando archivo...')
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
    else:
        print('Tipo de salida no reconocido.')

#Aca empieza el codigo y la lógica.

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Es obligatorio colocar al menos cuatro argumentos")
        print("-Debes ingresar primero el nombre del archivo csv.\n-Despues el DNI del cliente.\n-Despues la forma de salida que puede ser: PANTALLA O CSV.\n-Despues el tipo de cheque que puede ser: EMITIDO O DEPOSITADO\n Ejemplo: test.csv 42180335 PANTALLA EMITIDO ")

    #Guarda los valores de los argumentos
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