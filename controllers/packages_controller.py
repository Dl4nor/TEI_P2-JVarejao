import sys
import subprocess
import utils.utillities as utilU

def install_packages():
    required_packages = [
        "bcrypt",
        "keyboard"
    ]

    for package in required_packages:
        try:
            __import__(package)
        except:
            print(f"Pacote '{package}' não encontrado. Instalando...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        else:
            print(f"Pacote '{package}' já instalado.")

    utilU.wait_print("Todos os pacotes instalados!")