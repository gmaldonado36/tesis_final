import os
import random
from config import FASE1_FOLDER, TOTAL_IMAGES

def load_random_images():
    files = [f for f in os.listdir(FASE1_FOLDER)
             if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    random.shuffle(files)
    return files[:TOTAL_IMAGES]

