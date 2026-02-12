import os
import random

def load_random_images(folder):
    """
    Carga todas las imágenes de la carpeta especificada y las devuelve mezcladas.
    """
    files = [f for f in os.listdir(folder)
             if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    random.shuffle(files)
    return files


