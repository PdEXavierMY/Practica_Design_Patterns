# Patrones_Creacionales

Pincha [aquí](https://github.com/Xavitheforce/Patrones_Creacionales/) para dirigirte a mi repositorio.

Ejercicio 1: Análisis Modular de las Activaciones del SAMUR-Protección Civil en Madrid con Abstract Factory

Contexto:

El SAMUR-Protección Civil es el servicio de atención a urgencias y emergencias sanitarias extrahospitalarias en el municipio de Madrid. Su labor es esencial para garantizar la seguridad y el bienestar de los ciudadanos en situaciones de emergencia. A lo largo del año, el SAMUR lleva a cabo múltiples "activaciones" en respuesta a diversas situaciones, desde accidentes de tráfico hasta emergencias médicas.

La ciudad de Madrid, en su compromiso con la transparencia y la apertura de datos, publica un registro detallado de estas activaciones en formato CSV. Este registro incluye información como la fecha, hora, tipo de emergencia, y otros detalles relevantes de cada activación.

Objetivo:

Tu tarea es desarrollar un programa en Python que haga uso del patrón de diseño "Abstract Factory" para modularizar y estandarizar el análisis de estos datos.

Para este ejercicio he realizado un patron abstract factory en la carpeta Ejercicio1 que se encarga de calcular varias estadisticas del conjunto de datos y graficar relaciones que puedan ser importantes para algun estudio posterior. Antes de esto se ha limpiado y preparado el csv proporcionado en datos.py

Las gráficas extraidas son:

 ![Figure_1](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/6de3d79e-6c2c-4d46-82a6-7ee71397da93)
![2](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/ee4dbb48-3df4-4aea-980a-44a6adfa1fb7)
![3](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/b1301eae-4133-44e7-9e1e-f9516bba1433)
![4](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/5b229f1b-62ad-4b7c-b7e4-cfc2592d05e6)
![5](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/58806b1b-c060-44ea-beec-9eb4a37b845a)

Y el output:

![6](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/39c1c9aa-3002-4a5c-8668-8fcd0dc9781b)

Ha sido beneficioso utilizar este patrón aqui debido a la amplia adaptabilidad que tiene considerando que existen mil y una formas de hacer gráficas y sacar estadísticas. Con el patrón se pueden implementar de forma sencilla sin que lleguen a afectar al código o ejecución.

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

Para este ejercicio hemos creado un Django que a través del patrón Builder crea pizzas personalizables y las guarda en un csv.

Lo primero que hay que hacer cuando se inicia el Django es iniciar sesión. La entrada de usuarios está hecha de forma que si un usuario no existe o su contraseña es incorrecta esto se le comunica para que pueda ir a registrarse.

![7](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/ab7c8d4f-702c-4f75-b1af-5a08a459dea7)
![8](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/f70270c7-ee7a-4d7d-a77f-796e6d733ba5)


De necesitar registrarse hay otro formulario registro que comprueba que la contraseña metida sea correcta y además te devuelve a login si el ususario que se intenta crear ya se encuentra registrado.

![9](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/e48f3812-435a-43fc-b4f8-0d4d25882811)
![10](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/90be49ca-3890-4143-85d5-1d5dfc51c313)

Unas imagenes de como este formulario genera usuarios:

![19](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/e30a5c94-fe47-4b08-9715-0a7328d15753)
![20](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/6602453f-a878-4c6d-a565-0c705053a3e4)

Tras este proceso la página te dirige a su home, donde se pueden ver tus pedidos anteriores, los menús más comprados y crear una pizza personalizable:

![11](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/092d6811-4331-496c-9b3f-c493b68aff09)
![12](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/d6bbd1df-9b9e-4cc8-8fec-5f1b7c8fb7fb)


La pizza personalizable se crea aquí:

![14](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/9ec2ed78-3c64-4866-8d20-19b97acdfb3e)
![15](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/1dc3d1ce-6287-4d85-ac8b-8102228521ba)
![16](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/192b182a-14f0-4dbf-ae0a-bf311656d109)

Y unas imágenes que ilustran el guardado de las pizzas en el csv y su implementación en la página:

![13](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/fa54efb8-d6e5-4f35-8245-1402ba158609)
![17](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/37656af7-1413-4ad7-9d8f-0074ec1aafff)
![18](https://github.com/Xavitheforce/Patrones_Creacionales/assets/91721699/8c8462f6-213c-4385-8b17-5834767639d6)

El patrón Builder es ideal para este ejercicio de diseño de la plataforma digital de personalización de pizzas para "Delizioso" debido a la complejidad y diversidad de las opciones disponibles. El proceso de construir una pizza implica múltiples pasos interdependientes, desde la elección de la masa hasta los maridajes recomendados, y cada componente tiene varias variantes y opciones. El patrón Builder permite la construcción paso a paso de objetos complejos, en este caso, la pizza, garantizando que cada elección sea validada y que el sistema pueda adaptarse a las preferencias del cliente.

La robustez y adaptabilidad se logran al separar la construcción del objeto complejo en partes más pequeñas y manejables. Cada etapa del proceso de construcción de la pizza se aborda con un constructor específico, lo que facilita la validación y la incorporación de recomendaciones personalizadas. Además, la flexibilidad del sistema se asegura permitiendo la adición o modificación fácil de nuevos elementos en cada etapa del proceso sin afectar las otras partes del sistema.

El patrón Builder también se alinea con el objetivo de almacenar y reconstruir las pizzas personalizadas, ya que cada componente y elección se registra de manera ordenada durante el proceso de construcción. La interfaz de usuario amigable se beneficia al guiar al cliente a través de cada paso, ofreciendo información relevante y simplificando la toma de decisiones. Además, las medidas de seguridad para garantizar la integridad de los datos y la privacidad del cliente se integran de manera más eficaz, ya que el control detallado sobre la construcción de la pizza permite una gestión más precisa de los datos.

En resumen, el patrón Builder se revela como la elección óptima para este ejercicio al proporcionar una estructura modular, facilitar la validación y adaptación de elecciones, permitir la flexibilidad para futuras innovaciones y mejorar la experiencia del cliente a través de una interfaz intuitiva y segura.
