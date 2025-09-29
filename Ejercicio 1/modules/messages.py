import modules.utils as u

def menu():
    try:
        u.clear_screen()
        print("SISTEMA DE INVENTARIO DE VIDEOJUEGOS")
        print("." * 60)
        print("\n~~ MENÚ DE OPCIONES ~~\n") # Mostrar opciones, retornar choice
        print("1. Agregar juego")
        print("2. Ver colección de juegos")
        print("3. Marcar completados")
        print("4. Estadisticas básicas")
        print("0. Salir\n")
        opcion = int(input("Ingrese una opción (0-4): "))
        return opcion # Usar input() y return
    except ValueError:
        print("\nError: Opción no válida. Intente nuevamente.")
        u.pause()
        return None