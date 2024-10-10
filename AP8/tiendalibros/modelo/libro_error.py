from AP8.tiendalibros.modelo.libro import Libro

class LibroError(Exception):
    def __init__(self, libro: Libro):
        self.libro = libro

    def __str__(self):
        return f"Error relacionado con el libro: {self.libro.titulo}, ISBN: {self.libro.isbn}"
