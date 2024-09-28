import csv

# Datos de ejemplo (sin tildes)
personas = [
    ("Cristian Morales", "12/01/1990"),
    ("Camila Munoz", "24/07/1985"),
    ("Felipe Gonzalez", "15/03/1978"),
    ("Isidora Lopez", "30/11/2001"),
    ("Diego Ruiz", "10/05/1992"),
    ("Valentina Castro", "28/09/1988"),
    ("Joaquin Mora", "17/04/1975"),
    ("Antonia Ortiz", "22/12/1999"),
    ("Mateo Fernandez", "08/08/1980"),
    ("Sofia Ramirez", "19/02/1995"),
    ("Tomas Herrera", "02/06/2000"),
    ("Marta Silva", "14/10/1973"),
    ("Andres Paredes", "11/11/1982"),
    ("Natalia Rios", "26/07/1976"),
    ("Esteban Navarro", "05/09/1987")
]

# Generar el archivo CSV
with open('entrada.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    # Escribir los datos
    writer.writerows(personas)

print("Archivo CSV de entrada generado.")