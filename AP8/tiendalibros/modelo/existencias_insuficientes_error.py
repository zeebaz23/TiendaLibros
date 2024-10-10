from AP8.tiendalibros.modelo.libro_error import LibroError

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, libro, cantidad_a_comprar):
        super().__init__(libro)
        self.cantidad_a_comprar = cantidad_a_comprar

    def __str__(self):
        return (f"El libro con título '{self.libro.titulo}' y ISBN: {self.libro.isbn} "
                f"no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, "
                f"existencias: {self.libro.existencias}")
