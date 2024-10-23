from datetime import datetime

def obtener_saludo():
    hora_actual = datetime.now().hour
    if 6 <= hora_actual < 12:
        return "Buenos días"
    elif 12 <= hora_actual < 18:
        return "Buenas tardes"
    else:
        return "Buenas noches"

def mostrar_saludo(nombre):
    saludo = obtener_saludo()
    hora_actual = datetime.now().strftime("%H:%M:%S")
    print(f"{saludo}, {nombre}. La hora actual es {hora_actual}.")

# Ejemplo de uso
nombre = "Carlos"
mostrar_saludo(nombre)