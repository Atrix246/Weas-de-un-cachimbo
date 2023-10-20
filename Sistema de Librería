class SistemaLibreria:

    def __init__(self):
        self.inventario = {}

        self.agregar_libro("la ciudad y los perros","Mario Vargas Llosa","Seix Barral","I","Disponible")
        self.agregar_libro("paco yunque","César Vallejo","Apuntes Del hombre","I","Disponible")

    def agregar_libro (self,titulo,autor,editorial,version,estado):
        self.inventario[titulo] = {
            'autor':autor,
            'editorial':editorial,
            'version':version,
            'estado':estado
            }

    def prestar_libro (self,titulo):
        if titulo in self.inventario:
            if self.inventario[titulo]['estado'] == "Disponible":
                self.inventario[titulo]['estado'] = "Prestado"
                print(f"{titulo} ha sido prestado")
            else:
                print(f"El libro '{titulo}' no se encuentra disponible")
        else:
            print(f"El libro '{titulo}' no está en el inventario")

    def devolver_libro(self,titulo):
        if titulo in self.inventario:
            if self.inventario[titulo]['estado'] == "Prestado":
                self.inventario[titulo]['estado'] = "Disponible"
                print(f"Se devolvió el libro '{titulo}'.")
            else:
                print(f"El libro '{titulo}' no está prestado")
        else:
            print(f"El libro '{titulo}' no se encuentra en la lista")

    def libros_disponibles(self):
        print("---Libros Disponibles---")
        for titulo, info in self.inventario.items():
            print (f"Título: {titulo}, Autor: {info['autor']}, Editorial: {info['editorial']}, Versión: {info['version']}, Estado {info['estado']}")

almacen = SistemaLibreria()
while True:
    opcion = input ("""\nBienvenido(a) ¿Qué desea hacer?
    1. Agregar Libro
    2. Prestar Libro
    3. Devolver Libro
    4. Lista de Libros Disponibles
    5. Salir
""")
    if opcion == "1":
        titulo = (input("Ingrese el título del libro: ")).lower()
        autor = input("Ingrese el autor del libro: ")
        editorial = input("Ingrese la editorial del libro: ")
        version = input("Ingrese la versión del libro: ")
        estado = "Disponible"
        almacen.agregar_libro(titulo, autor, editorial, version, estado)
        print(f"\n'{titulo}' HA SIDO AGREGRADO.\n")
    
    elif opcion == "2":
        titulo = (input("Ingrese el título del libro a prestar: ")).lower()
        almacen.prestar_libro(titulo)
        
    elif opcion == "3":
        titulo = (input("Ingrese el libro a devolver: ")).lower()
        almacen.devolver_libro(titulo)

    elif opcion == "4":
        almacen.libros_disponibles()
    
    elif opcion == "5":
        print("Saliendo del programa ...")
        break

    else:
        print("\nOpción no válida, INGRESE OTRO VALOR")
