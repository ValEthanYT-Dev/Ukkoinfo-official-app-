import os
import subprocess
import sys

# 📦 Installation automatique des modules nécessaires
def install_packages():
    packages = ["pywin32", "customtkinter", "winshell"]
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ Module installé : {package}")
        except subprocess.CalledProcessError:
            print(f"❌ Échec de l'installation : {package}")

# 📁 Création du raccourci sur le bureau
def create_shortcut():
    import winshell
    from win32com.client import Dispatch

    # 📂 Dossier courant (où se trouve le script)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 📄 Fichiers cibles
    bat_file = os.path.join(current_dir, "Ukkoinfo.bat")
    ico_file = os.path.join(current_dir, "Ukkoinfo_logo.ico")

    # 📍 Chemin du raccourci sur le bureau
    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, "Ukkoinfo.lnk")

    # ✅ Vérifie si le raccourci existe déjà
    if os.path.exists(shortcut_path):
        print("⚠️ Le raccourci existe déjà, aucune action nécessaire.")
        return

    # 🧠 Création du raccourci
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = bat_file
    shortcut.WorkingDirectory = current_dir
    shortcut.IconLocation = f"{ico_file},0"  # Format correct pour l'icône
    shortcut.WindowStyle = 7  # Fenêtre réduite
    shortcut.Description = "Lance Ukkoinfo en mode réduit"
    shortcut.save()

    print(f"📎 Raccourci créé sur le bureau : {shortcut_path}")

# 🚀 Lancement du programme
if __name__ == "__main__":
    print("🔧 Installation des modules...")
    install_packages()

    print("🖱️ Vérification du raccourci...")
    create_shortcut()

    print("🎉 Terminé !")
