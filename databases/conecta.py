import sqlite3

def conecta():
    return sqlite3.connect("lanchonete.db")

