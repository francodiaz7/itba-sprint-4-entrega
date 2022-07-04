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
        for row in reader:
            if dni==row[8] and tipoCheque==row[9]:
                resultado.append(row)
        return resultado

def buscarPorDniTipoEstado():
    resultado = []
    with open(archivo, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if dni==row[8] and tipoCheque==row[9] and estadoCheque==row[10]:
                resultado.append(row)
        return resultado

def buscarPorDniTipoEstadoFecha():
    resultado = []
    with open(archivo, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            ''' EJEMPLO CÓDIGO FECHAS USANDO TIMESTAMP
            ts_now = time.time()
            dt_now = datetime.fromtimestamp(ts_now)
            '''

        #creo que acá hay que buscar el estado del cheque para la fecha actual, no sé si me equivoco
        if dni==row[8] and tipoCheque==row[9] and estadoCheque==row[10]:
            resultado.append(row)
    return resultado

''' ITEM 3 VERIFICAR CODIGO
def listaCheques():
    # Crea una lista de cheques para un número de dni
    
    csv_file = csv.reader(open(archivo, 'r'))
    for row in csv_file:
        cheques = []
        if dni == row[8]:
            cheque = row[1]
            while cheque != '':
                cheques.append(cheque)
                cheque = row[1]
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