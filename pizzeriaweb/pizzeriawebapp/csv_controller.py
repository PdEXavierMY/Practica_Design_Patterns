import csv

class CSV():

    def guardar_usuarios(self, campos_usuario):
        csv_path = 'usuarios.csv'
        with open(csv_path, mode='a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(campos_usuario)
            csvfile.close()

    def leer_usuarios(self):
        csv_path = 'usuarios.csv'
        with open(csv_path, mode='r') as csvfile:
            csvreader = csv.reader(csvfile)
            filas = []
            for row in csvreader:
                filas.append(row)
            csvfile.close()
        return filas

    def guardar_pizzas(self, pizza, id_usuario):
        csv_path = 'pizzas.csv'
        with open(csv_path, mode='a', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar=' ')
            csvwriter.writerow([str(pizza.to_csv()[0] + ';' + id_usuario)])

    def leer_pizzas(self):
        csv_path = 'pizzas.csv'
        with open (csv_path, mode='r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            filas = []
            for row in csvreader:
                filas.append(row)
            csvfile.close()
        return filas