from AP8.tiendalibros.modelo.tienda_libros import TiendaLibros
from AP8.tiendalibros.modelo.libro_existente_error import LibroExistenteError
from AP8.tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from AP8.tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError

class UIConsola:
    def __init__(self):
        self.tienda = TiendaLibros()  # Inicializa la tienda de libros

    def ejecutar_app(self):
        while True:
            print("Bienvenido a la Tienda de Libros")
            print("1. Adicionar libro al catálogo")
            print("2. Agregar libro al carrito")
            print("3. Retirar libro del carrito")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.adicionar_un_libro_a_catalogo()
            elif opcion == '2':
                self.agregar_libro_a_carrito_de_compras()
            elif opcion == '3':
                self.retirar_libro_de_carrito_de_compras()
            elif opcion == '4':
                print("Gracias por visitar la tienda. ¡Hasta luego!")
                break
            else:
                print("Opción no válida, por favor intente nuevamente.")

    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            precio = float(input("Ingrese el precio del libro: "))
            existencias = int(input("Ingrese la cantidad de existencias: "))
            libro = self.tienda.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print(f"Libro '{libro.titulo}' agregado al catálogo con ISBN {libro.isbn}.")
        except LibroExistenteError as e:
            print(e)
        except ValueError:
            print("Error: Introduzca un valor válido para precio y existencias.")

    def agregar_libro_a_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el ISBN del libro que desea agregar al carrito: ")
            cantidad = int(input("Ingrese la cantidad: "))
            libro = self.tienda.catalogo.get(isbn)
            if libro:
                self.tienda.agregar_libro_a_carrito(libro, cantidad)
                print(f"Agregado {cantidad} unidades del libro '{libro.titulo}' al carrito.")
            else:
                print("El libro no está en el catálogo.")
        except LibroAgotadoError as e:
            print(e)
        except ExistenciasInsuficientesError as e:
            print(e)
        except ValueError:
            print("Error: Introduzca un valor válido para la cantidad.")

    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro que desea retirar del carrito: ")
        self.tienda.retirar_item_de_carrito(isbn)
        print(f"El libro con ISBN {isbn} ha sido retirado del carrito.")

