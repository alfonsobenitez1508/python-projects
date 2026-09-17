from src.menu import menu_principal, ejecutar


def main():
    seguir = True
    while seguir:
        opcion = menu_principal()
        seguir = ejecutar(opcion)
        

if __name__ == "__main__":
    main()