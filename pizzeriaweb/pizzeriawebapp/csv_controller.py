import csv

class CSV():

    def guardar_usuarios(self, usuario):
        csv_path = 'usuarios.csv'
        with open (csv_path, mode='a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(usuario.to_csv())
            csvfile.close()

    def leer_usuarios(self):
        csv_path = 'usuarios.csv'
        with open (csv_path, mode='r') as csvfile:
            csvreader = csv.reader(csvfile)
            filas = []
            for row in csvreader:
                filas.append(row)
            csvfile.close()
        return filas