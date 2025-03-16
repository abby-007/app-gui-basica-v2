import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada.get().strip()  # Obtener el texto del campo de entrada
    if dato:  # Verificar que el campo no esté vacío
        lista.insert(tk.END, dato)  # Agregar el dato a la lista
        entrada.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa un dato.")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)  # Borrar todos los elementos de la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")  # Título de la ventana
ventana.geometry("400x300")  # Tamaño de la ventana

# Etiqueta de instrucción
etiqueta = tk.Label(ventana, text="Ingresa un dato y presiona 'Agregar':")
etiqueta.pack(pady=10)

# Campo de texto para entrada de datos
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()