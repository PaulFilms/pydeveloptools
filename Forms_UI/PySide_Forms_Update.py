import os
import subprocess

print("PySide Forms Update ----------")
print(os.getcwd())

## Set the PYSIDE6DEPLOY_QT_LIB environment variable
# os.environ["PYSIDE6DEPLOY_QT_LIB"] = "PySide6"
# PYSIDE6DEPLOY_QT_LIB="PySide6"
# print(os.environ["PYSIDE6DEPLOY_QT_LIB"])

## Run the pyuic6 tool
SUBPROCESS_LIST = [
    # ["pyuic6", "-x", "forms/PYQT_QLIST.ui", "-o", "forms/PYSIDE_QLIST.py"] # La opcion -x es para crear el eejecutable
    ["pyside6-uic", "Forms_UI/QACQUISITIONS.ui", "-o", "pydeveloptools/forms/PYSIDE_QACQUISITIONS.py"],
    ["pyside6-uic", "Forms_UI/QCALENDAR.ui", "-o", "pydeveloptools/forms/PYSIDE_QCALENDAR.py"],
    ["pyside6-uic", "Forms_UI/QLICENSE.ui", "-o", "pydeveloptools/forms/PYSIDE_QLICENSE.py"],
    ["pyside6-uic", "Forms_UI/QLIST_FORM.ui", "-o", "pydeveloptools/forms/PYSIDE_QLIST_FORM.py"],
    ["pyside6-uic", "Forms_UI/QLIST.ui", "-o", "pydeveloptools/forms/PYSIDE_QLIST.py"],
    ["pyside6-uic", "Forms_UI/QMARKDOWN.ui", "-o", "pydeveloptools/forms/PYSIDE_QMARKDOWN.py"],
    ["pyside6-uic", "Forms_UI/QTABLE_DICT.ui", "-o", "pydeveloptools/forms/PYSIDE_QTABLE_DICT.py"],
    ["pyside6-uic", "Forms_UI/QTABLE_FORM.ui", "-o", "pydeveloptools/forms/PYSIDE_QTABLE_FORM.py"],
]
for procss in SUBPROCESS_LIST:
    subprocess.run(procss)

print("FIN ----------")
print()