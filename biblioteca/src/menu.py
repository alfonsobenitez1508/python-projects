from src.datos import libros, usuarios, prestamos
from src.funciones import (
    agregar_libro, buscar_libros, estadisticas_libros, libros_disponibles,
    registrar_usuario, realizar_prestamo, devolver_libro, recomendar_libros,
)


def validar_opcion():
    while True:
        try:
            opcion = int(input())
        except ValueError:
            print("El argumento debe ser un número entero dentro de la lista: ")
            continue
        if 0 <= opcion < 11:
            return opcion
        print("El argumento debe ser un número entero dentro de la lista: ")


def menu_principal():
    """Despliega el menú y devuelve la opción elegida."""
    print("=" * 60)
    print("MENÚ PRINCIPAL")
    print("=" * 60 + "\n")
    print(
        "Digita el número correspondiente: \n"
        "1. Ver todos los libros \n"
        "2. Buscar libros \n"
        "3. Agregar un libro \n"
        "4. Ver usuarios \n"
        "5. Registrar usuario \n"
        "6. Realizar un préstamo \n"
        "7. Devolver libro \n"
        "8. Ver préstamos activos \n"
        "9. Ver estadísticas \n"
        "10. Ver recomendaciones \n"
        "0. Salir \n"
    )
    return validar_opcion()


def ejecutar(opcion):
    """Ejecuta la acción correspondiente. Devuelve True si seguir, False si salir."""
    if opcion == 0:
        print("Terminando sesión...")
        return False

    acciones = {
        1: lambda: print(libros),
        2: lambda: print(buscar_libros(
            input("Campo: "), input("Valor: "))),
        3: lambda: print(agregar_libro(
            input("Título: "), input("Autor: "),
            input("Género: "), input("Año: "))),
        4: lambda: print(usuarios),
        5: lambda: print(registrar_usuario(
            input("Nombre: "), input("Email: "))),
        6: lambda: print(realizar_prestamo(
            input("ID usuario: "), input("ID libro: "))),
        7: lambda: print(devolver_libro(
            input("ID usuario: "), input("ID libro: "))),
        8: lambda: print(prestamos),
        9: lambda: print(estadisticas_libros()),
        10: lambda: print(recomendar_libros(
            input("ID usuario: "), input("Número de recomendaciones: "))),
    }

    accion = acciones.get(opcion)
    if accion:
        accion()
        input("Presiona enter para continuar")
        return True
