import csv
import sys

with open('cheques.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader, None) # Saltea los encabezados de csv
    # Imprime cada fila en el archivo, estructura básica para saber como funciona
    for row in reader:
        print("Num: {0}, CodigoBanco: {1}, CodigoSucursal: {2}, NumeroCuentaOrigen: {3}, NumeroCuentaDestino: {4}, Valor: {5}, FechaOrigen: {6}, FechaPago: {7}, DNI: {8}, Estado: {9}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

