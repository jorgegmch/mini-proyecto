import modules.utils as u
import modules.messages as m
import modules.CRUD as c

def main():
    activo = True
    while activo:
        try:
            u.clear_screen()
            opcion = m.menu()
            match opcion:
                case "1":
                    c.menu_inventario()
                case "2":
                    c.menu_clientes()
                case "3":
                    c.menu_empleados()
                case "4":
                    c.menu_ventas()
                case "5":
                    c.menu_reportes()
                case "6":
                    c.menu_configuracion()
                case "0":
                    print("\n¡HASTA LUEGO! 👋")
                    print("Gracias por usar este sistema de gestión.\n")
                    activo = False
                case _:
                    print("\nError: Debe ingresar un número entre 0 y 6. Intente nuevamente.")
                    u.pause()
        except Exception:
            print("\nError: Ocurrió un problema. Intente nuevamente.")
            u.pause()