import subprocess
import sys
import time

# Bibliothèques à installer (hors standard)
required_libs = [
    "customtkinter"
]

def install_libs(libs):
    for lib in libs:
        try:
            __import__(lib)
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write("\r" + " " * 40 + "\r")  # Efface la ligne

        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

#Installation
install_libs(required_libs)
from Ukkoinfo import *