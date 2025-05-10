"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
import os


def pregunta_09():
    """
    Agregue el año como una columna al DataFrame que contiene
    el archivo `tbl0.tsv`.
    """
    ruta = os.path.join(os.path.dirname(__file__), "..", "files", "input", "tbl0.tsv")
    df = pd.read_csv(ruta, sep="\t")

    # Extraer los cuatro primeros caracteres de la fecha (YYYY)
    df["year"] = df["c3"].str[:4]

    return df


