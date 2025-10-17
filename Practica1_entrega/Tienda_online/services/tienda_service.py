from typing import Dict, List, Optional
from models.usuario import Usuario, Cliente, Administrador
from models.producto import Producto
from models.pedido import Pedido

class TiendaService:
    """Servicio central de gestión de usuarios, inventario y pedidos."""
    def __init__(self):
        self.usuarios: Dict[str, Usuario] = {}
        self.productos: Dict[str, Producto] = {}
        self.pedidos: List[Pedido] = []

    # --------- USUARIOS ---------
    def registrar_usuario(self, tipo: str, nombre: str, email: str, direccion: str = "") -> Usuario:
        """Crea y registra un usuario de tipo 'cliente' o 'admin'."""
        tipo = tipo.lower().strip()
        if tipo == "cliente":
            usuario = Cliente(nombre, email, direccion)
        elif tipo == "admin":
            usuario = Administrador(nombre, email)
        else:
            raise ValueError("Tipo de usuario no válido (use 'cliente' o 'admin')")
        self.usuarios[usuario.id] = usuario
        return usuario

    def listar_usuarios(self) -> List[Usuario]:
        """Devuelve todos los usuarios registrados."""
        return list(self.usuarios.values())

    # --------- PRODUCTOS ---------
    def agregar_producto(self, producto: Producto) -> None:
        self.productos[producto.id] = producto

    def eliminar_producto(self, producto_id: str) -> None:
        if producto_id in self.productos:
            del self.productos[producto_id]

    def listar_productos(self) -> List[Producto]:
        return list(self.productos.values())

    def buscar_producto_por_nombre(self, nombre: str) -> Optional[Producto]:
        """Devuelve el primer producto que coincida por nombre (case-insensitive)."""
        nombre_l = nombre.lower()
        for p in self.productos.values():
            if p.nombre.lower() == nombre_l:
                return p
        return None

    # --------- PEDIDOS ---------
    def crear_pedido(self, cliente_id: str, items: Dict[str, int]) -> Pedido:
        """Crea un pedido validando cliente y stock. items = {producto_id: cantidad}"""
        if cliente_id not in self.usuarios or not isinstance(self.usuarios[cliente_id], Cliente):
            raise ValueError("Cliente no válido")

        cliente = self.usuarios[cliente_id]
        productos_pedido: Dict[Producto, int] = {}

        for prod_id, cantidad in items.items():
            if prod_id not in self.productos:
                raise ValueError(f"Producto {prod_id} no encontrado")
            producto = self.productos[prod_id]
            if not producto.tiene_stock(cantidad):
                raise ValueError(f"Stock insuficiente para {producto.nombre}")
            producto.modificar_stock(-cantidad)
            productos_pedido[producto] = int(cantidad)

        pedido = Pedido(cliente, productos_pedido)
        self.pedidos.append(pedido)
        return pedido

    def historial_pedidos_usuario(self, cliente_id: str) -> List[Pedido]:
        """Devuelve los pedidos de un cliente por orden de fecha (más antiguos primero)."""
        return [p for p in self.pedidos if p.cliente.id == cliente_id]