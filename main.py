import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculadora de Vuelo Fotogramétrico")
root.geometry("600x620")

campos = [
    ("H", "Altura de vuelo [m]"),
    ("Sw", "Ancho sensor [mm]"),
    ("Sh", "Alto sensor [mm]"),
    ("f", "Distancia focal [mm]"),
    ("Iw", "Ancho imagen [px]"),
    ("Ih", "Alto imagen [px]"),
    ("OL", "Superposición longitudinal [%]"),
    ("SL", "Superposición lateral [%]"),
    ("Aw", "Ancho del área [m]"),
    ("Al", "Largo del área [m]"),
    ("V", "Velocidad del dron [m/s]")
]

inputs = {}

def crear_formulario():
    for idx, (clave, etiqueta) in enumerate(campos):
        lbl = ttk.Label(root, text=etiqueta)
        lbl.grid(row=idx, column=0, padx=8, pady=4, sticky="e")
        entrada = ttk.Entry(root, width=25)
        entrada.grid(row=idx, column=1, padx=8, pady=4)
        inputs[clave] = entrada

def abrir_resultados(texto):
    nueva = tk.Toplevel(root)
    nueva.title("Resultado del Cálculo")
    nueva.geometry("520x280")
    texto_widget = tk.Text(nueva, wrap="word")
    texto_widget.insert("1.0", texto)
    texto_widget.config(state="disabled")
    texto_widget.pack(expand=True, fill="both")

def ejecutar_calculo():
    try:
        datos = {clave: float(inputs[clave].get()) for clave, _ in campos}
        escala = datos["H"] / datos["f"]
        gsd = (datos["H"] * datos["Sw"]) / (datos["f"] * datos["Iw"])
        ancho_img = (gsd * datos["Iw"]) / 100
        alto_img = (gsd * datos["Ih"]) / 100
        dist_entre_fotos = alto_img * (1 - datos["OL"] / 100)
        dist_entre_lineas = ancho_img * (1 - datos["SL"] / 100)
        fotos_por_linea = int(datos["Al"] / dist_entre_fotos) + 1
        lineas = int(datos["Aw"] / dist_entre_lineas) + 1
        duracion = (datos["Al"] * lineas) / datos["V"]

        resultado = f"""
ESCALA APROXIMADA: 1:{round(escala, 2)}
GSD: {round(gsd, 2)} cm/pixel
Cobertura de Imagen: {round(ancho_img, 2)} m × {round(alto_img, 2)} m
Espaciado entre fotos: {round(dist_entre_fotos, 2)} m
Espaciado entre líneas: {round(dist_entre_lineas, 2)} m
Fotos por línea: {fotos_por_linea}
Número de líneas: {lineas}
Duración estimada del vuelo: {round(duracion, 2)} segundos
"""
        abrir_resultados(resultado)

    except ValueError:
        abrir_resultados("ERROR: Todos los campos deben contener números válidos.")

crear_formulario()

btn_calcular = ttk.Button(root, text="Ejecutar Cálculo", command=ejecutar_calculo)
btn_calcular.grid(row=len(campos), column=0, columnspan=2, pady=20)

root.mainloop()
