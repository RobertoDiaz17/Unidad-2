import tkinter as tk

def iniciar_sesion():
    usuario = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if usuario == "admin" and contrasena == "admin":
        resultado.config(text="Inicio de sesión exitoso")
    else:
        resultado.config(text="Nombre de usuario o contraseña incorrectos")

ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.configure(padx=100,bg="black")

# Crear campos de entrada para el nombre de usuario y la contraseña
nombre_usuario = tk.Entry(ventana,)
nombre_usuario.pack(pady=10)
contrasena_usuario = tk.Entry(ventana, show="*")
contrasena_usuario.pack()

# Crear botones para iniciar sesión y salir
iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion, bg=("pink")) 
iniciar_sesion.pack(padx=25, pady=25)
salir = tk.Button(ventana, text="Salir", command=ventana.quit)
salir.pack()

# Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
resultado = tk.Label(ventana, text="",bg="black")
resultado.pack(pady=25)

ventana.mainloop()