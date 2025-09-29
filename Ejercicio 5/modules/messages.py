import modules.utils as u

def menu():
    u.clear_screen()
    print("SISTEMA DE GESTIÓN DE TIENDA DE VIDEOJUEGOS")
    print("-" * 50)
    print("\n~~ MENÚ DE OPCIONES ~~\n")
    print("1. Inventario")
    print("2. Clientes")
    print("3. Empleados")
    print("4. Ventas")
    print("5. Reportes")
    print("6. Configuración")
    print("0. Salir")
    option = input("\n>>> Ingrese una opción (0-6): ")
    return option