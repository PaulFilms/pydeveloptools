'''
Build Script for Cython Files


ATTENTION:
    This code is incomplete, all functions have to be rewritten in.pyx files


cmd: 
    python setip.py build_ext --inplace
'''

__update__ = '2023.03.24'
__author__ = 'PABLO PILA'
__author_email__ = "pablogonzalezpila@gmail.com"

from setuptools import setup, find_packages, Extension
# from Cython.Build import cythonize

setup(
    name = "pydeveloptools",
    # packages = find_packages(), # con find_pachages no conseguir hacerlo funcionar
    packages=["pydeveloptools"],
    include_package_data=True, # muy importante para que se incluyan archivos sin extension .py
    package_data={'pydeveloptools': ['database/*.py', 'forms/*']}, 
    version = __update__,
    author = __author__,
    author_email = __author_email__,
    url = "https://github.com/PaulFilms/pydeveloptools.git",
    long_description = "README.md",
    # license = "www.unlicense.org",
    classifiers = [
        'Programming Language :: Python :: 3',
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        ],
)


''' CONFIG DE CPYTHON
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
    # ext_modules=cythonize(ext_modules),
)

'''