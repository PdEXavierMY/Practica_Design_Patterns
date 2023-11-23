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

        # Leer precios del CSV
        precios = self.leer_precios()
        # Obtener los ítems de la pizza
        items_pizza = pizza.to_csv()[0].split(';')[1:]  # Excluir el nombre
        items_pizza = [item.strip("[]' ") for item in items_pizza]
        # Nueva lista para almacenar los elementos después de dividirlos por "/"
        nuevo_items_pizza = []
        # Iterar sobre los elementos y dividirlos si contienen "/"
        for elemento in items_pizza:
            if '/' in elemento:
                nuevo_items_pizza.extend(elemento.split('/'))
            elif elemento == '':
                pass
            else:
                nuevo_items_pizza.append(elemento)
    
        # Calcular el precio total
        precio_total = sum(precios[item] for item in nuevo_items_pizza)

        # Añadir el precio total a la lista de la pizza
        pizza_lista = pizza.to_csv() + [f'{precio_total:.2f}', str(id_usuario)]
        pizza_str = ';'.join(pizza_lista)

        with open(csv_path, mode='a', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar=' ')
            csvwriter.writerow([pizza_str])

    def leer_pizzas(self):
        csv_path = 'pizzas.csv'
        with open (csv_path, mode='r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            filas = []
            for row in csvreader:
                filas.append(row)
            csvfile.close()
        return filas
    
    def borrar_ultima_pizza(self):
        csv_path = 'pizzas.csv'

        # Lee todas las líneas del archivo CSV
        with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
            filas = list(csv.reader(csvfile))

        # Borra la última línea del archivo CSV
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(filas[:-1])
    
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

    def leer_menus(self):
        csv_path = 'menus.csv'
        with open(csv_path, mode='r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            filas = []
            for row in csvreader:
                filas.append(row)
            csvfile.close()
        return filas
    
    def guardar_menus(self, menu, id_usuario, codigo):
        csv_path = 'menus.csv'
        string_a_guardar = menu.to_csv() + [";"+str(id_usuario)+";"+str(codigo)]
        string_a_guardar = ''.join(string_a_guardar)
        with open(csv_path, mode='a', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar=' ')
            csvwriter.writerow([string_a_guardar])

    def borrar_ultimo_menu(self):
        csv_path = 'menus.csv'

        # Lee todas las líneas del archivo CSV
        with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
            filas = list(csv.reader(csvfile))

        # Borra la última línea del archivo CSV
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(filas[:-1])