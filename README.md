# Planificador de Vuelo Fotogramétrico

Esta aplicación en Python permite calcular parámetros clave para planificar un vuelo fotogramétrico, incluyendo:

- GSD (Ground Sampling Distance)
- Escala aproximada
- Cobertura de imagen
- Distancia entre fotos
- Número de fotos y líneas de vuelo
- Tiempo estimado del vuelo

## Uso

1. Abre el archivo `main.py` y ejecútalo con Python 3:
    ```bash
    python main.py
    ```

2. Ingresa los parámetros requeridos.

3. Haz clic en "Ejecutar Cálculo".

## Compilación a EXE

Este proyecto fue compilado a `.exe` utilizando [PyInstaller](https://pyinstaller.org/en/stable/):

```bash
pyinstaller --onefile main.py
```

Esto generará:

- `/dist/main.exe`
- `/build/`
- `planificador.spec`

## Requisitos

- Python 3.x
- Tkinter (incluido por defecto en Python)


