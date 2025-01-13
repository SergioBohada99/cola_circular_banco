# Simulador de Banco con Colas Circulares

Este proyecto es una aplicación bancaria que simula un sistema de colas circulares con múltiples cajeros. La aplicación utiliza el algoritmo FIFO (First In, First Out) para gestionar las colas, permitiendo una experiencia visual interactiva a través de una interfaz gráfica. Además, incluye la simulación de generaciones de clientes que llegan y son atendidos por los cajeros.

## Características

- **Generación de Múltiples Cajeros:** Se generan entre 2 y 4 cajeros de manera aleatoria al inicio de la simulación.
- **Colas por Cajero:** Cada cajero tiene su propia cola, implementada como una estructura de datos tipo cola circular.
- **Atención FIFO:** Los clientes son atendidos según el orden en el que ingresan a la cola.
- **Simulación de Generaciones:** Se simulan 4 generaciones de clientes que llegan aleatoriamente y son distribuidos en las colas.
- **Interfaz Gráfica:** Visualización en tiempo real de las colas y los clientes atendidos.

## Tecnologías Utilizadas

- **Lenguaje de Programación:** Python
- **Biblioteca Gráfica:** Tkinter
- **Estructuras de Datos:** Colas circulares personalizadas

## Instalación

1. **Clona este repositorio:**
   ```bash
   git clone git@github.com:SergioBohada99/cola_circular_banco.git
   ```
2. **Accede al directorio del proyecto:**
   ```bash
   cd cola_circular_banco
   ```
3. **Ejecuta la aplicación:**
   ```bash
   python gui.py
   ```

## Cómo Funciona

1. **Inicio de la Simulación:** Al ejecutar la aplicación, se crean de 2 a 4 cajeros, cada uno con su propia cola.
2. **Llegada de Clientes:** En cada generación, se genera un número aleatorio de clientes (entre 1 y 4) que son asignados a las colas de los cajeros.
3. **Atención de Clientes:** Los clientes son atendidos en orden FIFO:
   - Si un cliente tiene 5 o menos transacciones, es atendido completamente y eliminado de la cola.
   - Si un cliente tiene más de 5 transacciones, se le atienden 5 transacciones y regresa al final de la cola.
4. **Visualización:** La interfaz gráfica muestra el estado de cada cola y el progreso de la atención en tiempo real.
5. **Finalización:** Después de 4 generaciones de clientes, la simulación concluye.

## Interfaz Gráfica

La interfaz incluye:
- Un botón para iniciar la simulación.
- Un área de texto para mostrar el historial de eventos (clientes llegando, siendo atendidos, etc.).
- Marcos visuales para representar las colas de cada cajero, mostrando los clientes en espera.

## Ejemplo Visual

Al iniciar la aplicación, se muestra un mensaje inicial indicando el número de cajeros creados. Durante la simulación, puedes ver cómo los clientes ingresan y son atendidos en las colas.

## Estructura del Proyecto

```plaintext
cola_circular_banco/
├── controller/
│   ├── cola.py       # Implementación de la cola circular
│   ├── __init__.py
├── model/
│   ├── cliente.py    # Clase Cliente
│   ├── node.py       # Nodo para la cola
│   ├── __init__.py
├── gui.py            # Interfaz gráfica principal
└── README.md         # Documentación del proyecto
```

## Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad o corrección.
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz un commit.
   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```
4. Envía tus cambios al repositorio remoto.
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. Crea un Pull Request y describe tus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

¡Gracias por utilizar el Simulador de Banco con Colas Circulares! Si tienes preguntas o sugerencias, no dudes en abrir un issue en el repositorio.
