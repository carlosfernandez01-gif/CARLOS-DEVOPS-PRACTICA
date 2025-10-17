import uuid
from datetime import datetime
from typing import Dict, Tuple
from models.usuario import Cliente
from models.producto import Producto

class Pedido:
    """Representa un pedido realizado por un cliente.

    - productos: diccionario {Producto: cantidad}
    """
    def __init__(self, cliente: Cliente, productos: Dict[Producto, int]):
        self.id = str(uuid.uuid4())
        self.fecha = datetime.now()
        self.cliente = cliente
        self.productos = productos

    def calcular_subtotal(self) -> float:
        return round(sum(prod.precio * cant for prod, cant in self.productos.items()), 2)

    def calcular_totales(self, iva: float = 0.21) -> Tuple[float, float, float]:
        """Devuelve (subtotal, iva_eur, total) con dos decimales."""
        subtotal = self.calcular_subtotal()
        iva_eur = round(subtotal * iva, 2)
        total = round(subtotal + iva_eur, 2)
        return subtotal, iva_eur, total

    def __str__(self) -> str:
        productos_str = "\n".join(
            f"- {prod.nombre} x{cant} = {round(prod.precio * cant, 2)}€"
            for prod, cant in self.productos.items()
        )
        subtotal, iva_eur, total = self.calcular_totales()
        return (
            f"Pedido {self.id} ({self.fecha.strftime('%Y-%m-%d %H:%M')})\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Productos:\n{productos_str}\n"
            f"Subtotal: {subtotal}€\n"
            f"IVA (21%): {iva_eur}€\n"
            f"Total: {total}€"
        )