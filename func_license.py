'''
# pyLICENSER

TASK:
    - Eliminar el formato f"@{}@" y sumar TOKEN
    - Hacer GET_LIMITS

WARNINGS:
    pydantic.BaseModel genera problemas con mypyc, se utiliza dataclass

mypyc:
    mypyc func_license.py
    Al distribuir a otras maquinas no funciona el archivo .pyd
'''

__version__ = '2024.01.14'
__author__ = 'PABLO GONZALEZ PILA <pablogonzalezpila@gmail.com>'


''' SYSTEM LIBRARIES '''
import os
from glob import glob
from datetime import datetime, timedelta
from typing import List # Tuple, Union
import hashlib 
# import bcrypt
# from enum import Enum
from dataclasses import dataclass, asdict

''' EXTERNAL LIBRARIES '''
# from pydantic import BaseModel # type: ignore

''' CUSTOM MAIN LIBRARIES '''
import pydeveloptools.func_system as SYS # type: ignore


''' FUNCTIONS
-------------------------------------------------------- '''

@dataclass
class LICENSE:
    USER_NAME: str = ""
    APP_NAME: str = ""
    MACHINE: str = ""
    TIME_MOD: str = ""
    TIME_LIMIT: str = ""

def ENCODE_STR(STR: str) -> str:
    '''
    Encode selected STR
    '''
    return hashlib.sha256(str(STR).encode('utf-8')).hexdigest()
    # hashed = bcrypt.hashpw(str(STR).encode('utf-8'), bcrypt.gensalt())
    # return hashed.decode('utf-8')

def CREATE(path: str, token: str, user_name: str, app_name: str, time_limit: datetime) -> None:
    '''
    Create an encrypted .lic file

    Args:
        path (str): _
        token (str): _
        user_name (str): _
        app_name (str): _
        time_limit (datetime): _

    Returns:
        None
    '''
    ## USER NAME
    USER_NAME = f"@{user_name}@"
    USER_NAME = ENCODE_STR(USER_NAME)

    ## APP NAME
    APP_NAME = f"@{app_name}@"
    APP_NAME = ENCODE_STR(APP_NAME)

    ## MACHINE NAME
    MACHINE = f"@{SYS.OS_GET_LOGIN()}@{SYS.OS_GET_MACHINE()}"
    MACHINE = ENCODE_STR(MACHINE)

    ## TIME MOD
    TIME_MOD = datetime.now().strftime(SYS.DATE_STR_FORMATS.DATE_NOW.value)
    TIME_MOD = ENCODE_STR(TIME_MOD)

    ## TIME LIMIT
    TIME_LIMIT = time_limit.strftime(SYS.DATE_STR_FORMATS.YYYY_MM_DD.value)
    TIME_LIMIT = ENCODE_STR(TIME_LIMIT)

    ## LICENSE
    license = LICENSE(
        USER_NAME=USER_NAME, 
        APP_NAME=APP_NAME, 
        MACHINE=MACHINE, 
        TIME_MOD=TIME_MOD, 
        TIME_LIMIT=TIME_LIMIT
    )
    # DICT = license.model_dump()
    DICT = asdict(license)
    
    DICT_LST: List[str] = list(DICT.values())
    TEXTO: str = ENCODE_STR(token).join(DICT_LST)
    TOKEN_NUMBER = int(sum([ord(l) for l in token]))
    TEXTO = TEXTO * TOKEN_NUMBER

    file_name: str = f"{user_name}.lic"
    path_file: str = os.path.join(path, file_name)
    with open(path_file, 'w') as f:
        f.write(TEXTO)

def GET_LIC(path: str) -> str:
    '''
    Get .lic license file from selected path

    BUG: Es mejor utilizar la funcion GLOB
    '''
    for file in os.listdir(path):
        if SYS.PATH_BASENAME.GET(file, SYS.PATH_BASENAME.EXTENSION) == "lic":
            return os.path.join(path, file)

def CHECK(path_app: str, token: str, app_name: str) -> bool:
    '''
    path (str): _
    token (str): _
    user_name (str): _
    app_name (str): _
    time_limit (datetime): _
    '''
    ## READ TEXT
    try:
        lic_list: list = glob(os.path.join(path_app, "*.lic"))
        if len(lic_list) != 1:
            return None
        path_file: str = lic_list[0]
        with open(path_file, 'r') as f:
            TEXTO = f.read()
    except:
        return False
    
    ## SPLIT TEXT
    TOKEN_NUMBER = int(sum([ord(l) for l in token]))
    TEXTO = "".join([TEXTO[i] for i in range(int(len(TEXTO) / TOKEN_NUMBER))])
    license: List[str] = TEXTO.split(ENCODE_STR(token))

    ## USER NAME
    USER_NAME = os.path.basename(path_file)
    USER_NAME = USER_NAME.split(".")[0]
    USER_NAME = f"@{USER_NAME}@"
    USER_NAME = ENCODE_STR(USER_NAME)
    if license[0] != USER_NAME:
        return False

    ## APP NAME
    APP_NAME = f"@{app_name}@"
    APP_NAME = ENCODE_STR(APP_NAME)
    if license[1] != APP_NAME:
        return False

    ## MACHINE NAME
    MACHINE = f"@{SYS.OS_GET_LOGIN()}@{SYS.OS_GET_MACHINE()}"
    MACHINE = ENCODE_STR(MACHINE)
    if license[2] != MACHINE:
        return False
    
    check: bool = False

    ## CREATE FILE DATE
    # TIME_MOD_FLT = os.path.getmtime(path_file)
    TIME_MOD_FLT = os.path.getctime(path_file)
    TIME_MOD = datetime.fromtimestamp(TIME_MOD_FLT)
    TIME_INIT = TIME_MOD - timedelta(minutes=2)
    for min in range(4):
        TIME_MOD = TIME_INIT + timedelta(minutes=min)
        TIME_STR = TIME_MOD.strftime(SYS.DATE_STR_FORMATS.DATE_NOW.value)
        if license[3] == ENCODE_STR(TIME_STR):
            check = True
    
    if check == False: 
        return False
    
    ## TIME MACHINE
    TIME_MOD_FLT = os.path.getctime(path_file)
    TIME_MOD = datetime.fromtimestamp(TIME_MOD_FLT)
    if datetime.now() < TIME_MOD:
        return False
    
    check = False
    
    ## TIME LIMIT
    TIME_NOW = datetime.now()
    for day in range(365*10):
        TIME_MOD = TIME_NOW + timedelta(days=day)
        TIME_STR = TIME_MOD.strftime(SYS.DATE_STR_FORMATS.YYYY_MM_DD.value)
        if license[4] == ENCODE_STR(TIME_STR):
            check = True

    if check == False: 
        return False
    else:
        return True

def GET_LIMITS() -> dict:
    '''
    Get the limits of selected license
    INCOMPLETE
    '''
    return dict


''' TEST
-------------------------------------------------------- '''

# class LICENSE(BaseModel):
#     USER_NAME: str = ""
#     APP_NAME: str = ""
#     MACHINE: str = ""
#     TIME_MOD: str = ""
#     TIME_LIMIT: str = ""