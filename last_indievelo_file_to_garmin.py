#Created by Paco Martínez with Gemini help
#Script to read the last file created by indieVelo and pass to garmin.py script and upload to Garmin Connect 
#Change "soy_tonto_directorio" to your directory where are the .fit indieVelo files.

import os
from datetime import datetime
import time
import subprocess

#Change "soy_tonto_directorio" to your directory where .fit indieVelo files are.
#The format should be with / not \, example C:/tengo_Iphone/soy_tonto/indieVelo/FITFiles
directorio = "soy_tonto_directorio"

def obtener_ultimo_archivo(directorio):
    """
    Obtiene el último archivo creado en un directorio dado.

    Args:
        directorio (str): Ruta al directorio a buscar.

    Returns:
        str: Ruta completa del último archivo creado, o None si no se encuentra ninguno.
    """

    lista_archivos = os.listdir(directorio)
    lista_archivos = [os.path.join(directorio, archivo) for archivo in lista_archivos]

    archivos_con_fecha = []
    for archivo in lista_archivos:
        try:
            fecha_creacion = datetime.fromtimestamp(os.path.getmtime(archivo))
            archivos_con_fecha.append((fecha_creacion, archivo))
        except OSError:
            # Ignorar archivos que no se pueden acceder
            pass

    if archivos_con_fecha:
        archivos_con_fecha.sort(reverse=True)
        return archivos_con_fecha[0][1]
    else:
        return None

ultimo_archivo = obtener_ultimo_archivo(directorio)

if ultimo_archivo:
    print("El último archivo creado es:", ultimo_archivo)
else:
    print("No se encontraron archivos en el directorio.")

print("Vamos a pasarselo al script garmin.py para que lo trate y lo suba a Garmin Connect")

#time.sleep(5)

subprocess.call(["python", "garmin.py", "-u", ultimo_archivo, "-v"])
