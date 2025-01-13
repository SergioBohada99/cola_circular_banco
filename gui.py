import tkinter as tk
import random
from tkinter import ttk
import time 
from controller.cola import ColaCircular
from model.node import Nodo
from model.cliente import Cliente

class AppBanco(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulación Bancaria con Múltiples Cajeros")
        self.geometry("900x600")

        self.max_generaciones = 4      # Número máximo de generaciones
        self.contador_clientes = 1     # ID unico de cliente 
        self.en_proceso = False        # Control para no duplicar ejecuciones

        # Número aleatorio de cajeros (entre 2 y 4)
        self.num_cajeros = random.randint(2, 4)

        # Creamos una lista de colas, una por cajero
        self.colas = [ColaCircular() for _ in range(self.num_cajeros)]

        # ----------------------------
        # Construcción de la Interfaz
        # ----------------------------
        self.frame_botones = ttk.Frame(self)
        self.frame_botones.pack(pady=5)

        # Botón de iniciar simulación
        self.boton_iniciar = ttk.Button(
            self.frame_botones, 
            text="Iniciar Simulación", 
            command=self.iniciar_simulacion
        )
        self.boton_iniciar.grid(row=0, column=0, padx=5)

        # Texto para mostrar resultados (historial)
        self.text_area = tk.Text(self, width=100, height=15)
        self.text_area.pack(pady=5)

        # Etiqueta para mostrar estado
        self.label_estado = ttk.Label(self, text="Estado: Sin iniciar")
        self.label_estado.pack()

        # Frame principal que contendrá la visual de cada cajero
        self.frame_cajeros = ttk.Frame(self)
        self.frame_cajeros.pack(pady=10)

        # Subframes para cada cajero (filas)
        # Cada cajero tendrá su propio frame donde veremos los bloques de la cola
        self.frames_cajeros = []
        for i in range(self.num_cajeros):
            # Creamos un Frame por cajero
            marco = ttk.Frame(self.frame_cajeros)
            marco.pack(pady=5, fill=tk.X)

            # Etiqueta de "Cajero i"
            lbl = ttk.Label(marco, text=f"Cajero #{i+1}: ")
            lbl.pack(side=tk.LEFT, padx=5)

            # Frame interno para la cola de este cajero
            frame_cola = ttk.Frame(marco)
            frame_cola.pack(side=tk.LEFT)
            
            # Guardamos ese frame para dibujarle la cola
            self.frames_cajeros.append(frame_cola)

        # Mensaje inicial
        self.imprimir_texto(f"Se crearon {self.num_cajeros} cajeros (entre 2 y 4).\n")
        self.imprimir_texto("Presiona 'Iniciar Simulación' para comenzar.\n")

    # ---------------------------------------------------------------
    # Función para imprimir texto en el Text de la interfaz
    # ---------------------------------------------------------------
    def imprimir_texto(self, texto):
        self.text_area.insert(tk.END, texto)
        self.text_area.see(tk.END)

    # ---------------------------------------------------------------
    # Función para visualizar la cola de cada cajero
    # ---------------------------------------------------------------
    def actualizar_vista_cajeros(self):
        """
        Limpia cada Frame de cajero y dibuja bloques
        representando a los clientes que están en la cola.
        """
        for i in range(self.num_cajeros):
            # Limpiamos el frame del cajero i
            for widget in self.frames_cajeros[i].winfo_children():
                widget.destroy()

            # Recorremos la cola del cajero i
            for cliente in self.colas[i]:
                texto = f"C{cliente.id_cliente}\n({cliente.transacciones})"
                bloque = tk.Label(
                    self.frames_cajeros[i],
                    text=texto,
                    bg="lightblue",
                    width=8,
                    height=3,
                    borderwidth=2,
                    relief="solid"
                )
                bloque.pack(side=tk.LEFT, padx=2, pady=2)

    # ---------------------------------------------------------------
    # Inicia la simulación
    # ---------------------------------------------------------------
    def iniciar_simulacion(self):
        if not self.en_proceso:
            self.en_proceso = True
            self.label_estado.config(text="Estado: Simulación en progreso")
            self.imprimir_texto("Iniciando simulación...\n")

            # Ejecutamos las generaciones en un bucle
            for gen in range(1, self.max_generaciones + 1):
                self.imprimir_texto(f"\n*** GENERACIÓN {gen} ***\n")
                self.label_estado.config(text=f"Estado: Generación {gen} de {self.max_generaciones}")

                # Llegada de clientes a las distintas colas
                self.llegada_clientes()

                # Atender todas las colas
                self.atender_colas_paso_a_paso()

                # Pequeña pausa para que se note la transición de generación
                self.update()
                time.sleep(2)

            self.imprimir_texto("\nSe alcanzó el número máximo de generaciones.\n")
            self.label_estado.config(text="Estado: Simulación finalizada")
            self.en_proceso = False
        else:
            self.imprimir_texto("La simulación ya está en curso.\n")

    # ---------------------------------------------------------------
    # Llegada de clientes
    # ---------------------------------------------------------------
    def llegada_clientes(self):
        """
        Genera un número aleatorio (1 a 4) de clientes nuevos.
        Asigna cada cliente a la cola de un cajero aleatorio.
        """
        num_clientes_nuevos = random.randint(1, 4)
        self.imprimir_texto(f"Llegan {num_clientes_nuevos} clientes nuevos.\n")

        for _ in range(num_clientes_nuevos):
            transacciones = random.randint(1, 10)
            nuevo_cliente = Cliente(self.contador_clientes, transacciones)

            # Elegimos un cajero aleatorio (índice) para encolar
            cajero_aleatorio = random.randint(0, self.num_cajeros - 1)
            self.colas[cajero_aleatorio].encolar(nuevo_cliente)

            self.imprimir_texto(
                f"  -> Entra a la cola del cajero #{cajero_aleatorio+1}: {nuevo_cliente}\n"
            )
            self.contador_clientes += 1

        # Actualizamos la vista después de agregar
        self.actualizar_vista_cajeros()

    # ---------------------------------------------------------------
    # Atender todas las colas paso a paso
    # ---------------------------------------------------------------
    def atender_colas_paso_a_paso(self):
        """
        Procesa cada cola, sacando cliente por cliente:
         - Si tiene <= 5 transacciones, se retira
         - Si tiene > 5, se atienden 5 y vuelve al final
        Mostramos la animación paso a paso.
        """
        # Podríamos atender cola por cola en un bucle,
        # repitiendo hasta que todas estén vacías, o hacerlo 
        # en "rondas". Aquí se hará un while de seguridad.

        limite_seguridad = 200
        contador = 0

        while contador < limite_seguridad:
            # Verificamos si TODAS las colas están vacías
            if all(c.esta_vacia() for c in self.colas):
                self.imprimir_texto("Todas las colas están vacías.\n")
                break

            # Recorremos cada cola y atendemos un cliente (si lo hay)
            for i, cola_cajero in enumerate(self.colas):
                if cola_cajero.esta_vacia():
                    continue  # No atendemos nada en una cola vacía

                cliente_actual = cola_cajero.desencolar()
                if cliente_actual is None:
                    continue

                if cliente_actual.transacciones <= 5:
                    self.imprimir_texto(
                        f"Atendiendo COMPLETAS a {cliente_actual} en Cajero #{i+1}. Se retira.\n"
                    )
                else:
                    self.imprimir_texto(
                        f"Atendiendo PARCIAL (5) a {cliente_actual} en Cajero #{i+1}.\n"
                    )
                    cliente_actual.transacciones -= 5
                    cola_cajero.encolar(cliente_actual)
                    self.imprimir_texto(
                        f"    -> {cliente_actual} regresa al final de la cola de Cajero #{i+1}.\n"
                    )

                # Refrescamos la vista y esperamos un instante
                self.actualizar_vista_cajeros()
                self.update()
                time.sleep(1)

            contador += 1

        if contador >= limite_seguridad:
            self.imprimir_texto("Advertencia: límite de seguridad alcanzado.\n")


# ---------------------------------------------------------------
# Ejecución de la aplicación
# ---------------------------------------------------------------
if __name__ == "__main__":
    app = AppBanco()
    app.mainloop()
