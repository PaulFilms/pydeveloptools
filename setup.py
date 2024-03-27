'''
'''

__update__ = '2023.03.27b2'
__author__ = 'PABLO PILA'

from setuptools import setup, find_packages, Extension

setup(
    name = "pydeveloptools",
    version = __update__,
    url = "https://github.com/PaulFilms/pydeveloptools",
    author = __author__,
    author_email = "pablogonzalezpila@gmail.com",
    # description="",
    long_description = "README.md",
    # license = "www.unlicense.org",
    packages = find_packages(where='src'), # con find_pachages no conseguir hacerlo funcionar
    # packages=["pydeveloptools"],
    package_dir={'': 'src'},
    include_package_data=True, # muy importante para que se incluyan archivos sin extension .py
    package_data={'pydeveloptools': ['database/*.py', 'forms/*']}, 
    # test_suite='tests',
    classifiers = [
        'Programming Language :: Python :: 3.12',
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        # "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
)

''' CONFIG DE CPYTHON

# Build Script for Cython Files

# ATTENTION:
#     This code is incomplete, all functions have to be rewritten in.pyx files

# cmd: 
#     python setup.py build_ext --inplace

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
    # ext_modules=cythonize(ext_modules),
)

'''
