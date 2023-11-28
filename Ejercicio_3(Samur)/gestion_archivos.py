from composite import Carpeta, Archivo, Enlace
from utils import extraer_usuario
from proxy import *

def buscar_documento(composite, fragmento_nombre):
    """
    Busca documentos en el composite cuyo nombre contiene el fragmento dado.
    Imprime por pantalla la información de los documentos encontrados.
    """
    documentos_encontrados = []

    # Función interna para buscar documentos recursivamente
    def buscar_recursivo(component, fragmento):
        if not component.is_composite():
            # Es un documento, verifica si el nombre contiene el fragmento
            if fragmento in component.nombre:
                documentos_encontrados.append(component)
        elif hasattr(component, '_children'):
            # Busca en las subcarpetas si es un composite con hijos
            for subcomponent in component._children:
                buscar_recursivo(subcomponent, fragmento)

    # Inicia la búsqueda desde el composite raíz
    buscar_recursivo(composite, fragmento_nombre)

    # Imprime la información de los documentos encontrados
    if documentos_encontrados:
        for documento in documentos_encontrados:
            if hasattr(documento, 'hipervinculo'):
                print(f"Documento: {documento.nombre}, Tipo: {documento.tipo}, Tamaño: {documento.tamaño}, Hipervínculo: {documento.hipervinculo}")
            else:
                print(f"Documento: {documento.nombre}, Tipo: {documento.tipo}, Tamaño: {documento.tamaño}")
    else:
        print(f"No se encontraron documentos que coincidan con '{fragmento_nombre}'.")

    # Actualizar el logs.txt
    logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
    usuario = extraer_usuario()
    if usuario is not None:
        logs.write(f"El usuario {usuario} ha buscado el documento {fragmento_nombre}\n")
    else:
        logs.write(f"Se ha buscado el documento {fragmento_nombre}\n")
    logs.close()

def crear_documento(composite, ruta, nombre, tipo, tamano, hipervinculo=None):
    # Divide la ruta en partes
    partes_ruta = ruta.split('/')

    # Verifica si la primera carpeta en la ruta coincide con la carpeta raíz
    if partes_ruta[0] != composite.nombre:
        print(f"Tu carpeta raíz introducida es '{partes_ruta[0]}'.")
        print(f"No se puede agregar el documento. La carpeta raíz debe ser '{composite.nombre}'.")
        return

    # Inicia desde el composite raíz
    ubicacion = composite

    # Recorre las partes de la ruta para encontrar la ubicación correcta
    for carpeta_nombre in partes_ruta[1:]:
        # Añade un condicional para manejar la situación de una ruta vacía
        if carpeta_nombre == '':
            ubicacion = composite
            break
        ubicacion = next((c for c in ubicacion._children if c.nombre == carpeta_nombre), None)
        if ubicacion is None:
            # La carpeta no existe
            print(f"No se puede agregar el documento. La carpeta '{carpeta_nombre}' no existe.")
            return

    # Crea el documento y agrégalo a la ubicación correcta
    if tipo == "Enlace":
        documento = Enlace(nombre, tipo, tamano, hipervinculo)
    else:
        documento = Archivo(nombre, tipo, tamano)
    ubicacion.add(documento)
    print(f"Documento '{nombre}' creado con éxito en la carpeta '{ubicacion.nombre}'.")
    print(composite.visualizar())

    # Actualizar el logs.txt
    logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
    usuario = extraer_usuario()
    if usuario is not None:
        logs.write(f"El usuario {usuario} ha creado el documento {nombre}\n")
    else:
        logs.write(f"Se ha creado el documento {nombre}\n")
    logs.close()

def editar_documento(composite, ruta, nombre_documento, atributo_a_modificar, nuevo_valor):
    # Divide la ruta en partes
    partes_ruta = ruta.split('/')

    # Verifica si la primera carpeta en la ruta coincide con la carpeta raíz
    if partes_ruta[0] != composite.nombre:
        print(f"Tu carpeta raíz introducida es '{partes_ruta[0]}'.")
        print(f"No se puede agregar el documento. La carpeta raíz debe ser '{composite.nombre}'.")
        return

    # Inicia desde el composite raíz
    ubicacion = composite

    # Recorre las partes de la ruta para encontrar la ubicación correcta
    for carpeta_nombre in partes_ruta[1:]:
        if carpeta_nombre == '':
            ubicacion = composite
            break
        ubicacion = next((c for c in ubicacion._children if c.nombre == carpeta_nombre), None)
        if ubicacion is None or not ubicacion.is_composite():
            # La carpeta no existe o no es una carpeta (puede ser un archivo)
            print(f"No se puede editar el documento. La carpeta '{carpeta_nombre}' no existe o no es una carpeta.")
            return

    # Verifica si se encontró la ubicación correcta
    if ubicacion is not None and ubicacion.is_composite():
        # Busca el documento por nombre
        documento = next((c for c in ubicacion._children if c.nombre == nombre_documento), None)
        if documento is not None:
            # Modifica el atributo especificado
            if hasattr(documento, atributo_a_modificar):
                setattr(documento, atributo_a_modificar, nuevo_valor)
                print(f"Documento '{nombre_documento}' modificado con éxito.")
                print(composite.visualizar())
            else:
                print(f"No se puede editar el atributo. '{atributo_a_modificar}' no es un atributo válido.")
        else:
            print(f"No se puede encontrar el documento '{nombre_documento}'.")
    else:
        print("No se puede encontrar la ubicación especificada.")
    
    #actualizar el logs.txt
    logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
    usuario = extraer_usuario()
    if usuario is not None:
        logs.write(f"El usuario {usuario} ha editado el documento {nombre_documento}\n")
    else:
        logs.write(f"Se ha editado el documento {nombre_documento}\n")
    logs.close()

def borrar_documento(composite, ruta, nombre_documento):
    # Divide la ruta en partes
    partes_ruta = ruta.split('/')

    # Verifica si la primera carpeta en la ruta coincide con la carpeta raíz
    if partes_ruta[0] != composite.nombre:
        print(f"Tu carpeta raíz introducida es '{partes_ruta[0]}'.")
        print(f"No se puede borrar el documento. La carpeta raíz debe ser '{composite.nombre}'.")
        return

    # Inicia desde el composite raíz
    ubicacion = composite

    # Recorre las partes de la ruta para encontrar la ubicación correcta
    for carpeta_nombre in partes_ruta[1:]:
        if carpeta_nombre == '':
            ubicacion = composite
            break
        ubicacion = next((c for c in ubicacion._children if c.nombre == carpeta_nombre), None)
        if ubicacion is None or not ubicacion.is_composite():
            # La carpeta no existe o no es una carpeta (puede ser un archivo)
            print(f"No se puede borrar el documento. La carpeta '{carpeta_nombre}' no existe o no es una carpeta.")
            return

    # Verifica si se encontró la ubicación correcta
    if ubicacion is not None and ubicacion.is_composite():
        # Busca el documento por nombre
        documento = next((c for c in ubicacion._children if c.nombre == nombre_documento), None)
        if documento is not None:
            # Elimina el documento
            ubicacion.remove(documento)
            print(f"Documento '{nombre_documento}' borrado con éxito.")
            print(composite.visualizar())
        else:
            print(f"No se puede encontrar el documento '{nombre_documento}'.")
    else:
        print("No se puede encontrar la ubicación especificada.")

    #actualizar el logs.txt
    logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
    usuario = extraer_usuario()
    if usuario is not None:
        logs.write(f"El usuario {usuario} ha borrado el documento {nombre_documento}\n")
    else:
        logs.write(f"Se ha borrado el documento {nombre_documento}\n")
    logs.close()

def buscar_carpeta(composite, fragmento_nombre):
    """
    Busca carpetas en el composite cuyo nombre contiene el fragmento dado.
    Imprime por pantalla las carpetas encontradas con su contenido.
    """
    carpetas_encontradas = []

    # Función interna para buscar carpetas recursivamente
    def buscar_recursivo(component, fragmento):
        if component.is_composite():
            # Es una carpeta, verifica si el nombre contiene el fragmento
            if fragmento in component.nombre:
                carpetas_encontradas.append(component)

            # Busca en las subcarpetas
            for subcomponent in component._children:
                buscar_recursivo(subcomponent, fragmento)

    # Inicia la búsqueda desde el composite raíz
    buscar_recursivo(composite, fragmento_nombre)

    # Imprime las carpetas encontradas con su contenido
    if carpetas_encontradas:
        for carpeta in carpetas_encontradas:
            print(carpeta.visualizar())
    else:
        print(f"No se encontraron carpetas que coincidan con '{fragmento_nombre}'.")

    #actualizar el logs.txt
    logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
    usuario = extraer_usuario()
    if usuario is not None:
        logs.write(f"El usuario {usuario} ha buscado la carpeta {fragmento_nombre}\n")
    else:
        logs.write(f"Se ha buscado la carpeta {fragmento_nombre}\n")
    logs.close()

def crear_carpeta(composite, ruta, nombre_carpeta):
    """
    Crea una carpeta en la ruta especificada del composite.
    """
    # Divide la ruta en partes
    partes_ruta = ruta.split('/')

    # Verifica si la primera carpeta en la ruta coincide con la carpeta raíz
    if partes_ruta[0] != composite.nombre:
        print(f"La carpeta raíz introducida es '{partes_ruta[0]}'.")
        print(f"No se puede crear la carpeta. La carpeta raíz debe ser '{composite.nombre}'.")
        return

    # Inicia desde el composite raíz
    ubicacion = composite

    # Recorre las partes de la ruta para encontrar la ubicación correcta
    for carpeta_nombre in partes_ruta[1:]:
        # Añade un condicional para manejar la situación de una ruta vacía
        if carpeta_nombre == '':
            break
        # Busca si la carpeta ya existe
        carpeta_existente = next((c for c in ubicacion._children if c.nombre == carpeta_nombre), None)

        if carpeta_existente is None:
            # La carpeta no existe, la crea y la agrega a la ubicación actual
            nueva_carpeta = Carpeta(carpeta_nombre)
            ubicacion.add(nueva_carpeta)
            ubicacion = nueva_carpeta
        elif carpeta_existente.is_composite():
            # La carpeta ya existe y es una carpeta, avanza a la siguiente ubicación
            ubicacion = carpeta_existente
        else:
            # La carpeta ya existe pero no es una carpeta (puede ser un archivo)
            print(f"No se puede crear la carpeta. '{carpeta_nombre}' ya existe y no es una carpeta.")
            return

    # Verifica si se encontró la ubicación correcta
    if ubicacion is not None and ubicacion.is_composite():
        # Busca si la carpeta ya existe
        carpeta_existente = next((c for c in ubicacion._children if c.nombre == nombre_carpeta), None)

        if carpeta_existente is None:
            # La carpeta no existe, la crea y la agrega a la ubicación actual
            nueva_carpeta = Carpeta(nombre_carpeta)
            ubicacion.add(nueva_carpeta)
            print(f"Carpeta '{nombre_carpeta}' creada con éxito.")
            print(composite.visualizar())
        else:
            # La carpeta ya existe
            print(f"No se puede crear la carpeta. La carpeta '{nombre_carpeta}' ya existe en la ubicación especificada.")
    else:
        print("No se puede encontrar la ubicación especificada.")

    # Actualizar el logs.txt
    logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
    usuario = extraer_usuario()
    if usuario is not None:
        logs.write(f"El usuario {usuario} ha creado la carpeta {nombre_carpeta}\n")
    else:
        logs.write(f"Se ha creado la carpeta {nombre_carpeta}\n")
    logs.close()

def editar_carpeta(composite, ruta, nombre_carpeta, nuevo_nombre):
    # Divide la ruta en partes
    partes_ruta = ruta.split('/')

    # Verifica si la primera carpeta en la ruta coincide con la carpeta raíz
    if partes_ruta[0] != composite.nombre:
        print(f"Tu carpeta raíz introducida es '{partes_ruta[0]}'.")
        print(f"No se puede editar la carpeta. La carpeta raíz debe ser '{composite.nombre}'.")
        return

    # Inicia desde el composite raíz
    ubicacion = composite

    # Recorre las partes de la ruta para encontrar la ubicación correcta
    for carpeta_nombre in partes_ruta[1:]:
        if carpeta_nombre == '':
            ubicacion = composite
            break
        ubicacion = next((c for c in ubicacion._children if c.nombre == carpeta_nombre), None)
        if ubicacion is None or not ubicacion.is_composite():
            # La carpeta no existe o no es una carpeta (puede ser un archivo)
            print(f"No se puede editar la carpeta. La carpeta '{carpeta_nombre}' no existe o no es una carpeta.")
            return

    # Verifica si se encontró la ubicación correcta
    if ubicacion is not None and ubicacion.is_composite():
        # Busca la carpeta por nombre
        carpeta = next((c for c in ubicacion._children if c.nombre == nombre_carpeta), None)
        if carpeta is not None and carpeta.is_composite():
            # Modifica el nombre de la carpeta
            carpeta.nombre = nuevo_nombre
            print(f"Carpeta '{nombre_carpeta}' modificada con éxito.")
            print(composite.visualizar())
        else:
            print(f"No se puede encontrar la carpeta '{nombre_carpeta}'.")
    else:
        print("No se puede encontrar la ubicación especificada.")

    #actualizar el logs.txt
    logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
    usuario = extraer_usuario()
    if usuario is not None:
        logs.write(f"El usuario {usuario} ha editado la carpeta {nombre_carpeta}\n")
    else:
        logs.write(f"Se ha editado la carpeta {nombre_carpeta}\n")
    logs.close()

def borrar_carpeta(composite, ruta, nombre_carpeta):
    # Divide la ruta en partes
    partes_ruta = ruta.split('/')

    # Verifica si la primera carpeta en la ruta coincide con la carpeta raíz
    if partes_ruta[0] != composite.nombre:
        print(f"Tu carpeta raíz introducida es '{partes_ruta[0]}'.")
        print(f"No se puede borrar la carpeta. La carpeta raíz debe ser '{composite.nombre}'.")
        return

    # Inicia desde el composite raíz
    ubicacion = composite

    # Recorre las partes de la ruta para encontrar la ubicación correcta
    for carpeta_nombre in partes_ruta[1:]:
        if carpeta_nombre == '':
            ubicacion = composite
            break
        ubicacion = next((c for c in ubicacion._children if c.nombre == carpeta_nombre), None)
        if ubicacion is None or not ubicacion.is_composite():
            # La carpeta no existe o no es una carpeta (puede ser un archivo)
            print(f"No se puede borrar la carpeta. La carpeta '{carpeta_nombre}' no existe o no es una carpeta.")
            return

    # Verifica si se encontró la ubicación correcta
    if ubicacion is not None and ubicacion.is_composite():
        # Busca la carpeta por nombre
        carpeta = next((c for c in ubicacion._children if c.nombre == nombre_carpeta), None)
        if carpeta is not None and carpeta.is_composite():
            # Elimina la carpeta y su contenido del composite
            ubicacion.remove(carpeta)
            print(f"Carpeta '{nombre_carpeta}' y su contenido eliminados con éxito.")
            print(composite.visualizar())
        else:
            print(f"No se puede encontrar la carpeta '{nombre_carpeta}'.")
    else:
        print("No se puede encontrar la ubicación especificada.")

    #actualizar el logs.txt
    logs = open('Ejercicio_3(Samur)/logs.txt', 'a', encoding='utf-8')
    usuario = extraer_usuario()
    if usuario is not None:
        logs.write(f"El usuario {usuario} ha borrado la carpeta {nombre_carpeta}\n")
    else:
        logs.write(f"Se ha borrado la carpeta {nombre_carpeta}\n")
    logs.close()