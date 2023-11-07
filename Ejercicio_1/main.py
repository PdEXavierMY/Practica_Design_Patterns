import pandas as pd
from datos import *
from visualizacion import *
from analisis import *
from factories import *

if __name__ == "__main__":
    # Leer el archivo CSV "datos_limpio.csv"
    data = pd.read_csv("datos_limpio.csv", delimiter=';')

    # Extraer la columna "PRECIO"
    precios = data['PRECIO'].tolist()

    # Extraer las columnas "GRATUITO" y "LARGA-DURACION"
    gratuito = data['GRATUITO'].tolist()
    larga_duracion = data['LARGA-DURACION'].tolist()

    # Extraer la columna "TITULO-ACTIVIDAD"
    titulo_actividad = data['TITULO-ACTIVIDAD'].tolist()

    # Extraer la columna "DIAS-SEMANA"
    dias_semana = data['DIAS-SEMANA'].tolist()

    # Crear fábricas de análisis y visualización
    analisis_factory = MediaFactory()  # Fábrica para calcular la media
    visualizacion_factory_barras = BarrasFactory()  # Fábrica para gráfico de barras
    visualizacion_factory_queso = GcirculoFactory()  # Fábrica para gráfico circular
    visualizacion_factory_histograma = HistogramaFactory()  # Fábrica para histograma

    # Crear objetos de análisis
    analisis_media = analisis_factory.crear_analisis()
    analisis_moda = ModaFactory().crear_analisis()
    analisis_mediana = MedianaFactory().crear_analisis()

    # Calcular la media, moda y mediana de la columna "PRECIO"
    media_precio = analisis_media.analizar(precios)
    moda_precio = analisis_moda.analizar(precios)
    mediana_precio = analisis_mediana.analizar(precios)

    print("Vamos a ver los resultados de los análisis y visualizaciones:\n")
    print("Primero analizaremos la columna PRECIO:\n")

    # Mostrar los resultados por terminal
    print(f'Media de la columna "PRECIO": {media_precio}')
    print(f'Moda de la columna "PRECIO": {moda_precio}')
    print(f'Mediana de la columna "PRECIO": {mediana_precio}')

    print("\nAhora vamos a ver las visualizaciones:\n")

    # Crear objetos de visualización de barras para "GRATUITO" y "LARGA-DURACION"
    visualizacion_barras_gratuito = visualizacion_factory_barras.crear_visualizacion()
    visualizacion_barras_larga_duracion = visualizacion_factory_barras.crear_visualizacion()

    print("La primera es para ver cuantas actividades son gratuitas y cuantas de larga duración.")
    print("Recordar que 0 es NO y 1 es SI\n")
    # Generar diagrama de barras para "GRATUITO" y "LARGA-DURACION"
    visualizacion_barras_gratuito.generar_visualizacion(gratuito, "Actividades gratuitas")
    visualizacion_barras_larga_duracion.generar_visualizacion(larga_duracion, "Actividades de larga duración")

    # Crear objeto de visualización circular para "TITULO-ACTIVIDAD"
    visualizacion_queso_titulo_actividad = visualizacion_factory_queso.crear_visualizacion()

    print("La segunda es para ver cuantas actividades hay de cada tipo:\n")
    # Generar diagrama circular para "TITULO-ACTIVIDAD"
    visualizacion_queso_titulo_actividad.generar_visualizacion(titulo_actividad, "Actividades")

    # Crear objetos de visualización de barras para "DIAS-SEMANA"
    visualizacion_barras_dias_semana = visualizacion_factory_barras.crear_visualizacion()

    print("La tercera es para ver cuantas actividades hay por día de la semana:\n")
    # Generar diagrama barras para DIAS-SEMANA
    visualizacion_barras_dias_semana.generar_visualizacion_string(dias_semana, "Días de la semana")

    # Crear objeto de visualización de histograma para "PRECIO"
    visualizacion_histograma_precio = visualizacion_factory_histograma.crear_visualizacion()

    print("La última es para ver la frecuencia de los precios:\n")
    # Generar histograma para "PRECIO"
    visualizacion_histograma_precio.generar_visualizacion(precios, "Precios")