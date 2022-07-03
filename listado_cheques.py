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
    new_file=[]
    csv_salida = tipoDeSalida
    csv_file = csv.reader(open(archivo, 'r'))
    header = next(csv_file)
    if csv_salida == "CSV":
        for row in csv_file:
            if dni==row[8] and tipoCheque==row[9]:
                new_file.append(row)
                new_file.append(row[3:8])
                with open(nombreDeArchivocsv+".csv", 'w', newline='') as cf:
                    writer = csv.writer(cf, delimiter=',')
                    writer.writerow(header[3:8])
                    writer.writerows(new_file[3:8])
            elif dni==row[8] and tipoCheque!=row[9]:
                print("Error! El tipo de cheque es incorrecto.")
                  

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
