import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

# Calcular la edad
def calcular_edad(fecha_nacimiento):
    fecha_nac = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    hoy = datetime.today()
    return hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))

# Determinar el signo zodiacal
def obtener_signo_zodiacal(fecha_nacimiento):
    fecha_nac = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    dia = fecha_nac.day
    mes = fecha_nac.month
    
    signos = [
        ("Capricornio", (12, 22), (1, 19)),
        ("Acuario", (1, 20), (2, 18)),
        ("Piscis", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Tauro", (4, 20), (5, 20)),
        ("Geminis", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Escorpio", (10, 23), (11, 21)),
        ("Sagitario", (11, 22), (12, 21))
    ]
    
    # Recorrer la lista de signos y comparar las fechas con un ciclo "for"
    for signo, inicio, fin in signos:
        mes_inicio, dia_inicio = inicio
        mes_fin, dia_fin = fin
        
        if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin):
            return signo

    return "Signo no encontrado"

# Determinar la generación con "if"
def obtener_generacion(fecha_nacimiento):
    anio = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").year
    if 1946 <= anio <= 1964:
        return "Baby Boomer"
    elif 1965 <= anio <= 1980:
        return "Generacion X"
    elif 1981 <= anio <= 1996:
        return "Millennial"
    elif anio >= 1997:
        return "Generacion Z"
    else:
        return "Generacion Silenciosa"

# Buscar que paso el dia que nacio la persona en Google con Selenium
def buscar_quePaso(fecha_nacimiento):
    driver = webdriver.Chrome()
    query = f"qué pasó el {fecha_nacimiento}"
    driver.get(f"https://www.google.com/search?q={query}")
    try:
        resultado = driver.find_element(By.CSS_SELECTOR, "div[data-attrid='wa:/description']").text
    except:
        resultado = "No encontrado"
    driver.quit()

    # Limitar la longitud del resultado a 1000 caracteres y eliminar retornos de carro y tabulaciones con "replace"
    if len(resultado) > 1000:
        resultado = resultado[0:999]
        resultado = resultado.replace("\n", " ")
        resultado = resultado.replace("\r", " ")
        resultado = resultado.replace("\t", " ")

    print("=======================================================")

    return resultado

# Leer el archivo CSV de entrada y procesarlo
personas_procesadas = []
with open('entrada.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        nombre = row[0]
        fecha_nacimiento = row[1]
        edad = calcular_edad(fecha_nacimiento)
        signo = obtener_signo_zodiacal(fecha_nacimiento)
        generacion = obtener_generacion(fecha_nacimiento)
        quePaso = buscar_quePaso(fecha_nacimiento)
        personas_procesadas.append([nombre, edad, signo, generacion, quePaso])

# Guardar en archivo CSV de salida
with open('salida.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["Nombre Completo", "Edad", "Signo del Zodiaco", "Generacion", "¿Que paso ese dia?"])
    writer.writerows(personas_procesadas)

print("Archivo CSV de salida generado.")
