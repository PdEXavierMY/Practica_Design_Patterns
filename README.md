# Patrones_de_Diseño

Pincha [aquí](https://github.com/Xavitheforce/Patrones_Creacionales/) para dirigirte a mi repositorio.

<h1>Ejercicio 1: Análisis Modular de las Activaciones del SAMUR-Protección Civil en Madrid con Abstract Factory</h1>

Contexto:

El SAMUR-Protección Civil es el servicio de atención a urgencias y emergencias sanitarias extrahospitalarias en el municipio de Madrid. Su labor es esencial para garantizar la seguridad y el bienestar de los ciudadanos en situaciones de emergencia. A lo largo del año, el SAMUR lleva a cabo múltiples "activaciones" en respuesta a diversas situaciones, desde accidentes de tráfico hasta emergencias médicas.

La ciudad de Madrid, en su compromiso con la transparencia y la apertura de datos, publica un registro detallado de estas activaciones en formato CSV. Este registro incluye información como la fecha, hora, tipo de emergencia, y otros detalles relevantes de cada activación.

Objetivo:

Tu tarea es desarrollar un programa en Python que haga uso del patrón de diseño "Abstract Factory" para modularizar y estandarizar el análisis de estos datos.

Para este ejercicio he realizado un patron abstract factory en la carpeta Ejercicio1 que se encarga de calcular varias estadisticas del conjunto de datos y graficar relaciones que puedan ser importantes para algun estudio posterior. Antes de esto se ha limpiado y preparado el csv proporcionado en datos.py

Las gráficas extraidas son:

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/Figure_1.png">
<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/2.png">
<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/3.png">
<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/4.png">
<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/5.png">

Y el output:

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/6.png">

El código con el que se implementa el patrón (el main del ejercicio) es:
```py
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
```

Este código implementa el patrón Abstract Factory para facilitar la creación de objetos relacionados con el análisis y la visualización de datos en Python. Utiliza fábricas concretas, como `MediaFactory` y `BarrasFactory`, para crear instancias específicas de análisis y visualización. Posteriormente, se aplican estas fábricas para realizar análisis estadísticos (media, moda, mediana) y generar visualizaciones (gráficos de barras, gráficos circulares, histogramas) a partir de un conjunto de datos proporcionado en un archivo CSV. El código demuestra cómo la implementación del patrón Abstract Factory puede mejorar la modularidad y extensibilidad al permitir la fácil incorporación de nuevos tipos de análisis y visualizaciones.

El patrón en sí es:
```py
# Fábrica para crear objetos de visualización
class VisualizacionFactory(ABC):
    @abstractmethod
    def crear_visualizacion(self) -> Visualizacion:
        pass

class HistogramaFactory(VisualizacionFactory):
    def crear_visualizacion(self) -> Visualizacion:
        return Histograma()

class BarrasFactory(VisualizacionFactory):
    def crear_visualizacion(self) -> Visualizacion:
        return Barras()

class GcirculoFactory(VisualizacionFactory):
    def crear_visualizacion(self) -> Visualizacion:
        return Gcirculo()

# Fábrica para crear objetos de análisis de datos
class AnalisisFactory(ABC):
    @abstractmethod
    def crear_analisis(self) -> Analisis:
        pass

class MediaFactory(AnalisisFactory):
    def crear_analisis(self) -> Analisis:
        return Media()

class MedianaFactory(AnalisisFactory):
    def crear_analisis(self) -> Analisis:
        return Mediana()

class ModaFactory(AnalisisFactory):
    def crear_analisis(self) -> Analisis:
        return Moda()

#producto abstracto
class Visualizacion(ABC):
    @abstractmethod
    def generar_visualizacion(self, dataset, titulo):
        pass

    def mostrar_datos(self, dataset):
        print(dataset)


#productos concreto
class Histograma(Visualizacion):
    def generar_visualizacion(self, dataset, titulo):
        # Generar un histograma a partir del dataset
        plt.hist(dataset, bins=10, color='skyblue', edgecolor='black')
        plt.xlabel('Valores')
        plt.ylabel('Frecuencia')
        plt.title(titulo)  # Usar el título proporcionado como argumento
        plt.show()

class Barras(Visualizacion):
    def generar_visualizacion(self, dataset, titulo):
        # Contar el número de repeticiones de cada valor
        valores_unicos = list(set(dataset))
        conteo_valores = [dataset.count(valor) for valor in valores_unicos]

        # Ubicación de las barras en el eje x
        ubicacion_barras = range(len(valores_unicos))

        # Generar un gráfico de barras con etiquetas en el eje x y conteo en el eje y
        plt.bar(ubicacion_barras, conteo_valores, color='green')
        plt.xlabel('Valores')
        plt.ylabel('Número de Repeticiones')
        plt.title(titulo)  # Usar el título proporcionado como argumento
        plt.xticks(ubicacion_barras, valores_unicos)  # Establecer las etiquetas en el eje x
        plt.show()

    def generar_visualizacion_string(self, dataset, titulo):
        # Separar los días en cada fila y contar su frecuencia
        dias = [dia for fila in dataset for dia in fila.split(',')]
        conteo_dias = Counter(dias)

        # Extraer los días únicos y sus frecuencias
        dias_unicos = list(conteo_dias.keys())
        frecuencias = list(conteo_dias.values())

        # Generar un histograma con etiquetas en el eje x y frecuencias en el eje y
        plt.bar(dias_unicos, frecuencias, color='skyblue', edgecolor='black')
        plt.xlabel('Días de la Semana')
        plt.ylabel('Frecuencia')
        plt.title(titulo)  # Usar el título proporcionado como argumento
        plt.show()

class Gcirculo(Visualizacion):
    def generar_visualizacion(self, dataset, titulo):
        # Contar el número de repeticiones de cada tipo de actividad
        conteo_actividades = Counter(dataset)

        # Extraer los tipos de actividad y sus repeticiones
        tipos_actividades = list(conteo_actividades.keys())
        repeticiones = list(conteo_actividades.values())

        # Colores para las porciones del gráfico
        colores = ['lightcoral', 'lightblue', 'lightgreen', 'lightsalmon', 'lightcyan']

        # Generar un gráfico circular (de queso) con etiquetas, leyenda y colores
        plt.pie(repeticiones, labels=tipos_actividades, autopct='%1.1f%%', startangle=90, colors=colores)
        plt.axis('equal')
        plt.title(titulo)  # Usar el título proporcionado como argumento
        plt.show()

#Producto abstracto
class Analisis(ABC):
    @abstractmethod
    def analizar(self, dataset):
        pass


#Productos concretos
class Media(Analisis):
    def analizar(self, dataset):
        return mean(dataset)

class Mediana(Analisis):
    def analizar(self, dataset):
        return median(dataset)

class Moda(Analisis):
    def analizar(self, dataset):
        return mode(dataset)
```

Ha sido beneficioso utilizar este patrón aqui debido a la amplia adaptabilidad que tiene considerando que existen mil y una formas de hacer gráficas y sacar estadísticas. Con el patrón se pueden implementar de forma sencilla sin que lleguen a afectar al código o ejecución.

<h1>Ejercicio: Sistema Integral de Creación y Gestión de Pizzas Gourmet con Almacenamiento en CSV utilizando el Patrón Builder</h1>

La reconocida cadena de pizzerías gourmet "Delizioso" ha decidido lanzar una plataforma digital para permitir a sus clientes diseñar y personalizar sus pizzas al máximo detalle. Esta pizzería es conocida por su meticulosidad y su vasto menú de ingredientes, técnicas de cocción y presentaciones. Además de la personalización, "Delizioso" busca almacenar cada pizza diseñada por sus clientes en un archivo CSV para análisis posterior, recomendaciones personalizadas y marketing dirigido.

Características a considerar:

Tipo de masa: Variedades premium desde masas delgadas hasta masas fermentadas por 48 horas, con opciones de ingredientes especiales.
Salsa base: Desde salsas clásicas hasta salsas de autor, incluyendo opciones veganas y de edición limitada.
Ingredientes principales: Una gama que abarca desde ingredientes locales hasta importados de especialidad, todos categorizados por su origen, tipo y rareza.
Técnicas de cocción: Diversidad que abarca desde hornos tradicionales hasta técnicas modernas de cocina molecular.
Presentación: Opciones que van desde estilos clásicos hasta presentaciones que son verdaderas obras de arte.
Maridajes recomendados: Una base de datos con cientos de opciones de vinos, cervezas y cocteles, con recomendaciones basadas en las elecciones de los ingredientes de la pizza.
Extras y finalizaciones: Desde bordes especiales hasta acabados con ingredientes gourmet como trufas y caviar.

Para este ejercicio hemos creado un Django que a través del patrón Builder crea pizzas personalizables y las guarda en un csv. (Tener en cuenta que para el ejercicio siguiente de la pizzeria los estilos se han actualizado y ha habido nuevas implementaciones, como, entre otros, un control de calidad en el guardado de la informacion del csv)

<h2>¡Importante! Para ver la pizzeria hay que descargarse los requirements en requirements.txt. Después abrir una terminal y ejecutar "cd pizzeriawebapp" seguido de 
"python manage.py runserver"</h2>

Lo primero que hay que hacer cuando se inicia el Django es iniciar sesión. La entrada de usuarios está hecha de forma que si un usuario no existe o su contraseña es incorrecta esto se le comunica para que pueda ir a registrarse.

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/7.png">
<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/8.png">

De necesitar registrarse hay otro formulario registro que comprueba que la contraseña metida sea correcta y además te devuelve a login si el ususario que se intenta crear ya se encuentra registrado.

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/9.png">

El mensaje si el usuario ya existe:

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/10.png">

Unas imagenes de como este formulario genera usuarios:

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/19.png">
<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/20.png">

Tras este proceso la página te dirige a su home, donde se pueden ver tus pedidos anteriores, los menús más comprados y crear una pizza personalizable:

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/11.png">
<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/12.png">

La pizza personalizable se crea aquí:

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/14.png">
<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/15.png">
<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/16.png">

Y unas imágenes que ilustran el guardado de las pizzas en el csv y su implementación en la página:

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/13.png">
<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/17.png">
<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/18.png">

El código del patrón implementado en este ejercicio es:

```py
class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def setMasa(self, masa):
        pass

    @abstractmethod
    def setSalsa(self, salsa):
        pass

    @abstractmethod
    def agregarIngrediente(self, ingrediente):
        pass

    @abstractmethod
    def setTecnicaDeCoccion(self, tecnica):
        pass

    @abstractmethod
    def setPresentacion(self, presentacion):
        pass

    @abstractmethod
    def agregarExtra(self, extra):
        pass

class PizzaBuilder(Builder):
    
    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Pizza()

    @property
    def product(self) -> None:
        product = self._product
        self.reset()
        return product
    
    def setNombre(self, nombre):
        self._product.nombre = nombre

    def setMasa(self, masa):
        self._product.masa = masa

    def setSalsa(self, salsa):
        self._product.salsa = salsa

    def agregarIngrediente(self, ingrediente):
        self._product.ingredientes = ingrediente

    def setTecnicaDeCoccion(self, tecnica):
        self._product.tecnica = tecnica

    def setPresentacion(self, presentacion):
        self._product.presentacion = presentacion

    def agregarExtra(self, extra):
        self._product.extras = extra

class Pizza:
    def __init__(self):
        self.nombre = None
        self.masa = None
        self.salsa = None
        self.ingredientes = None
        self.tecnica = None
        self.presentacion = None
        self.extras = None
    
    def to_csv(self):
        return [str(self.nombre)+";"+str(self.masa)+";"+str(self.salsa)+";"+str(self.ingredientes)+";"+str(self.tecnica)+";"+str(self.presentacion)+";"+str(self.extras)]

class Director():
    """
    El director solo es responsable de ejecutar los pasos de construcción en una
    secuencia particular. Es útil cuando se producen objetos de acuerdo con un
    orden o configuración específicos. En este caso, se trata de una pizza.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        El director funciona con cualquier instancia de constructor que el código
        del cliente le pase. De esta manera, el código del cliente puede cambiar
        el tipo final del producto recién ensamblado.
        """
        self._builder = builder

    """
    El director puede construir varias configuraciones de productos utilizando
    las mismas etapas de construcción.
    """

    def construir_pizza_completa(self, partes) -> None:
        self.builder.setNombre(partes[0])
        self.builder.setMasa(partes[1])
        self.builder.setSalsa(partes[2])
        self.builder.agregarIngrediente(partes[3])
        self.builder.setTecnicaDeCoccion(partes[4])
        self.builder.setPresentacion(partes[5])
        self.builder.agregarExtra(partes[6])
```

Y su implementación viene dada en las vistas por:

```py
            df = pd.read_csv('pizzas.csv', delimiter=';')  # Especifica el delimitador utilizado en tu archivo CSV
            nombres_pizza = list(df['Nombre'])
            campos = ['nombre', 'masa', 'salsa', 'ingredientes', 'tecnica', 'presentacion', 'extras']
            pizza = []
            for campo in campos:
                if form.cleaned_data['nombre'] in nombres_pizza:
                    messages.error(request, f"Los nombres deben ser únicos. Ese nombre ya existe")
                    return redirect('Crear Pizza')
                else:
                    if campo == 'ingredientes' or campo == 'extras':
                        # Convierte la lista a cadena y reemplaza las comas por barras inclinadas
                        lista_cambiada = '/'.join(map(str, form.cleaned_data[campo]))
                        
                        # Agrega la cadena modificada a la lista final
                        pizza.append([lista_cambiada])
                    else:
                        pizza.append(form.cleaned_data[campo])
            director = Director()
            builder = PizzaBuilder()
            director.builder = builder
            director.construir_pizza_completa(pizza)
            pizza_completa = builder.product
            id_usuario = None
            with open('logs.txt', 'r') as logs_file:
                id_usuario = logs_file.read()
            CSV().guardar_pizzas(pizza_completa, id_usuario)
```

El patrón Builder es ideal para este ejercicio de diseño de la plataforma digital de personalización de pizzas para "Delizioso" debido a la complejidad y diversidad de las opciones disponibles. El proceso de construir una pizza implica múltiples pasos interdependientes, desde la elección de la masa hasta los maridajes recomendados, y cada componente tiene varias variantes y opciones. El patrón Builder permite la construcción paso a paso de objetos complejos, en este caso, la pizza, garantizando que cada elección sea validada y que el sistema pueda adaptarse a las preferencias del cliente.

La robustez y adaptabilidad se logran al separar la construcción del objeto complejo en partes más pequeñas y manejables. Cada etapa del proceso de construcción de la pizza se aborda con un constructor específico, lo que facilita la validación y la incorporación de recomendaciones personalizadas. Además, la flexibilidad del sistema se asegura permitiendo la adición o modificación fácil de nuevos elementos en cada etapa del proceso sin afectar las otras partes del sistema.

El patrón Builder también se alinea con el objetivo de almacenar y reconstruir las pizzas personalizadas, ya que cada componente y elección se registra de manera ordenada durante el proceso de construcción. La interfaz de usuario amigable se beneficia al guiar al cliente a través de cada paso, ofreciendo información relevante y simplificando la toma de decisiones. Además, las medidas de seguridad para garantizar la integridad de los datos y la privacidad del cliente se integran de manera más eficaz, ya que el control detallado sobre la construcción de la pizza permite una gestión más precisa de los datos.

En resumen, el patrón Builder se revela como la elección óptima para este ejercicio al proporcionar una estructura modular, facilitar la validación y adaptación de elecciones, permitir la flexibilidad para futuras innovaciones y mejorar la experiencia del cliente a través de una interfaz intuitiva y segura.

<h1>Mejoras y optimizaciones de cara al siguiente:</h1>

Se ha actualizado el layout de la pizzería:

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/mejora_layout.png">

Se ha arreglado el guardado de csv (tema cifrado):

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/nuevocsv.png">

Se han añadido id autogenerativos a los usuarios y las pizzas ahora registran un nombre, el id del ususario que las ha creado y el precio (ver imagen superior):

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/nuevo_usuarios.png">

Se ha eliminado la seccion "Tus pizzas" en la página inicial de la pizzeria y se ha implementado un comprobador para confirmar el guardado de la pizza:

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/comprobacion_pizzas.png">

<h1>Ejercicio: Expansión del Sistema Integral de Pizzería "Delizioso" con Menús Personalizados y Almacenamiento en CSV utilizando los Patrones Builder y Composite
</h1>

Contexto:

Tras el éxito inicial de su plataforma digital de creación y gestión de pizzas gourmet personalizadas, la cadena "Delizioso" desea llevar su propuesta al siguiente nivel. Ahora, aparte de permitir la personalización individual de pizzas, quiere ofrecer a sus clientes la posibilidad de combinar sus creaciones en menús personalizados, que podrían incluir entradas, bebidas, pizzas y postres. Estos menús pueden ser creados tanto por el cliente como por el equipo culinario de "Delizioso", con opciones preestablecidas que representan la esencia de la marca.

Objetivos:

Desarrollo de Menús Personalizados:
Introducir la noción de un "menú", que puede contener varios elementos: entradas, bebidas, pizzas (que ya han sido definidas previamente con su sistema de creación de pizzas) y postres.
Un "menú" puede ser simple (contener elementos básicos) o compuesto (incluir otros menús más pequeños, como un "Combo Pareja" que incluye dos menús individuales).
Cada "menú" tendrá un código único y un precio, que se determina como la suma de los precios de sus elementos, con un descuento según la promoción aplicada.
Patrones de Diseño:
Implementar el patrón Composite para modelar la relación entre los elementos y menús, facilitando la creación, modificación y cálculo de precios de menús compuestos.
Continuar utilizando el patrón Builder para la creación detallada de las pizzas.
Interacción con CSV:
Ampliar el sistema de almacenamiento en CSV para incluir los menús personalizados, de forma que se pueda registrar y recuperar la información de menús individuales y compuestos.
Permitir que, a partir de un menú almacenado, se pueda reconstruir toda la estructura del menú con sus elementos individuales y precios.
Restricciones:
Las librerías estándar de Python para la interacción con archivos CSV están permitidas.
Se espera un diseño modular y orientado a objetos, con una clara separación de responsabilidades.
La implementación del cálculo del precio de un "menú" debe hacerse en tiempo de ejecución y ser eficiente.

<h2>Nota: Los UML de todos los ejercicios se encuentran en la carpeta UML</h2>

En este ejercicio de ampliación de la pizzeria he desarrollado 5 tipos de menu en la página inicial del negocio que llevan a un formulario que permite, dentro de la estrucutra del menú, personalizar el pedido:

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/menus.png">

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/menu_form.png">

Cabe destacar que se ha añadido a las pizzas un nombre (debe ser único y está controlado por mensajes de error) para poder elegir que tipo de pizza quiere el ususario dentro de la seleccion de la propia pizzeria o de sus pedidos pasados (todo esto está controlado con el id del usuario):

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/seleccion_personal.png">

Como adicional, al menú infantil se le ha añadido una lista de bebidas adaptadas.
El guardado de los menús queda como se ve en las siguientes imágenes:

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/menu_csv.png">

El precio del menu se calcula primero sumando los precios asociados al nuevo csv precios con todos los precios de cada item, y después se le aplica el descuento mostrado en la descripción de este en la página principal. Esto puede verse en la página de comprobación en la columna precio:

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/precios_csv.png">

<img src="https://github.com/Xavitheforce/Patrones_Creacionales/blob/main/imagenes_patronesC/comprobacion_menu.png">

El código patrón utilizado es:
```py
class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, the base Component can declare an interface for setting and
        accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods.
        """

        self._parent = parent

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Component class. This way, you won't need to
    expose any concrete component classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the leaf-level components.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether a
        component can bear children.
        """

        return False


class Maridaje(Component):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class PizzaMenu(Component):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Entrante(Component):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Postre(Component):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Menu(Component):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self, tipo:str) -> None:
        self._children: List[Component] = []
        self.tipo = tipo

    """
    A composite object can add or remove other components (both simple or
    complex) to or from its child list.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True
    
    def precio_total(self):
        precio_total = 0
        for child in self._children:
            precio_total += child.precio
        if self.tipo == "Doble":
            precio_total = precio_total * 0.9
        elif self.tipo == "Triple":
            precio_total = precio_total * 0.8
        elif self.tipo == "Familiar":
            precio_total = precio_total * 0.7
        elif self.tipo == "Infantil":
            precio_total = precio_total * 0.5
        return round(precio_total, 2)

    def to_csv(self):
        str_entrantes = ""
        str_pizzas = ""
        str_maridajes = ""
        str_postres = ""

        for child in self._children:
            if isinstance(child, Entrante):
                str_entrantes += child.nombre + "/"
            elif isinstance(child, PizzaMenu):
                str_pizzas += child.nombre + "/"
            elif isinstance(child, Maridaje):
                str_maridajes += child.nombre + "/"
            elif isinstance(child, Postre):
                str_postres += child.nombre + "/"

        return [str(self.tipo)+";"+str_entrantes+";"+str_pizzas+";"+str_maridajes+";"+str_postres+";"+str(self.precio_total())]
```

Y su implementación es una variación de:

```py
tipo_menu = 'Individual'
            precios = CSV().leer_precios()
            df = pd.read_csv('pizzas.csv', delimiter=';')  # Especifica el delimitador utilizado en tu archivo CSV
            entrante_1 = Entrante(
                nombre=form.cleaned_data['Entrante_1'],
                precio=float(precios[form.cleaned_data['Entrante_1']])
            )
            pizza_1 = PizzaMenu(
                nombre=form.cleaned_data['Pizza_1'],
                precio=df.loc[df['Nombre'] == form.cleaned_data['Pizza_1'], 'Precio'].values[0]
            )
            maridaje_1 = Maridaje(
                nombre=form.cleaned_data['Maridaje_1'],
                precio=float(precios[form.cleaned_data['Maridaje_1']])
            )
            postre_1 = Postre(
                nombre=form.cleaned_data['Postre_1'],
                precio=float(precios[form.cleaned_data['Postre_1']])
            )

            menu = Menu(
                tipo=tipo_menu
            )
            menu.add(entrante_1); menu.add(pizza_1); menu.add(maridaje_1); menu.add(postre_1)
            id_usuario = None
            with open('logs.txt', 'r') as logs_file:
                id_usuario = logs_file.read()
            menus = CSV().leer_menus()
            if menus:
                #si solo hay un elemento en la lista, el código es 1
                if len(menus) == 1:
                    codigo = 1
                else:
                    #si hay más de un elemento, el código es el último código + 1
                    ultimo_codigo = int(menus[-1][0].split(';')[-1])
                    codigo = ultimo_codigo + 1
            CSV().guardar_menus(menu, id_usuario, codigo)
            return redirect('Comprobacion Menu')
```

El patrón Composite es adecuado para la creación de menús en la pizzería debido a su capacidad para representar tanto los elementos individuales del menú, como las composiciones complejas de esos elementos. En un menú, tenemos diferentes categorías como entrantes, pizzas, maridajes y postres, y cada una de estas categorías puede contener elementos individuales o incluso otras composiciones. El Composite permite organizar estos elementos en una estructura de árbol, donde cada componente (elemento o composición) comparte una interfaz común. Esto facilita la manipulación uniforme de elementos individuales y compuestos, lo que es esencial al construir y gestionar menús complejos.

Además, el patrón Composite proporciona flexibilidad al permitir que los clientes seleccionen elementos individuales o combinaciones de elementos como parte de su pedido. La capacidad para calcular el precio total del menú en función de los elementos seleccionados también se beneficia de la estructura jerárquica del Composite. En última instancia, el patrón Composite simplifica la gestión y expansión del menú, ya que nuevos elementos o categorías pueden agregarse sin afectar la lógica existente, brindando así una solución eficiente y escalable para la pizzería.
