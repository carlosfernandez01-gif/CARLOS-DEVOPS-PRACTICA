from models.producto import ProductoElectronico, ProductoRopa
from services.tienda_service import TiendaService

def mostrar_inventario(tienda: TiendaService, titulo: str):
    print(f"\n--- {titulo} ---")
    for producto in tienda.listar_productos():
        print(producto)

def main():
    tienda = TiendaService()

    # Crear usuarios
    cliente1 = tienda.registrar_usuario("cliente", "Ana", "ana@mail.com", "Calle 1")
    cliente2 = tienda.registrar_usuario("cliente", "Luis", "luis@mail.com", "Calle 2")
    cliente3 = tienda.registrar_usuario("cliente", "Marta", "marta@mail.com", "Calle 3")
    admin = tienda.registrar_usuario("admin", "Root", "admin@mail.com")

    # Crear productos (mismo nombre, ids diferentes)
    prod1 = ProductoElectronico("Móvil", 299.99, 10, 24)
    prod2 = ProductoElectronico("Portátil", 1199.0, 5, 12)
    prod3 = ProductoRopa("Camiseta", 19.95, 50, "M", "Rojo")
    prod4 = ProductoRopa("Pantalón", 34.5, 40, "L", "Azul")
    prod5 = ProductoRopa("Chaqueta", 59.9, 20, "S", "Negro")

    for p in [prod1, prod2, prod3, prod4, prod5]:
        tienda.agregar_producto(p)

    mostrar_inventario(tienda, "Inventario inicial")

    # Realizar pedidos
    pedido1 = tienda.crear_pedido(cliente1.id, {prod1.id: 1, prod3.id: 2})
    pedido2 = tienda.crear_pedido(cliente2.id, {prod2.id: 1, prod5.id: 1})
    pedido3 = tienda.crear_pedido(cliente3.id, {prod4.id: 3})

    print("\n--- Pedidos realizados ---")
    print(pedido1)
    print()
    print(pedido2)
    print()
    print(pedido3)

    mostrar_inventario(tienda, "Inventario tras pedidos")

    print("\n--- Histórico de pedidos de Ana ---")
    for p in tienda.historial_pedidos_usuario(cliente1.id):
        print(p)

if __name__ == "__main__":
    main()