import csv
import ast  # Módulo ast para evaluar la cadena como una lista literal de Python

def expandir_lista(items):
            nuevos_items = []
            for item in items:
                if item.startswith('[') and item.endswith(']'):
                    # Si es una cadena que representa una lista, evaluarla y agregar sus elementos
                    lista_evaluada = ast.literal_eval(item)
                    nuevos_items.extend(lista_evaluada)
                else:
                    # Si no es una cadena que representa una lista, agregar el elemento tal cual
                    nuevos_items.append(item)
            return nuevos_items

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

        # Leer precios del CSV
        precios = self.leer_precios()
        # Obtener los ítems de la pizza
        items_pizza = expandir_lista(pizza.to_csv()[0].split(';')[1:])  # Excluir el nombre

        # Calcular el precio total
        precio_total = sum(precios[item] for item in items_pizza)

        # Añadir el precio total a la lista de la pizza
        pizza_lista = pizza.to_csv() + [f';{precio_total:.2f};{id_usuario}']

        with open(csv_path, mode='a', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar=' ')
            csvwriter.writerow(pizza_lista)

    def leer_pizzas(self):
        csv_path = 'pizzas.csv'
        with open (csv_path, mode='r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            filas = []
            for row in csvreader:
                filas.append(row)
            csvfile.close()
        return filas
    
    def leer_precios(self):
        precios_path = 'precios.csv'
        precios = {}

        with open(precios_path, mode='r', encoding='utf-8') as precios_file:
            csvreader = csv.reader(precios_file, delimiter=';')
            next(csvreader)  # Saltar la primera fila (encabezado)

            for row in csvreader:
                item = row[0]
                precio = float(row[1])
                precios[item] = precio

        return precios