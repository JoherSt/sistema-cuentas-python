
import getpass

def pedir_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor ingresa un valor válido.")


def pedir_correo(mensaje):
    while True:
        correo = input(mensaje).strip().lower()
        if "@gmail.com" in correo:
            return correo
        else:
            print("El correo debe contener @gmail.com")


def pedir_contraseña(mensaje):
    while True:
        contraseña = getpass.getpass(mensaje)
        confirmar = getpass.getpass("Confirma la contraseña: ")

        if contraseña == confirmar:
            return contraseña
        else:
            print("Las contraseñas no coinciden.")


