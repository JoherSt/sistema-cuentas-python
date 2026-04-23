from paquete.libros import agregar_books, mostrar_books, eliminar_book, edit_book

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