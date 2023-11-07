# Patrones_Creacionales

Ejercicio 1: Análisis Modular de las Activaciones del SAMUR-Protección Civil en Madrid con Abstract Factory

Contexto:

El SAMUR-Protección Civil es el servicio de atención a urgencias y emergencias sanitarias extrahospitalarias en el municipio de Madrid. Su labor es esencial para garantizar la seguridad y el bienestar de los ciudadanos en situaciones de emergencia. A lo largo del año, el SAMUR lleva a cabo múltiples "activaciones" en respuesta a diversas situaciones, desde accidentes de tráfico hasta emergencias médicas.

La ciudad de Madrid, en su compromiso con la transparencia y la apertura de datos, publica un registro detallado de estas activaciones en formato CSV. Este registro incluye información como la fecha, hora, tipo de emergencia, y otros detalles relevantes de cada activación.

Objetivo:

Tu tarea es desarrollar un programa en Python que haga uso del patrón de diseño "Abstract Factory" para modularizar y estandarizar el análisis de estos datos. En específico:

Lectura de Datos: Acceda y lea el archivo CSV directamente desde el enlace proporcionado: Activaciones del SAMUR-Protección Civil. A continuación, te dejo un código que realiza la lectura del archivo CSV:
import pandas as pd

 

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

 

# Leer CSV desde la URL

data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

 

print(data.head())  # Mostrar las primeras filas para visualizar los datos

 

Modelado de Datos: Modela y estructura la información para su análisis.
Abstract Factory: Diseña un "Abstract Factory" que permita crear diferentes tipos de análisis o representaciones de los datos. Por ejemplo:
Una fábrica que genere análisis estadísticos (media, moda, mediana).
Una fábrica que produzca visualizaciones gráficas (histogramas, gráficos de barras).
Cada fábrica debe tener al menos dos productos concretos (e.g., histograma de activaciones por tipo de emergencia, gráfico de barras de activaciones por mes).

Análisis y Representación: Utiliza las fábricas creadas para generar distintos análisis y representaciones de los datos. Muestra la media de activaciones por día, y un histograma de las activaciones
Recomendaciones:

El objetivo principal es demostrar una correcta implementación y uso del patrón "Abstract Factory". Asegúrate de definir claramente las interfaces (productos abstractos) y las implementaciones concretas (productos concretos).
Utiliza pandas para la manipulación de datos y, si decides incluir visualizaciones, considera matplotlib o seaborn.
 

Rúbrica para la Evaluación del Ejercicio

Criterio

Excelente (5-4 puntos)

Bueno (3-2 puntos)

Necesita Mejora (1-0 puntos)

Comprensión del Patrón Abstract Factory

Demuestra una completa comprensión del patrón, implementando correctamente las factories abstractas y concretas.

Implementa parcialmente el patrón, pero presenta algunas confusiones o errores menores.

No utiliza el patrón adecuadamente o no lo implementa en absoluto.

Lectura y Manipulación de Datos

Lee y procesa el archivo CSV de manera eficiente y sin errores. Los datos se estructuran adecuadamente para su análisis.

Lee el archivo CSV pero puede presentar errores menores en su manipulación o estructuración.

Tiene problemas significativos al leer o manipular el archivo CSV.

Implementación de Productos Concretos (Análisis)

Implementa productos concretos (ej., análisis estadístico) de manera correcta y útil. Los análisis son relevantes y significativos.

Implementa productos concretos, pero estos podrían no ser tan relevantes o contener errores menores.

No implementa productos concretos adecuadamente o los análisis proporcionados son incorrectos o no relevantes.

Implementación de Productos Concretos (Visualización)

Crea visualizaciones claras y útiles que aportan información valiosa sobre los datos.

Las visualizaciones se crean, pero pueden carecer de claridad o no ser totalmente relevantes.

No implementa adecuadamente las visualizaciones o las gráficas proporcionadas son incorrectas o no aportan valor.

Calidad del Código

El código es limpio, bien organizado, y sigue buenas prácticas. Es fácil de entender y modificar.

El código es generalmente claro, pero podría beneficiarse de mejor organización o de seguir mejores prácticas.

El código es desordenado, difícil de seguir o no sigue buenas prácticas de programación.

Documentación y Comentarios

El código está bien documentado con comentarios claros y útiles. Las funciones y clases tienen descripciones adecuadas.

Hay algunos comentarios, pero falta documentación en áreas clave o algunos comentarios no son claros.

Carece de documentación o los comentarios presentes no son útiles.

Notas adicionales:

La puntuación máxima posible según esta rúbrica es de 30 puntos.
 

 

Ejercicio: Sistema Integral de Creación y Gestión de Pizzas Gourmet con Almacenamiento en CSV utilizando el Patrón Builder

La reconocida cadena de pizzerías gourmet "Delizioso" ha decidido lanzar una plataforma digital para permitir a sus clientes diseñar y personalizar sus pizzas al máximo detalle. Esta pizzería es conocida por su meticulosidad y su vasto menú de ingredientes, técnicas de cocción y presentaciones. Además de la personalización, "Delizioso" busca almacenar cada pizza diseñada por sus clientes en un archivo CSV para análisis posterior, recomendaciones personalizadas y marketing dirigido.

Características a considerar:

Tipo de masa: Variedades premium desde masas delgadas hasta masas fermentadas por 48 horas, con opciones de ingredientes especiales.
Salsa base: Desde salsas clásicas hasta salsas de autor, incluyendo opciones veganas y de edición limitada.
Ingredientes principales: Una gama que abarca desde ingredientes locales hasta importados de especialidad, todos categorizados por su origen, tipo y rareza.
Técnicas de cocción: Diversidad que abarca desde hornos tradicionales hasta técnicas modernas de cocina molecular.
Presentación: Opciones que van desde estilos clásicos hasta presentaciones que son verdaderas obras de arte.
Maridajes recomendados: Una base de datos con cientos de opciones de vinos, cervezas y cocteles, con recomendaciones basadas en las elecciones de los ingredientes de la pizza.
Extras y finalizaciones: Desde bordes especiales hasta acabados con ingredientes gourmet como trufas y caviar.
Objetivos:

Diseñar un sistema que permita a los clientes construir su pizza paso a paso utilizando el patrón Builder.
Asegurar que cada elección sea validada para ser compatible con las selecciones previas del cliente.
Incorporar un sistema de recomendaciones que sugiera ingredientes, técnicas y maridajes basados en las elecciones previas del cliente.
Desarrollar un módulo que guarde cada pizza personalizada en un archivo CSV, almacenando cada detalle, desde los ingredientes hasta el maridaje recomendado.
Crear una funcionalidad que lea del archivo CSV y pueda reconstruir la pizza para su visualización, edición o reorden.
Garantizar la flexibilidad del sistema para futuras adiciones o modificaciones, ya que la pizzería está en constante innovación.
Desarrollar una interfaz de usuario amigable que guíe al cliente en el proceso de creación, ofreciendo información relevante sobre cada elección y facilitando la toma de decisiones.
Implementar medidas de seguridad para garantizar la integridad de los datos almacenados y la privacidad de las elecciones de los clientes.
Al final del ejercicio, el estudiante deberá justificar el uso del patrón Builder y explicar cómo se logra la robustez y adaptabilidad del sistema, destacando las ventajas de su diseño frente a otros posibles enfoques.

 

Rúbrica para el Sistema Integral de Creación y Gestión de Pizzas Gourmet

Criterio

Excelente (56-70 puntos)

Bueno (41-55 puntos)

Aceptable (26-40 puntos)

Insuficiente (0-25 puntos)

Implementación del patrón Builder

Se ha implementado el patrón Builder de forma impecable, demostrando una comprensión completa del patrón y sus ventajas.

Se ha implementado el patrón Builder correctamente con pequeñas áreas de mejora.

La implementación del patrón Builder tiene múltiples áreas de mejora, aunque muestra un entendimiento básico.

Falla en la implementación del patrón Builder o no se utiliza.

Validación y compatibilidad de elecciones

Validaciones meticulosas y precisas de todas las combinaciones de ingredientes y técnicas.

Validaciones en su mayoría correctas con algunas omisiones.

Validaciones básicas, omitiendo varios escenarios posibles.

Carece de validaciones o estas son incorrectas.

Sistema de recomendaciones

Recomendaciones altamente personalizadas y relevantes basadas en las elecciones previas.

Recomendaciones generalmente relevantes con algunas imprecisiones.

Recomendaciones básicas o generalizadas.

Sin sistema de recomendaciones o recomendaciones irrelevantes.

Almacenamiento y lectura en CSV

Almacenamiento y lectura perfectamente implementados con estructura clara y eficiente.

Almacenamiento y lectura correctamente implementados con pequeñas áreas de mejora.

Funcionalidad básica de almacenamiento y lectura con múltiples áreas de mejora.

Falta de funcionalidad o implementación errónea.

Flexibilidad y adaptabilidad del sistema

El sistema es altamente adaptable, con fácil integración de nuevos ingredientes y técnicas.

El sistema muestra adaptabilidad con algunas limitaciones.

El sistema tiene una estructura rígida con poca adaptabilidad.

El sistema es rígido y difícil de adaptar o modificar.

Interfaz de usuario

Interfaz intuitiva, atractiva y fácil de usar, que guía al usuario en cada paso.

Interfaz funcional con algunas áreas de mejora en diseño o usabilidad.

Interfaz básica que cumple su función, pero no es especialmente amigable.

Interfaz confusa, poco atractiva o difícil de usar.

Seguridad y privacidad

Implementa medidas avanzadas de seguridad y garantiza la privacidad de los datos del usuario.

Implementa medidas básicas de seguridad con algunas áreas de mejora.

Seguridad y privacidad mínimamente consideradas.

Ignora aspectos de seguridad y privacidad.

Justificación del diseño y uso del patrón Builder

Explicación detallada, coherente y con argumentos sólidos sobre el diseño y el patrón utilizado.

Explicación adecuada con algunas áreas de mejora.

Explicación básica con omisiones o inexactitudes.

No proporciona una explicación o esta es incorrecta.

Distribución de puntos:

Implementación del patrón Builder: 15 puntos.
Validación y compatibilidad de elecciones: 10 puntos.
Sistema de recomendaciones: 10 puntos.
Almacenamiento y lectura en CSV: 10 puntos.
Flexibilidad y adaptabilidad del sistema: 5 puntos.
Interfaz de usuario: 5 puntos.
Seguridad y privacidad: 5 puntos.
Justificación del diseño y uso del patrón Builder: 10 puntos.
El estudiante debe alcanzar al menos 26 puntos para obtener una calificación aprobatoria en este ejercicio.