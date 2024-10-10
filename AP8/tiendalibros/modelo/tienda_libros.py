from AP8.tiendalibros.modelo.libro import Libro
from AP8.tiendalibros.modelo.libro_existente_error import LibroExistenteError
from AP8.tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from AP8.tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from AP8.tiendalibros.modelo.carro_compra import CarroCompras

class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int):
        if isbn in self.catalogo:
            raise LibroExistenteError(self.catalogo[isbn])
        libro = Libro(titulo, isbn, precio, existencias)
        self.catalogo[isbn] = libro
        return libro

    def agregar_libro_a_carrito(self, libro: Libro, cantidad: int):
        if libro.existencias <= 0:
            raise LibroAgotadoError(libro)
        if libro.existencias < cantidad:
            raise ExistenciasInsuficientesError(libro, cantidad)
        self.carrito.agregar_item(libro, cantidad)
        libro.existencias -= cantidad

    def retirar_item_de_carrito(self, isbn: str):
        self.carrito.quitar_item(isbn)
