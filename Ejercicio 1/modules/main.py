import modules.utils as u
import modules.messages as m
import modules.CRUD as c

def main():
    isActive = True 
    while isActive: # Usar while con booleano
        u.clear_screen()
        choice = m.menu()
        
        match choice:
            case 1:
                c.add_game()

            case 2:
                c.view_games()
                u.pause()
                
            case 3:
                c.complete_game()
                u.pause()
                
            case 4:
                c.show_stats()
                u.pause()
                
            case 0:
                print("Gracias por usar el sistema de gestión de videojuegos ¡Hasta luego!")
                isActive=False
                
            case _:
                print("\nOpción no válida. Intente nuevamente.")
                u.pause()