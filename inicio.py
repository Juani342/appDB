import tkinter as tk
from tkinter import messagebox
import requests


# Función para obtener el último registro del API
def obtener_ultimo_registro():
    try:
        # URL de la API
        url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"
        # Hacer la petición GET a la API
        response = requests.get(url)

        # Verificar si la petición fue exitosa
        if response.status_code == 200:
            # Convertir la respuesta en formato JSON
            datos = response.json()
            # Obtener el último registro (el más reciente)
            ultimo_registro = datos[-1]
            # Mostrar el último registro en la interfaz
            mostrar_datos(ultimo_registro)
        else:
            messagebox.showerror("Error", "No se pudo obtener los datos de la API.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")


# Función para mostrar los datos del último registro en la ventana
def mostrar_datos(registro):
    # Limpiar el contenido anterior del texto
    texto_datos.config(state=tk.NORMAL)
    texto_datos.delete(1.0, tk.END)

    # Formatear los datos del último registro de manera legible
    texto_datos.insert(tk.END, f"ID: {registro['id']}\n")
    texto_datos.insert(tk.END, f"Nombre: {registro['nombre']}\n")
    texto_datos.insert(tk.END, f"Apellido: {registro['apellido']}\n")
    texto_datos.insert(tk.END, f"Ciudad: {registro['ciudad']}\n")
    texto_datos.insert(tk.END, f"Calle: {registro['calle']}\n")

    # Desactivar la edición del texto
    texto_datos.config(state=tk.DISABLED)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Último registro del estudiante")
ventana.geometry("400x300")

# Etiqueta para el título
label_titulo = tk.Label(ventana, text="Último registro del estudiante", font=("Arial", 16))
label_titulo.pack(pady=10)

# Caja de texto para mostrar los datos
texto_datos = tk.Text(ventana, height=8, width=40, font=("Arial", 12))
texto_datos.pack(pady=10)

# Botón para obtener el último registro
boton_actualizar = tk.Button(ventana, text="Obtener último registro", command=obtener_ultimo_registro)
boton_actualizar.pack(pady=10)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()