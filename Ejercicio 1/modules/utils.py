import os

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear") # Usar os.system para limpiar

def pause():
    input("\nPresione Enter para continuar...")