import os
import sys

# Importar las funciones desde el módulo functions
from functions.analizador_functions import analizar_carpetas

def main():
    """
    Función principal del script
    """
    # Ruta por defecto (puedes cambiarla)
    ruta_por_defecto = r"C:\Users\paco_"
    
    # Verificar si se proporcionó una ruta como argumento
    if len(sys.argv) > 1:
        ruta_analizar = sys.argv[1]
    else:
        ruta_analizar = ruta_por_defecto
    
    print("=== ANALIZADOR DE TAMAÑO DE CARPETAS ===")
    print()
    
    # Verificar que la ruta existe
    if not os.path.exists(ruta_analizar):
        print(f"Error: La ruta '{ruta_analizar}' no existe.")
        print("Uso: python src/main.py [ruta]")
        return
    
    # Analizar las carpetas
    analizar_carpetas(ruta_analizar)

if __name__ == "__main__":
    main()

