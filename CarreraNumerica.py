import tkinter as tk
import random

# Función para iniciar el juego después de seleccionar la cantidad de jugadores y el nivel del tablero
def iniciar_juego():
    global num_jugadores, tamaño_tablero
    
    num_jugadores = int(entry_jugadores.get())  # Obtener el número de jugadores
    
    # Obtener el nivel del tablero seleccionado
    nivel = nivel_tablero.get()
    if nivel == 1:
        tamaño_tablero = 20
    elif nivel == 2:
        tamaño_tablero = 30
    elif nivel == 3:
        tamaño_tablero = 50
    elif nivel == 4:
        tamaño_tablero = 100
    
    # Cerrar la ventana de selección
    ventana_seleccion.destroy()
    
    # Iniciar la ventana del juego de dados
    iniciar_ventana_juego()

# Función para lanzar los dados
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    resultado.set(f"{dado1} y {dado2}")
    
    # Actualizar posición del jugador
    movimiento = dado1 + dado2
    posiciones[jugador_actual.get() - 1] += movimiento
    label_posiciones.config(text=f"Posición Jugador {jugador_actual.get()}: {posiciones[jugador_actual.get() - 1]}")
    
    # Verificar si el jugador ha llegado a la meta
    if posiciones[jugador_actual.get() - 1] >= tamaño_tablero:
        resultado.set(f"¡Jugador {jugador_actual.get()} ha ganado!")
        boton_roll.config(state=tk.DISABLED)  # Deshabilitar el botón "Roll" si alguien gana
        return

    # Cambiar al siguiente jugador
    jugador_actual.set((jugador_actual.get() % num_jugadores) + 1)
    label_jugador.config(text=f"Turno Jugador {jugador_actual.get()}")

# Función para iniciar la ventana de juego
def iniciar_ventana_juego():
    global ventana_juego, resultado, jugador_actual, posiciones, label_jugador, label_posiciones, boton_roll
    
    ventana_juego = tk.Tk()
    ventana_juego.title("Juego de Dados")

    posiciones = [0] * num_jugadores  # Inicializar las posiciones de los jugadores
    jugador_actual = tk.IntVar(value=1)  # Jugador que inicia el turno
    resultado = tk.StringVar()  # Resultado de los dados

    # Etiqueta para mostrar el turno del jugador
    label_jugador = tk.Label(ventana_juego, text=f"Turno Jugador {jugador_actual.get()}", font=("Arial", 16))
    label_jugador.pack(pady=10)

    # Etiqueta para mostrar el resultado de los dados (más grande)
    label_resultado = tk.Label(ventana_juego, textvariable=resultado, font=("Arial", 72), bg="white", width=10, height=2)
    label_resultado.pack(pady=20)

    # Etiqueta para mostrar la posición del jugador actual
    label_posiciones = tk.Label(ventana_juego, text=f"Posición Jugador {jugador_actual.get()}: 0", font=("Arial", 16))
    label_posiciones.pack(pady=10)

    # Botón para lanzar los dados
    boton_roll = tk.Button(ventana_juego, text="Roll", command=lanzar_dados, font=("Arial", 20))
    boton_roll.pack(pady=20)

    ventana_juego.mainloop()

# Ventana de selección de jugadores y nivel
ventana_seleccion = tk.Tk()
ventana_seleccion.title("Configuración del Juego")

# Etiqueta de instrucción para seleccionar la cantidad de jugadores
label_instruccion_jugadores = tk.Label(ventana_seleccion, text="Seleccione la cantidad de jugadores (1 a 4)", font=("Arial", 14))
label_instruccion_jugadores.pack(pady=10)

# Entrada para seleccionar la cantidad de jugadores
entry_jugadores = tk.Entry(ventana_seleccion, font=("Arial", 14), justify='center')
entry_jugadores.pack(pady=10)

# Etiqueta para seleccionar el nivel de dificultad
label_instruccion_nivel = tk.Label(ventana_seleccion, text="Seleccione el nivel del tablero:", font=("Arial", 14))
label_instruccion_nivel.pack(pady=10)

# Variable para almacenar el nivel del tablero
nivel_tablero = tk.IntVar()

# Radio buttons para seleccionar el nivel del tablero
tk.Radiobutton(ventana_seleccion, text="1. Nivel básico (Tablero de 20 posiciones)", variable=nivel_tablero, value=1, font=("Arial", 12)).pack(pady=5)
tk.Radiobutton(ventana_seleccion, text="2. Nivel intermedio (Tablero de 30 posiciones)", variable=nivel_tablero, value=2, font=("Arial", 12)).pack(pady=5)
tk.Radiobutton(ventana_seleccion, text="3. Nivel avanzado (Tablero de 50 posiciones)", variable=nivel_tablero, value=3, font=("Arial", 12)).pack(pady=5)
tk.Radiobutton(ventana_seleccion, text="4. Nivel experto (Tablero de 100 posiciones)", variable=nivel_tablero, value=4, font=("Arial", 12)).pack(pady=5)

# Botón para iniciar el juego
boton_iniciar = tk.Button(ventana_seleccion, text="Iniciar Juego", command=iniciar_juego, font=("Arial", 14))
boton_iniciar.pack(pady=20)

ventana_seleccion.mainloop()
