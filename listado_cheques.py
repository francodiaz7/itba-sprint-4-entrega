import csv
import sys
import datetime

def salidaPorPantalla(tipoDeSalida):
    csv_salida = tipoDeSalida
    csv_file = csv.reader(open(archivo, 'r'))
    if csv_salida == "PANTALLA":
        for row in csv_file:
            if dni==row[8] and tipoCheque==row[9]:
                print(row[:10])
            elif dni==row[8] and tipoCheque!=row[9]:
                print("Error! El tipo de cheque es incorrecto.")

def salidaPorCsv(tipoDeSalida,dniCliente):
    fechaActual = datetime.datetime.now()
    fechaActualFormato = datetime.datetime.strftime(fechaActual, '%d %m %Y  %Hhs %Mmin %Sseg')
    dni= dniCliente
    nombreDeArchivocsv= str("DNI "+dni+" "+fechaActualFormato)
    resultado=[]
    csv_salida = tipoDeSalida
    csv_file = csv.reader(open(archivo, 'r'))
    for row in csv_file:
        if dni==row[8] and tipoCheque==row[9]:
            resultado.append(row)
    return resultado

def buscarPorDniTipoEstado():
    resultado = []
    csv_file = csv.reader(open(archivo, 'r'))
    for row in csv_file:
        if dni==row[8] and tipoCheque==row[9] and estadoCheque==row[10]:
            resultado.append(row)
    return resultado

#Está incompleta, la fecha en el archivo csv está guardada en segundos.
#abajo del todo hay un ejemplo de como usar datetime

def buscarPorDniTipoEstadoFecha():
    resultado = []
    csv_file = csv.reader(open(archivo, 'r'))
    for row in csv_file:
        ''' EJEMPLO CÓDIGO FECHAS USANDO TIMESTAMP
         ts_now = time.time()
         dt_now = datetime.fromtimestamp(ts_now)
        '''

        #creo que acá hay que buscar el estado del cheque para la fecha actual, no sé si me equivoco
        if dni==row[8] and tipoCheque==row[9] and estadoCheque==row[10]:
            resultado.append(row)
    return resultado


#Falta la opción para crear un archivo CSV

def tipoDeSalida(resultado):
    if salida == "PANTALLA":
        print(resultado)
    elif salida == "CSV":
        print('Preparando archivo...')
        """
        csv_file = csv.reader(open(archivo, 'r'))
        with open('<DNI><TIMESTAMP>.csv', 'w') as csvfile:
            datos = ['nro_cuenta', 'start_date', 'end_date', 'valor_cheque']
            writer = csv.DictWriter(csvfile, datos = datos)

            writer.writeheader()
            for row in cvs_file:
                writer.writerow('nro_cuenta': row[5], 'start_date': row[7], 'end_date': datetime.now(), 'valor_cheque': row[6])
        """
    else:
        print('Tipo de salida no reconocido.')

#Aca empieza el codigo y la lógica.

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("Es obligatorio colocar al menos cuatro argumentos")
        print("-Debes ingresar primero el nombre del archivo csv.\n-Despues el DNI del cliente.\n-Despues la forma de salida que puede ser: PANTALLA O CSV.\n-Despues el tipo de cheque que puede ser: EMITIDO O DEPOSITADO\n Ejemplo: test.csv 42180335 PANTALLA EMITIDO ")

    if len(sys.argv) == 5:
        archivo = sys.argv[1]
        dni = sys.argv[2]
        salida = sys.argv[3]
        tipoCheque = sys.argv[4]
        print(archivo, dni, salida, tipoCheque)
        salidaPorPantalla(salida)
        salidaPorCsv(salida,dni)

    if 2 == 1: # Argumentos opcionales
        estadoCheque = sys.argv[5]
        rangoFecha = sys.argv[6]
