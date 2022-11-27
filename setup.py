import sys
from cx_Freeze import setup, Executable
from Dlls import include_files

base = None
if sys.platform == "win32":
    base = "Win32GUI"
if sys.platform == "win64":
    base = "Win64GUI"
    
setup(
    name="Zeros Pogram",
    author="David Pereira (david.pereira@acad.ufsm.br) e Emerson Fouchy (emerson.fouchy@acad.ufsm.br)",
    version="1.0.0",
    description="Prorama de zero de funções",
    options={'build_exe': {
        'includes': ["gi"],
        'excludes': ['wx', 'email', 'pydoc_data', 'curses'],
        'packages': ["gi"],
        'include_files': include_files
    }},
    executables=[
        Executable("program.py",
                   base=base
                   )
    ]
)
