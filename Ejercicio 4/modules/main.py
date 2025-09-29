import modules.utils as u
import modules.messages as m
import modules.CRUD as c

def main():
    isActive = True
    while isActive:
        try:
            choice = m.menu()

            match choice:
                case "1":
                    c.registrar_usuario()
                    u.pause()

                case "2":
                    c.agregar_libro()
                    u.pause()

                case "3":
                    c.prestar_libro()
                    u.pause()

                case "4":
                    c.devolver_libro()
                    u.pause()

                case "5":
                    c.recomendar_libros()
                    u.pause()

                case "6":
                    c.analisis_usuarios()
                    u.pause()

                case "0":
                    print("\n¡HASTA LUEGO! 👋")
                    print("Gracias por usar el gestor de biblioteca 😊.\n")
                    isActive = False

                case _:
                    print("\nError: Debe ingresar un número entre 0 y 6. Intente nuevamente.")
                    u.pause()
        except ValueError:
            print("\nError: Opción no válida. Intente nuevamente.")
            u.pause()