import tkinter as tk
from services.mi_sql import conectar

def cargar_login(ventana):
    login_panel = tk.Frame(
        ventana,
        bg="Violet",
        padx=0,
        pady=0,
        width=1000,
        height=600
    )

    # Título
    #título = tk.Label(login_panel, text="Filtrar datos", font=("Arial", 16))
    #título.pack(pady=20)

    # Entrada de nombre
    tk.Label(login_panel, text="Escriba el nombre a buscar:").pack()
    entrada_nombre = tk.Entry(login_panel, width=40)
    entrada_nombre.pack(pady=10)

    # Función del botón
    def buscar_datos():
        nombre = entrada_nombre.get()
        consulta = f"SELECT correo, contraseña, apellido FROM usuarios WHERE nombre = '{nombre}'"
        resultado = conectar(consulta)

        if resultado:
            print("Datos encontrados:")
            for fila in resultado:
                print(f"Correo: {fila[0]}")
                print(f"Clave: {fila[1]}")
                print(f"Apellido: {fila[2]}")
        else:
            print("No se encontró ese nombre en la base de datos.")

    # Botón para buscar
    boton_buscar = tk.Button(login_panel, text="Buscar", command=buscar_datos)
    boton_buscar.pack(pady=10)

    login_panel.pack()
    print("Panel de filtrado cargado")



    