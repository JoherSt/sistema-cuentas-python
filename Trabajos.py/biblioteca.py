biblioteca = []

def agregar_books():
    titulo = input("Ingresa el titulo del libro: ")
    autor = input("Ingresa el Nombre del autor: ") 

    libros = {
        "titulo" : titulo,
        "autor" :  autor
    }

    biblioteca.append(libros)
    print("Agregado Correctamente")

def mostrar_books():

    
    if not biblioteca:
        print("No hay libros")
        return

    mostrar = input("Ingresa el nombre de el libro que solicita")

    for book in biblioteca:
        if book['nombre'] == mostrar:
            print(f"Su libro es: {book}")
            return
        
    print("No se encontro un libro con este nombre")