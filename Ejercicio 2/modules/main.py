import modules.utils as u
import modules.messages as m
import modules.CRUD as c

def main():
    isActive = True
    while isActive:
        try:
            choice_entered = m.menu()
            match choice_entered:
                case "1":
                    c.add_books()

                case "2":
                    u.clear_screen()
                    c.view_library()
                    u.pause()

                case "3":
                    c.search_books()
                    
                case "4":
                    c.change_state()
                    u.pause()

                case "5":
                    c.reading_stats()
                    u.pause()

                case "6":
                    c.delete_books()
                    u.pause()

                case "0":
                    print("\n¡HASTA LUEGO! 👋")
                    print("Gracias por usar el gestor de biblioteca personal 😊.\n")
                    isActive = False

                case _:
                    print("\nError: Debe ingresar un número entre 0 y 6. Intente nuevamente.")
                    u.pause()
        except ValueError:
            print("\nError: Opción no válida. Intente nuevamente.")
            u.pause()