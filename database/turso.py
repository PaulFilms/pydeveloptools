'''
Functions for Using Databases with TURSO DB
¡¡ UNDER TEST!!

More info:
- https://turso.tech
- https://docs.turso.tech/quickstart

pip install libsql-experimental

WARNINGS:
    - [Using MacOS] Problems with RUST:
        thread '<unnamed>' panicked at /Users/runner/.cargo/git/checkouts/libsql-311658d335deb3b1/b015002/libsql/src/hrana/hyper.rs:88:9:
        there is no reactor running, must be called from the context of a Tokio 1.x runtime
        note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
        pyo3_runtime.PanicException: there is no reactor running, must be called from the context of a Tokio 1.x runtime
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