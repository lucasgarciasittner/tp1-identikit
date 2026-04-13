"""
Una empresa de análisis de mercado desea desarrollar un programa en Python
para gestionar información sobre las descargas de aplicaciones móviles en distintas
plataformas.
El sistema debe resolver los siguientes puntos:

1)Generación del archivo CSV. Se deben ingresar datos de diferentes aplicaciones.
Por cada aplicación se registrará:

codigo de la aplicacion (valor entero entre 1000 y 9999).
Plataforma (texto: "ANDROID" o "IOS").
Cantidad de descargas (entero entre 0 y 100000).

La carga finaliza cuando el codigo de la aplicacion sea 999.

Todos los ingresos deben validarse utilizando función/es genérica/s con
manejo de excepciones que garantice que los datos ingresados sean válidos.

El archivo generado debe llamarse apps.csv.

2)Carga y procesamiento de datos

A partir del archivo apps.csv, se solicita cargar los datos a memoria en
un diccionario principal que agrupe por plataforma, la cantidad total de descargas
y por cada app descargada en la plataforma que indique el parcial de total de descargas
para esa app en esa plataforma.

3) Generación del archivo resultante:  A partir del diccionario, generar un nuevo archivo
CSV llamado resumen_descargas.csv, con el siguiente formato:

PLATAFORMA,CANTIDAD TOTAL DE DESCARGAS,PORCENTAJE QUE REPRESENTA
-----------------------------------------------------------------------------
Restricciones técnicas

El programa debe estar dividido en funciones (modularizado).

No usar librerías externas (ni csv).

Manejar errores de entrada con try/except.

Se recomienda utilizar funciones genéricas para validar ingresos numéricos y de texto.

El programa principal (main) debe coordinar todas las etapas."""

def validar_entero(mensaje, min_val=None, max_val=None):
    while True:
        try:
            valor = int(input(mensaje))
            if (min_val is not None and valor < min_val) or (max_val is not None and valor > max_val):
                raise ValueError
            return valor
        except ValueError:
            print(f"Por favor, ingrese un entero válido entre {min_val} y {max_val}.")
        

def validar_texto(mensaje, opciones=None):
    while True:
        valor = input(mensaje).strip().upper()
        if opciones and valor not in opciones:
            print(f"Por favor, ingrese una opción válida: {', '.join(opciones)}.")
        elif not valor:
            print("El valor no puede estar vacío.")
        else:
            return valor
def generar_archivo_csv():
    with open("apps.csv", "w") as archivo:
        while True:
            codigo = validar_entero("Ingrese el código de la aplicación (999 para finalizar): ", 1000, 9999)
            if codigo == 999:
                break
            plataforma = validar_texto("Ingrese la plataforma (ANDROID/IOS): ", ["ANDROID", "IOS"])
            descargas = validar_entero("Ingrese la cantidad de descargas (0-100000): ", 0, 100000)
            archivo.write(f"{codigo},{plataforma},{descargas}\n")
def cargar_datos():
    datos = {}
    with open("apps.csv", "r") as archivo:
        for linea in archivo:
            codigo, plataforma, descargas = linea.strip().split(",")
            descargas = int(descargas)
            if plataforma not in datos:
                datos[plataforma] = {"total_descargas": 0, "apps": {}}
            datos[plataforma]["total_descargas"] += descargas
            datos[plataforma]["apps"][codigo] = descargas
    return datos
def generar_resumen(datos):
    with open("resumen_descargas.csv", "w") as archivo:
        for plataforma, info in datos.items():
            total_descargas = info["total_descargas"]
            for codigo, descargas in info["apps"].items():
                porcentaje = (descargas / total_descargas) * 100 if total_descargas > 0 else 0
                archivo.write(f"{plataforma},{total_descargas},{porcentaje:.2f}\n")
def main():
    generar_archivo_csv()
    datos = cargar_datos()
    generar_resumen(datos)
if __name__ == "__main__":
    main()
