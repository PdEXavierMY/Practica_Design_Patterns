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

Para este ejercicio hemos creado un Django que a través del patrón Builder crea pizzas personalizables y las guarda en un csv.

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

El patrón Builder es ideal para este ejercicio de diseño de la plataforma digital de personalización de pizzas para "Delizioso" debido a la complejidad y diversidad de las opciones disponibles. El proceso de construir una pizza implica múltiples pasos interdependientes, desde la elección de la masa hasta los maridajes recomendados, y cada componente tiene varias variantes y opciones. El patrón Builder permite la construcción paso a paso de objetos complejos, en este caso, la pizza, garantizando que cada elección sea validada y que el sistema pueda adaptarse a las preferencias del cliente.

La robustez y adaptabilidad se logran al separar la construcción del objeto complejo en partes más pequeñas y manejables. Cada etapa del proceso de construcción de la pizza se aborda con un constructor específico, lo que facilita la validación y la incorporación de recomendaciones personalizadas. Además, la flexibilidad del sistema se asegura permitiendo la adición o modificación fácil de nuevos elementos en cada etapa del proceso sin afectar las otras partes del sistema.

El patrón Builder también se alinea con el objetivo de almacenar y reconstruir las pizzas personalizadas, ya que cada componente y elección se registra de manera ordenada durante el proceso de construcción. La interfaz de usuario amigable se beneficia al guiar al cliente a través de cada paso, ofreciendo información relevante y simplificando la toma de decisiones. Además, las medidas de seguridad para garantizar la integridad de los datos y la privacidad del cliente se integran de manera más eficaz, ya que el control detallado sobre la construcción de la pizza permite una gestión más precisa de los datos.

En resumen, el patrón Builder se revela como la elección óptima para este ejercicio al proporcionar una estructura modular, facilitar la validación y adaptación de elecciones, permitir la flexibilidad para futuras innovaciones y mejorar la experiencia del cliente a través de una interfaz intuitiva y segura.
