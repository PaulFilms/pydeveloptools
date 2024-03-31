'''
UNDER TEST
'''

from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "func_license",
        sources=["func_license.pyx"],
        # Aquí puedes añadir más opciones como librerías externas, directorios, etc.
    )
]

setup(
    name='func_license',
    ext_modules=cythonize(ext_modules),
)
