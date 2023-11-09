import qrcode
import pandas as pd

# Crear una lista de diccionarios con la información de los estudiantes
estudiantes = [
    {"nombre": "Christopher Soriano", "edad": 20, "carrera": "ICO", "id": 1926638},
    {"nombre": "Kevin Miranda", "edad": 22, "carrera": "ICO", "id": 1926639},
    {"nombre": "antonio Blancas", "edad": 21, "carrera": "ICO", "id": 1926658},
    # Agrega más estudiantes según sea necesario
]

# Crear un DataFrame de pandas con la información de los estudiantes
df = pd.DataFrame(estudiantes)

# Crear una columna adicional para almacenar los códigos QR
df["codigo_qr"] = ""

# Crear códigos QR y guardar la información en el DataFrame
for index, estudiante in df.iterrows():
    data = f"Nombre: {estudiante['nombre']}\nEdad: {estudiante['edad']}\nCarrera: {estudiante['carrera']}\nID: {estudiante['id']}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar el código QR como una imagen
    img.save(f"codigo_qr_estudiante_{estudiante['id']}.png")

    # Almacenar la ruta de la imagen en el DataFrame
    df.at[index, "codigo_qr"] = f"codigo_qr_estudiante_{estudiante['id']}.png"

# Guardar la información en un archivo Excel
df.to_excel("BD_alumnos.xlsx", index=False, engine='openpyxl')
