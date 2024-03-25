import os
import subprocess

print("PySide Forms Update ----------")
print(os.getcwd())

# Set the PYSIDE6DEPLOY_QT_LIB environment variable
# os.environ["PYSIDE6DEPLOY_QT_LIB"] = "PySide6"
# PYSIDE6DEPLOY_QT_LIB="PySide6"
# print(os.environ["PYSIDE6DEPLOY_QT_LIB"])

# Run the pyuic6 tool
SUBPROCESS_LIST = [
    # ["pyuic6", "-x", "forms/PYQT_QLIST.ui", "-o", "forms/PYSIDE_QLIST.py"] # La opcion -x es para crear el eejecutable
    ["pyside6-uic", "forms/PYQT_QLIST.ui", "-o", "forms/PYSIDE_QLIST.py"],
    ["pyside6-uic", "forms/PYQT_QLIST_FORM.ui", "-o", "forms/PYSIDE_QLIST_FORM.py"],
]
for procss in SUBPROCESS_LIST:
    subprocess.run(procss)

print("FIN ----------")
print()