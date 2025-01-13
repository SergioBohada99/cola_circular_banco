class Cliente:
    def __init__(self, id_cliente, transacciones):
        self.id_cliente = id_cliente
        self.transacciones = transacciones  # número de transacciones pendientes

    def __str__(self):
        return f"Cliente {self.id_cliente} - Transacciones: {self.transacciones}"

