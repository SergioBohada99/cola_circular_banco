from model.node import Nodo

class ColaCircular:
    def __init__(self):
        self.frente = None
        self.final = None

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, cliente):
        """Inserta un cliente al final de la cola."""
        nuevo_nodo = Nodo(cliente)
        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
            self.final.siguiente = self.frente
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
            self.final.siguiente = self.frente

    def desencolar(self):
        """Retira y retorna el cliente del frente de la cola."""
        if self.esta_vacia():
            return None
        cliente_eliminado = self.frente.cliente
        if self.frente == self.final:
            # Solo había un nodo
            self.frente = None
            self.final = None
        else:
            self.frente = self.frente.siguiente
            self.final.siguiente = self.frente
        return cliente_eliminado

    def __iter__(self):
        """Permite iterar sobre la cola para visualizarla."""
        if not self.esta_vacia():
            nodo_actual = self.frente
            while True:
                yield nodo_actual.cliente
                if nodo_actual == self.final:
                    break
                nodo_actual = nodo_actual.siguiente