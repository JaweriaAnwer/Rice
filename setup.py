# setup.py
import sys
import os
from cx_Freeze import setup, Executable

python_install_dir = os.path.dirname(os.path.dirname(os.__file__))
include_files = [
    os.path.join(python_install_dir, "tcl", "tcl8.6"),
    os.path.join(python_install_dir, "tcl", "tk8.6"),
    r"C:/Users/USERC/Desktop/rice/img/icon1.ico"
]

build_exe_options = {
    "packages": ["os", "tkinter"],
    "include_files": include_files
}

exe = Executable(
    script="main.py",
    base=None,         
    icon=r"C:/Users/USERC/Desktop/rice/img/icon1.ico"
)

setup(
    name="National Grain Tech NGT",
    version="1.0",
    description="Rice Grain Analysis Software",
    options={"build_exe": build_exe_options},
    executables=[exe]  # use exe here, not base=None
)