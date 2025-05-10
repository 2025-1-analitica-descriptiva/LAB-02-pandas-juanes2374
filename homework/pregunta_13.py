"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd
import os

def pregunta_13():
    ruta_tbl0 = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'tbl0.tsv')
    ruta_tbl2 = os.path.join(os.path.dirname(__file__), '..', 'files', 'input', 'tbl2.tsv')
    
    tbl0 = pd.read_csv(ruta_tbl0, sep='\t')
    tbl2 = pd.read_csv(ruta_tbl2, sep='\t')

    df_merged = pd.merge(tbl0[['c0', 'c1']], tbl2[['c0', 'c5b']], on='c0')
    resultado = df_merged.groupby("c1")["c5b"].sum()
    
    return resultado
