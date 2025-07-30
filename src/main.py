import os
import sys

# Importar las funciones desde el módulo functions
from functions.analizador_functions import analizar_carpetas

def mostrar_ayuda():
    """Mostrar información de ayuda"""
    print("=== ANALIZADOR DE TAMAÑO DE CARPETAS ===")
    print()
    print("Modos de uso:")
    print("  python src/main.py                    - Ejecutar interfaz gráfica")
    print("  python src/main.py --gui              - Ejecutar interfaz gráfica")
    print("  python src/main.py --cli [ruta]       - Modo línea de comandos")
    print("  python src/main.py [ruta]             - Modo línea de comandos")
    print("  python src/main.py --help             - Mostrar esta ayuda")
    print()
    print("Ejemplos:")
    print("  python src/main.py                    # Interfaz gráfica")
    print("  python src/main.py --cli Documents    # Analizar carpeta Documents")
    print("  python src/main.py C:\\Users\\paco_\\Downloads  # Ruta completa")

def modo_linea_comandos(ruta_analizar):
    """Ejecutar en modo línea de comandos"""
    print("=== ANALIZADOR DE TAMAÑO DE CARPETAS ===")
    print()
    
    # Verificar que la ruta existe
    if not os.path.exists(ruta_analizar):
        print(f"Error: La ruta '{ruta_analizar}' no existe.")
        print("Uso: python src/main.py [ruta]")
        return
    
    # Analizar las carpetas
    analizar_carpetas(ruta_analizar)

def modo_interfaz_grafica():
    """Ejecutar en modo interfaz gráfica"""
    try:
        from gui_interface import main as gui_main
        gui_main()
    except ImportError as e:
        print("❌ Error: No se pudo importar la interfaz gráfica.")
        print("Asegúrate de tener instaladas las dependencias:")
        print("  pip install -r requirements.txt")
        print()
        print("Error específico:", e)
    except Exception as e:
        print(f"❌ Error al ejecutar la interfaz gráfica: {e}")

def main():
    """
    Función principal del script
    """
    # Procesar argumentos de línea de comandos
    if len(sys.argv) == 1:
        # Sin argumentos: ejecutar interfaz gráfica
        modo_interfaz_grafica()
        return
    
    # Con argumentos
    primer_arg = sys.argv[1].lower()
    
    if primer_arg in ["--help", "-h", "help"]:
        mostrar_ayuda()
        return
    
    elif primer_arg in ["--gui", "-g", "gui"]:
        # Modo interfaz gráfica explícito
        modo_interfaz_grafica()
        return
    
    elif primer_arg in ["--cli", "-c", "cli"]:
        # Modo línea de comandos explícito
        if len(sys.argv) < 3:
            print("❌ Error: Debes especificar una ruta para el modo CLI.")
            print("Uso: python src/main.py --cli [ruta]")
            return
        ruta_analizar = sys.argv[2]
        modo_linea_comandos(ruta_analizar)
        return
    
    else:
        # Modo línea de comandos implícito (primer argumento es la ruta)
        ruta_analizar = sys.argv[1]
        modo_linea_comandos(ruta_analizar)
        return

if __name__ == "__main__":
    main()

