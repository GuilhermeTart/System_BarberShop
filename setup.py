from cx_Freeze import setup, Executable
import sys
import os

# Definindo o parâmetro Include_msrv
include_msrv = True  # Mude para False se não quiser incluir o redistribuível

# Lista de bibliotecas e arquivos adicionais usados no seu script
build_exe_options = {
    "packages": ["flet", "csv", "re", "datetime", "tinydb", "openpyxl", "threading"],
    "include_files": ["luxa.org-opacity-changed-FULLHD.jpg", "Barber.ico"],  # Inclua arquivos adicionais necessários
}

# Condicionalmente incluindo o redistribuível MSVC se Include_msrv for True ADICIONA UM OUTRO EXE NO COMPILADO
if include_msrv:
    # Caminho para o redistribuível VC_redist.x86.exe
    msvc_path = "C:/Users/pc/Music/Barber/venv/VC_redist.x64.exe"
    
    # Verifica se o arquivo existe
    if os.path.exists(msvc_path):
        build_exe_options["include_files"].append((msvc_path, "VC_redist.x86.exe"))
    else:
        print("Aviso: VC_redist.x64.exe não encontrado. Verifique o caminho.")

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
