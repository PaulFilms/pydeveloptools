'''
Functions for using collections in json format

DEBUG:
    - Son funciones muy sencillas hay que intentar usar las funciones nativas
'''
__update__ = '2024.02.20'
__author__ = 'PABLO GONZALEZ PILA <pablopila.spain@gmail.com>'


''' SYSTEM LIBRARIES '''
import json

''' CUSTOM LIBRARIES '''


''' MAIN
------------------------------------------ '''

def json_load(filePath: str) -> dict:
    '''
    '''
    file = f"{filePath}.json"
    dictionary = {}
    with open(file, "r") as read_file:
        dictionary = json.load(read_file)
    return dictionary

def json_save(dictionary: dict, filePath: str) -> None:
    '''
    '''
    file = f"{filePath}.json"
    with open(file, 'w') as f:
        json.dump(dictionary, f)

def dict_to_json(pyDict: dict) -> str:
    '''
    La función "loads" decodifica una información JSON a Diccionario de Python
    '''
    d: str = json.dumps(pyDict)
    return d

def json_to_dict(JSON: str) -> dict:
    '''
    INCOMPLETE:
        No funciona
    '''
    DICT: dict = json.load(JSON)
    return DICT

def json_to_datframe():
    '''
    INCOMPLETE
    Sin hacer
    '''
    print('json_to_datframe')