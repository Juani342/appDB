import tkinter as tk
import requests


def obtener_ultimo_registro():
    url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la respuesta no es exitosa
        datos = response.json()
        if datos:
            return datos[-1]  # Retorna el último registro
        else:
            return None
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def mostrar_registro():
    registro = obtener_ultimo_registro()

    if registro and 'error' not in registro:
        resultado = (f"Id: {registro['id']}\n"
                     f"Nombre: {registro['nombre']}\n"
                     f"Apellido: {registro['apellido']}\n"
                     f"Ciudad: {registro['ciudad']}\n"
                     f"Calle: {registro['calle']}")
    else:
        resultado = "Error al obtener el registro o no hay registros disponibles."

    etiqueta_resultado.config(text=resultado)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Último Registro Estudiante")

# Crear un botón para obtener el último registro
boton = tk.Button(ventana, text="Mostrar Último Registro", command=mostrar_registro)
boton.pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", justify=tk.LEFT)
etiqueta_resultado.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
