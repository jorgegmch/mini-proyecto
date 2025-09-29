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
                    c.registrar_estudiante()
                    u.pause()

                case "2":
                    c.agregar_materia()
                    u.pause()

                case "3":
                    c.inscribir_materia()
                    u.pause()

                case "4":
                    c.registrar_calificacion()
                    u.pause()
                case "5":
                    c.materias_comunes()
                    u.pause()

                case "6":
                    c.generar_reporte()
                    u.pause()

                case "0":
                    print("\n¡HASTA LUEGO! 👋")
                    print("Gracias por usar este gestor académico 😊.\n")
                    isActive = False

                case _:
                    print("\nError: Debe ingresar un número entre 0 y 6. Intente nuevamente.")
                    u.pause()
        except ValueError:
            print("\nError: Opción no válida. Intente nuevamente.")
            u.pause()