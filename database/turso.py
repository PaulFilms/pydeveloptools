'''
¡¡ UNDER TEST!!

Functions for Using Databases with TURSO DB

More info:
- https://turso.tech
- https://docs.turso.tech/quickstart

pip install libsql-experimental
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

TASK:
- ...

WARNINGS:
- RUST: Its necesary to install rust <https://www.rust-lang.org/tools/install>
    
'''
__update__ = '2024.02.11'
__author__ = 'PABLO GONZALEZ PILA <pablopila.spain@gmail.com>'


''' SYSTEM LIBRARIES '''
import os
from dotenv import load_dotenv
import libsql_experimental as libsql

load_dotenv()

''' CUSTOM LIBRARIES '''

''' 
FUNCTIONS
----------------------------------------------------------------------------------
'''

## URL & TOKEN
load_dotenv(dotenv_path=os.path.join(os.getcwd(), "database", "turso.env"))
url = os.getenv("LIBSQL_URL")
auth_token = os.getenv("LIBSQL_AUTH_TOKEN")

## CONNECTION
conn = libsql.connect(database=url, auth_token=auth_token)
cur = conn.cursor()

## SQL
# cur.execute("INSERT INTO users VALUES (2, 'alice@example.org')")
print(conn.execute("select * from users").fetchall())

## FIN
print("FIN")