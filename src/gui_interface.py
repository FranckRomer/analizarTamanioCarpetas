import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import os
import threading
from functions.analizador_functions import obtener_tamaño_carpeta, convertir_tamaño, analizar_carpetas

class AnalizadorGUI:
    def __init__(self):
        # Configurar el tema de customtkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Crear la ventana principal
        self.root = ctk.CTk()
        self.root.title("Analizador de Tamaño de Carpetas")
        self.root.geometry("800x1000")
        self.root.resizable(True, True)
        
        # Variables
        self.ruta_seleccionada = tk.StringVar()
        self.analizando = False
        
        # Crear la interfaz
        self.crear_interfaz()
        
    def crear_interfaz(self):
        """Crear todos los elementos de la interfaz"""
        
        # Frame principal
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        titulo = ctk.CTkLabel(
            main_frame, 
            text="📁 Analizador de Tamaño de Carpetas",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        titulo.pack(pady=(20, 30))
        
        # Frame para selección de ruta
        ruta_frame = ctk.CTkFrame(main_frame)
        ruta_frame.pack(fill="x", padx=20, pady=10)
        
        # Etiqueta de ruta
        ruta_label = ctk.CTkLabel(ruta_frame, text="Ruta a analizar:", font=ctk.CTkFont(size=14))
        ruta_label.pack(anchor="w", padx=20, pady=(20, 5))
        
        # Frame para entrada de ruta y botón
        entrada_frame = ctk.CTkFrame(ruta_frame)
        entrada_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Entrada de ruta
        self.ruta_entry = ctk.CTkEntry(
            entrada_frame, 
            textvariable=self.ruta_seleccionada,
            placeholder_text="Selecciona una carpeta para analizar...",
            height=35
        )
        self.ruta_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        # Botón para seleccionar carpeta
        self.btn_seleccionar = ctk.CTkButton(
            entrada_frame,
            text="📂 Seleccionar",
            command=self.seleccionar_carpeta,
            height=35,
            width=120
        )
        self.btn_seleccionar.pack(side="right")
        
        # Frame para botones de rutas rápidas
        rutas_rapidas_frame = ctk.CTkFrame(main_frame)
        rutas_rapidas_frame.pack(fill="x", padx=20, pady=10)
        
        # Etiqueta
        rapidas_label = ctk.CTkLabel(rutas_rapidas_frame, text="Rutas rápidas:", font=ctk.CTkFont(size=14))
        rapidas_label.pack(anchor="w", padx=20, pady=(20, 10))
        
        # Botones de rutas rápidas
        botones_frame = ctk.CTkFrame(rutas_rapidas_frame)
        botones_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        rutas_rapidas = [
            ("🏠 Usuario", self.obtener_ruta_usuario()),
            ("🖥️ Escritorio", os.path.join(self.obtener_ruta_usuario(), "Desktop")),
            ("📄 Documentos", os.path.join(self.obtener_ruta_usuario(), "Documents")),
            ("⬇️ Descargas", os.path.join(self.obtener_ruta_usuario(), "Downloads")),
            ("🖼️ Imágenes", os.path.join(self.obtener_ruta_usuario(), "Pictures")),
            ("🎵 Música", os.path.join(self.obtener_ruta_usuario(), "Music")),
            ("🎬 Videos", os.path.join(self.obtener_ruta_usuario(), "Videos")),
        ]
        
        # Crear botones en filas de 3
        for i, (texto, ruta) in enumerate(rutas_rapidas):
            row = i // 3
            col = i % 3
            
            btn = ctk.CTkButton(
                botones_frame,
                text=texto,
                command=lambda r=ruta: self.seleccionar_ruta_rapida(r),
                height=30,
                width=120
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
        
        # Configurar columnas para que se expandan
        for i in range(3):
            botones_frame.columnconfigure(i, weight=1)
        
        # Botón de análisis
        self.btn_analizar = ctk.CTkButton(
            main_frame,
            text="🔍 Analizar Carpetas",
            command=self.iniciar_analisis,
            height=40,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.btn_analizar.pack(pady=20)
        
        # Frame para resultados
        resultados_frame = ctk.CTkFrame(main_frame)
        resultados_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Etiqueta de resultados
        resultados_label = ctk.CTkLabel(resultados_frame, text="Resultados:", font=ctk.CTkFont(size=14))
        resultados_label.pack(anchor="w", padx=20, pady=(20, 10))
        
        # Texto para mostrar resultados
        self.resultados_text = ctk.CTkTextbox(
            resultados_frame,
            wrap="word",
            font=ctk.CTkFont(size=12)
        )
        self.resultados_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Barra de progreso
        self.progress_bar = ctk.CTkProgressBar(resultados_frame)
        self.progress_bar.pack(fill="x", padx=20, pady=(0, 20))
        self.progress_bar.set(0)
        
        # Etiqueta de estado
        self.estado_label = ctk.CTkLabel(resultados_frame, text="Listo para analizar", font=ctk.CTkFont(size=12))
        self.estado_label.pack(pady=(0, 20))
        
    def obtener_ruta_usuario(self):
        """Obtener la ruta del directorio de usuario"""
        return os.path.expanduser("~")
    
    def seleccionar_carpeta(self):
        """Abrir diálogo para seleccionar carpeta"""
        ruta = filedialog.askdirectory(
            title="Seleccionar carpeta para analizar",
            initialdir=self.obtener_ruta_usuario()
        )
        if ruta:
            self.ruta_seleccionada.set(ruta)
    
    def seleccionar_ruta_rapida(self, ruta):
        """Seleccionar una ruta rápida"""
        if os.path.exists(ruta):
            self.ruta_seleccionada.set(ruta)
        else:
            messagebox.showwarning("Advertencia", f"La ruta {ruta} no existe en tu sistema.")
    
    def iniciar_analisis(self):
        """Iniciar el análisis en un hilo separado"""
        ruta = self.ruta_seleccionada.get().strip()
        
        if not ruta:
            messagebox.showerror("Error", "Por favor, selecciona una carpeta para analizar.")
            return
        
        if not os.path.exists(ruta):
            messagebox.showerror("Error", f"La ruta '{ruta}' no existe.")
            return
        
        if not os.path.isdir(ruta):
            messagebox.showerror("Error", f"'{ruta}' no es una carpeta válida.")
            return
        
        # Deshabilitar botones durante el análisis
        self.analizando = True
        self.btn_analizar.configure(state="disabled", text="⏳ Analizando...")
        self.btn_seleccionar.configure(state="disabled")
        self.progress_bar.set(0)
        self.estado_label.configure(text="Iniciando análisis...")
        
        # Limpiar resultados anteriores
        self.resultados_text.delete("1.0", "end")
        
        # Ejecutar análisis en hilo separado
        thread = threading.Thread(target=self.ejecutar_analisis, args=(ruta,))
        thread.daemon = True
        thread.start()
    
    def ejecutar_analisis(self, ruta):
        """Ejecutar el análisis en un hilo separado"""
        try:
            self.actualizar_estado("Obteniendo lista de carpetas...")
            self.progress_bar.set(0.1)
            
            # Obtener lista de carpetas
            elementos = os.listdir(ruta)
            carpetas = []
            
            for elemento in elementos:
                ruta_completa = os.path.join(ruta, elemento)
                if os.path.isdir(ruta_completa):
                    carpetas.append(elemento)
            
            if not carpetas:
                self.mostrar_resultado("No se encontraron carpetas en la ruta especificada.")
                return
            
            self.actualizar_estado(f"Analizando {len(carpetas)} carpetas...")
            self.progress_bar.set(0.2)
            
            # Analizar cada carpeta
            carpetas_info = []
            for i, carpeta in enumerate(carpetas):
                self.actualizar_estado(f"Calculando tamaño de: {carpeta}...")
                progreso = 0.2 + (0.7 * i / len(carpetas))
                self.progress_bar.set(progreso)
                
                ruta_carpeta = os.path.join(ruta, carpeta)
                tamaño = obtener_tamaño_carpeta(ruta_carpeta)
                carpetas_info.append((carpeta, tamaño))
            
            # Ordenar por tamaño
            carpetas_info.sort(key=lambda x: x[1], reverse=True)
            
            self.progress_bar.set(0.9)
            self.actualizar_estado("Generando reporte...")
            
            # Mostrar resultados
            self.mostrar_resultados_finales(ruta, carpetas_info)
            
            self.progress_bar.set(1.0)
            self.actualizar_estado("Análisis completado")
            
        except Exception as e:
            self.mostrar_resultado(f"Error durante el análisis: {str(e)}")
            self.actualizar_estado("Error en el análisis")
        finally:
            # Habilitar botones nuevamente
            self.root.after(0, self.finalizar_analisis)
    
    def actualizar_estado(self, mensaje):
        """Actualizar el mensaje de estado"""
        self.root.after(0, lambda: self.estado_label.configure(text=mensaje))
    
    def mostrar_resultado(self, mensaje):
        """Mostrar un mensaje en el área de resultados"""
        self.root.after(0, lambda: self.resultados_text.insert("end", mensaje + "\n"))
    
    def mostrar_resultados_finales(self, ruta_base, carpetas_info):
        """Mostrar los resultados finales del análisis"""
        resultado = f"=== ANALIZADOR DE TAMAÑO DE CARPETAS ===\n\n"
        resultado += f"Ruta analizada: {ruta_base}\n"
        resultado += f"Fecha: {os.popen('date /t').read().strip()}\n"
        resultado += "=" * 60 + "\n\n"
        resultado += "RESULTADOS DEL ANÁLISIS\n"
        resultado += "=" * 60 + "\n\n"
        
        for i, (nombre_carpeta, tamaño_bytes) in enumerate(carpetas_info, 1):
            tamaño_formateado = convertir_tamaño(tamaño_bytes)
            resultado += f"{i:2d}. {nombre_carpeta:<30} {tamaño_formateado:>15}\n"
        
        # Mostrar total
        tamaño_total = sum(tamaño for _, tamaño in carpetas_info)
        resultado += "-" * 60 + "\n"
        resultado += f"TOTAL: {convertir_tamaño(tamaño_total):>45}\n"
        
        self.root.after(0, lambda: self.resultados_text.delete("1.0", "end"))
        self.root.after(0, lambda: self.resultados_text.insert("1.0", resultado))
    
    def finalizar_analisis(self):
        """Finalizar el análisis y habilitar botones"""
        self.analizando = False
        self.btn_analizar.configure(state="normal", text="🔍 Analizar Carpetas")
        self.btn_seleccionar.configure(state="normal")
    
    def ejecutar(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()

def main():
    """Función principal para ejecutar la interfaz gráfica"""
    app = AnalizadorGUI()
    app.ejecutar()

if __name__ == "__main__":
    main() 