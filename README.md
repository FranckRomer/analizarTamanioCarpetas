# 📁 Analizador de Tamaño de Carpetas

Una herramienta de línea de comandos en Python para analizar y mostrar el tamaño de las carpetas en tu sistema de archivos.

## 🚀 Características

- **Análisis completo**: Calcula el tamaño total de cada carpeta incluyendo todos los archivos y subcarpetas
- **Unidades legibles**: Muestra los tamaños en unidades apropiadas (B, KB, MB, GB, TB)
- **Ordenamiento inteligente**: Las carpetas se muestran ordenadas por tamaño (de mayor a menor)
- **Manejo robusto de errores**: Gestiona permisos, archivos inaccesibles y rutas inexistentes
- **Flexibilidad**: Permite especificar cualquier ruta o usar una ruta por defecto
- **Sin dependencias externas**: Utiliza solo módulos de la biblioteca estándar de Python
- **Arquitectura modular**: Código organizado en módulos separados para mejor mantenimiento
- **Interfaz interactiva**: Menú fácil de usar para seleccionar rutas comunes del sistema

## 📋 Requisitos

- Python 3.6 o superior
- Sistema operativo: Windows, macOS, o Linux

## 🛠️ Instalación

1. **Clona o descarga el proyecto**:
   ```bash
   git clone <url-del-repositorio>
   cd analizarTamanioCarpetas
   ```

2. **Instala las dependencias** (opcional, ya que no hay dependencias externas):
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Uso

### Modo interactivo (recomendado)
```bash
python src/main.py
```
Esto mostrará un menú interactivo donde podrás seleccionar la ruta a analizar:

```
=== ANALIZADOR DE TAMAÑO DE CARPETAS ===

Selecciona la ruta que deseas analizar:
1. Mi carpeta de usuario
2. Escritorio
3. Documentos
4. Descargas
5. Imágenes
6. Música
7. Videos
8. Ruta personalizada
9. Salir

Ingresa tu opción (1-9):
```

### Modo no interactivo (línea de comandos)
```bash
python src/main.py "C:\Users\paco_\Documents"
```

### Ejemplos de uso
```bash
# Modo interactivo (selecciona desde el menú)
python src/main.py

# Analizar el escritorio directamente
python src/main.py "C:\Users\paco_\Desktop"

# Analizar una unidad externa
python src/main.py "D:\"

# Analizar una carpeta específica
python src/main.py "C:\Users\paco_\Downloads"
```

## 📊 Ejemplo de salida

```
=== ANALIZADOR DE TAMAÑO DE CARPETAS ===

Analizando carpetas en: C:\Users\paco_
------------------------------------------------------------
Calculando tamaño de: Downloads...
Calculando tamaño de: Documents...
Calculando tamaño de: Pictures...
Calculando tamaño de: Desktop...

============================================================
RESULTADOS DEL ANÁLISIS
============================================================
 1. Downloads                          2.45 GB
 2. Documents                          1.23 GB
 3. Pictures                           856.32 MB
 4. Desktop                            234.56 MB
------------------------------------------------------------
TOTAL:                                   4.78 GB
```

## 🏗️ Estructura del proyecto

```
analizarTamanioCarpetas/
├── src/
│   └── main.py              # Punto de entrada principal
├── functions/
│   ├── __init__.py          # Hace que functions sea un módulo
│   └── analizador_functions.py  # Funciones del analizador
├── requirements.txt         # Dependencias del proyecto
└── README.md               # Este archivo
```

## 🔧 Funciones principales

### `obtener_tamaño_carpeta(ruta)` (en `functions/analizador_functions.py`)
Calcula el tamaño total de una carpeta en bytes, incluyendo todos los archivos y subcarpetas.

### `convertir_tamaño(tamaño_bytes)` (en `functions/analizador_functions.py`)
Convierte bytes a una unidad más legible (B, KB, MB, GB, TB).

### `analizar_carpetas(ruta_base)` (en `functions/analizador_functions.py`)
Analiza todas las carpetas en la ruta base y muestra su tamaño ordenado.

### `main()` (en `src/main.py`)
Función principal que maneja los argumentos de línea de comandos y coordina la ejecución.

## ⚠️ Consideraciones

- **Permisos**: El script necesita permisos de lectura en las carpetas que analiza
- **Tiempo de ejecución**: El análisis puede tomar tiempo en carpetas con muchos archivos
- **Memoria**: Para carpetas muy grandes, el script puede consumir memoria significativa

## 🐛 Solución de problemas

### Error: "No tienes permisos para acceder"
- Ejecuta el script como administrador
- Verifica que tienes permisos de lectura en la carpeta

### Error: "La ruta no existe"
- Verifica que la ruta especificada sea correcta
- Asegúrate de usar comillas si la ruta contiene espacios

### El script se ejecuta muy lento
- Esto es normal para carpetas con muchos archivos
- Considera analizar subcarpetas específicas en lugar de carpetas muy grandes

### Error de importación de módulos
- Asegúrate de ejecutar el script desde la raíz del proyecto
- Verifica que la estructura de carpetas sea correcta

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Paco** - Francisco Romero

---

⭐ Si este proyecto te ha sido útil, ¡dale una estrella!
