import os
import sys
from pathlib import Path

def obtener_tamaño_carpeta(ruta):
    """
    Calcula el tamaño total de una carpeta en bytes
    """
    tamaño_total = 0
    try:
        for ruta_actual, carpetas, archivos in os.walk(ruta):
            for archivo in archivos:
                ruta_archivo = os.path.join(ruta_actual, archivo)
                try:
                    tamaño_total += os.path.getsize(ruta_archivo)
                except (OSError, FileNotFoundError):
                    continue
    except (OSError, PermissionError):
        print(f"No se puede acceder a la carpeta: {ruta}")
        return 0
    
    return tamaño_total

def convertir_tamaño(tamaño_bytes):
    """
    Convierte bytes a una unidad más legible (KB, MB, GB, etc.)
    """
    for unidad in ['B', 'KB', 'MB', 'GB', 'TB']:
        if tamaño_bytes < 1024.0:
            return f"{tamaño_bytes:.2f} {unidad}"
        tamaño_bytes /= 1024.0
    return f"{tamaño_bytes:.2f} PB"

def analizar_carpetas(ruta_base):
    """
    Analiza todas las carpetas en la ruta base y muestra su tamaño
    """
    print(f"Analizando carpetas en: {ruta_base}")
    print("-" * 60)
    
    try:
        # Obtener la lista de elementos en la ruta
        elementos = os.listdir(ruta_base)
        
        carpetas_info = []
        
        for elemento in elementos:
            ruta_completa = os.path.join(ruta_base, elemento)
            
            # Verificar si es una carpeta
            if os.path.isdir(ruta_completa):
                print(f"Calculando tamaño de: {elemento}...")
                tamaño = obtener_tamaño_carpeta(ruta_completa)
                carpetas_info.append((elemento, tamaño))
        
        # Ordenar por tamaño (de mayor a menor)
        carpetas_info.sort(key=lambda x: x[1], reverse=True)
        
        print("\n" + "=" * 60)
        print("RESULTADOS DEL ANÁLISIS")
        print("=" * 60)
        
        if not carpetas_info:
            print("No se encontraron carpetas en la ruta especificada.")
            return
        
        for i, (nombre_carpeta, tamaño_bytes) in enumerate(carpetas_info, 1):
            tamaño_formateado = convertir_tamaño(tamaño_bytes)
            print(f"{i:2d}. {nombre_carpeta:<30} {tamaño_formateado:>15}")
        
        # Mostrar total
        tamaño_total = sum(tamaño for _, tamaño in carpetas_info)
        print("-" * 60)
        print(f"TOTAL: {convertir_tamaño(tamaño_total):>45}")
        
    except FileNotFoundError:
        print(f"Error: La ruta '{ruta_base}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permisos para acceder a '{ruta_base}'.")

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
        print("Uso: python analizador.py [ruta]")
        return
    
    # Analizar las carpetas
    analizar_carpetas(ruta_analizar)

if __name__ == "__main__":
    main()



