import uuid

class Producto:
    """Clase base para los productos.

    Reglas:
      - El precio no puede ser negativo.
      - El stock no puede ser negativo tras una operación.
    """
    def __init__(self, nombre: str, precio: float, stock: int):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if stock < 0:
            raise ValueError("El stock inicial no puede ser negativo")
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)

    def tiene_stock(self, cantidad: int) -> bool:
        """Devuelve True si hay 'cantidad' disponible en inventario."""
        return self.stock >= cantidad

    def modificar_stock(self, cantidad: int) -> None:
        """Modifica el stock (positivo repone, negativo descuenta)."""
        nuevo = self.stock + int(cantidad)
        if nuevo < 0:
            raise ValueError("La operación dejaría el stock en negativo")
        self.stock = nuevo

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} - {self.precio}€ (Stock: {self.stock})"


class ProductoElectronico(Producto):
    """Producto electrónico con garantía (meses)."""
    def __init__(self, nombre: str, precio: float, stock: int, garantia: int):
        super().__init__(nombre, precio, stock)
        self.garantia = int(garantia)

    def __str__(self) -> str:
        return (f"[{self.id}] {self.nombre} - {self.precio}€ "
                f"(Stock: {self.stock}), Garantía: {self.garantia} meses")


class ProductoRopa(Producto):
    """Producto de ropa con talla y color."""
    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str):
        super().__init__(nombre, precio, stock)
        self.talla = talla
        self.color = color

    def __str__(self) -> str:
        return (f"[{self.id}] {self.nombre} - {self.precio}€ "
                f"(Stock: {self.stock}), Talla: {self.talla}, Color: {self.color}")