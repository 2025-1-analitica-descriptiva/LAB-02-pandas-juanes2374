"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
import os

def pregunta_01():
    ruta = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'tbl0.tsv')
    df = pd.read_csv(ruta, sep='\t')
    return df.shape[0]

