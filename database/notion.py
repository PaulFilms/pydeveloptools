'''
Functions for Using Notion API

BUG: INCOMPLETE

More info: 
[pypi.org](https://pypi.org/project/notion-client/) / pip install notion-client
[github.com](https://github.com/ramnes/notion-sdk-py)

'''

__update__ = '2024.01.12'
__author__ = 'PABLO GONZALEZ PILA <pablopila.spain@gmail.com>'

''' SYSTEM LIBRARIES '''
import os
from notion_client import Client


''' MAIN
------------------------------------------ '''

filePath = "database/notion.txt"
with open(filePath, 'r') as f:
    txt = f.readlines()

NOTION_TOKEN: str = txt[0].replace(chr(10), str())
DATABASE_ID: str = txt[1]

print(NOTION_TOKEN)
print(DATABASE_ID)
print()

# Establecer la variable de entorno
os.environ["NOTION_TOKEN"] = NOTION_TOKEN


notion = Client(auth=os.environ["NOTION_TOKEN"])

v = notion.databases.query(database_id=DATABASE_ID)
for row in v["results"]:
    for field in row:
        print(field)
    print()