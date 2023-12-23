'''
Build Script for Cython Files


ATTENTION:
    This code is incomplete, all functions have to be rewritten in.pyx files


cmd: 
    python setip.py build_ext --inplace
'''

__update__ = '2023.12.02'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'

from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "pydeveloptools",
        sources=[
            # "func_database.pyx"
            ],
        # Aquí puedes añadir más opciones como librerías externas, directorios, etc.
    )
]

setup(
    name='pydeveloptools',
    ext_modules=cythonize(ext_modules),
)

