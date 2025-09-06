import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import sys
import os

def install_pyinstaller():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    except subprocess.CalledProcessError:
        messagebox.showerror("Erreur", "L'installation de PyInstaller a échoué.")

def build_executable(script_path, icon_path):
    try:
        subprocess.check_call([
            sys.executable,
            "-m", "pyinstaller",
            "--onefile",
            f"--icon={icon_path}",
            script_path
        ])
        messagebox.showinfo("Succès", "✅ Compilation terminée ! Ton .exe est dans le dossier 'dist'.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Erreur", "La compilation a échoué.")

def select_script():
    path = filedialog.askopenfilename(filetypes=[("Fichiers Python", "*.py")])
    if path:
        script_entry.delete(0, tk.END)
        script_entry.insert(0, path)

def select_icon():
    path = filedialog.askopenfilename(filetypes=[("Icônes", "*.ico")])
    if path:
        icon_entry.delete(0, tk.END)
        icon_entry.insert(0, path)

def compile():
    script = script_entry.get()
    icon = icon_entry.get()

    if not os.path.exists(script) or not script.endswith(".py"):
        messagebox.showerror("Erreur", "Sélectionne un fichier Python valide.")
        return
    if not os.path.exists(icon) or not icon.endswith(".ico"):
        messagebox.showerror("Erreur", "Sélectionne une icône .ico valide.")
        return

    install_pyinstaller()
    build_executable(script, icon)

# Interface Tkinter
root = tk.Tk()
root.title("Créateur d'exécutable Ukkoinfo 🐍")

tk.Label(root, text="Sélectionne ton script Python :").pack(pady=5)
script_entry = tk.Entry(root, width=60)
script_entry.pack()
tk.Button(root, text="📂 Parcourir", command=select_script).pack(pady=5)

tk.Label(root, text="Sélectionne ton icône (.ico) :").pack(pady=5)
icon_entry = tk.Entry(root, width=60)
icon_entry.pack()
tk.Button(root, text="🖼️ Parcourir", command=select_icon).pack(pady=5)

tk.Button(root, text="🚀 Compiler en .exe", command=compile, bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

root.mainloop().