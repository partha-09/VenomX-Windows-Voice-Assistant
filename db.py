import csv
import sqlite3

con = sqlite3.connect("venomX.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS siddugodi(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

