from cx_Freeze import setup, Executable
import sys

# Inclua todas as bibliotecas que você está usando no seu script
build_exe_options = {
    "packages": ["flet", "csv", "re", "datetime", "tinydb", "openpyxl"],
    "include_files": ["luxa.org-opacity-changed-FULLHD.jpg", "Barber.ico"],  # Inclua arquivos adicionais necessários
}

# Defina o alvo do executável
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use "Win32GUI" para aplicativos GUI no Windows

setup(
    name="BarbeariaApp",
    version="1.0",
    description="Aplicativo de gestão de barbearia",
    options={"build_exe": build_exe_options},
    executables=[Executable("BarberShop.py", base=base, icon="Barber.ico")]
)