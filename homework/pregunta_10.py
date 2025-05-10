"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
import os


def pregunta_10():
    """
    Construya una tabla que contenga `c1` como índice (_c1) y una lista
    separada por ':' con los valores ordenados de la columna `c2` para
    cada letra en `tbl0.tsv`.
    """
    ruta = os.path.join(os.path.dirname(__file__),
                        "..", "files", "input", "tbl0.tsv")
    df = pd.read_csv(ruta, sep="\t")

    # agrupar, ordenar y concatenar
    serie = (
        df.groupby("c1")["c2"]
        .apply(lambda x: ":".join(map(str, sorted(x))))
    )

    # convertir a DataFrame y ajustar nombre del índice
    resultado = serie.to_frame()
    resultado.index.name = "_c1"

    return resultado
