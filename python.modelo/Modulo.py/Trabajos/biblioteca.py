books = []

def agregar_books():
    titulo = input("Ingresa el titulo del libro: ")
    autor = input("Ingresa el Nombre del autor: ") 

    libros = {
        "titulo" : titulo,
        "autor" :  autor
    }

    books.append(libros)
    print("Agregado Correctamente")

def mostrar_books():

    
    if not books:
        print("No hay libros")
        return

    mostrar = input("Ingresa el nombre de el libro que solicita: ")

    for book in books:
        if book['titulo'] == mostrar:
            print(f"Su libro es: {book}")
            return
        
    print("No se encontro un libro con este nombre")

def eliminar_book():

    if not books:
        print("No se encontro ningun libro")
        return
        
    eliminar = input("Por favor ingresa el nombre del libro que quiere eliminar: ")

    for book in books:
        if book['titulo'] == eliminar:
            books.remove(book)
            print("el Libro se elimino correctamente")
            return
    print("No se encontro ningun libro con este nombre")

def edit_book():
    if not books:
        print("No hay Ningun libro agregado")
        return
    
    edit = input("Ingresa el titulo que quieres editar")

    for book in books:
        if book['titulo'] == edit:
            nuevo_titulo = input(f" nuevo titulo ({book['titulo']}): ")
            nuevo_autor = input(f"Nuevo Autor ({book['autor']}): ")

            if nuevo_titulo:
                book['titulo'] = nuevo_titulo
            if nuevo_autor:
                book['autor'] = nuevo_autor

            print("Libro actualizado correctamente")
            return

        print("No hay Libros con este nombre ")




def menu():
    while True:
        print("==BIENVENIDO==")
        print("1.Agregar Libro: ")
        print("2.Mostrar libro: ")
        print("3.Eliminar Libro: ")
        print("4.Editar Libro: ")
        print("5.Salir: ")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            agregar_books()
        elif opcion == "2":
            mostrar_books()
        elif opcion == "3":
            eliminar_book()
        elif opcion == "4":
            edit_book()
        elif opcion == "5":
            print("Saliendo del programa")
            break


menu()