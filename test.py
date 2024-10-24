import tkinter as tk
import requests


# Función para obtener el último registro desde la API
def obtener_ultimo_registro():
    try:
        url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"
        response = requests.get(url)
        response.raise_for_status() # Verifica si hubo un error en la solicitud
        data = response.json()

    # Obtiene el último registro
        if data:
            ultimo_registro = data[-1]
            mostrar_datos(ultimo_registro)
        else:
            resultado_label.config(text="No se encontraron registros.")
    except Exception as e:
        resultado_label.config(text=f"Error: {e}")


    # Función para mostrar los datos en la interfaz gráfica
def mostrar_datos(registro):
    texto = (
        f"ID: {registro['id']}\n"
        f"Nombre: {registro['nombre']}\n"
        f"Apellido: {registro['apellido']}\n"
        f"Ciudad: {registro['ciudad']}\n"
        f"Calle: {registro['calle']}"
        )
    resultado_label.config(text=texto)


# Configuración de la interfaz gráfica
app = tk.Tk()
app.title("Último Registro Estudiante")
app.geometry("300x200")

# Botón para obtener el último registro
boton = tk.Button(app, text="Obtener Último Registro", command=obtener_ultimo_registro)
boton.pack(pady=10)

# Label para mostrar los resultados
resultado_label = tk.Label(app, text="", justify="left")
resultado_label.pack(pady=10)

# Iniciar la aplicación
app.mainloop()