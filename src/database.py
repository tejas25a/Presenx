from pathlib import Path 
import sqlite3
import pandas as pd
import time
import calendar as cal

#Presenx dir 
BASE_DIR = Path(__file__).resolve().parents[1]

#Data dir
DATA_DIR = BASE_DIR / "data"

def initDB():
    #ensure the dir exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    db_path = DATA_DIR/"students_details.db"
    #Creates a new database file if it doesn't exist
    db_connect = sqlite3.connect(db_path)

    #Create a db cursor object
    db_cursor = db_connect.cursor()

    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT
        )
                      """)


    return db_connect, db_cursor

#dynamic create table
def createMonthTable(db_cursor, month, year):
    numberDays = cal.monthrange(year, month)[1]
    ls=list(range(1,numberDays+1))
    columns=""
    for i in ls:
        columns+=f"day_{i} INTEGER,"
    columns=columns[:-1] #remove trailing comma
    db_cursor.execute(f"""
  CREATE TABLE IF NOT EXISTS t{month}_{year} (
        id INTEGER PRIMARY KEY,
        {columns}
        )
                      """)

def outputTables(conn):
    #Intial version Output Console
    # uses parameter db_cursor 
    
    #OUTPUT Using Pandas
    # ✅ FIXED
    dataframe = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table'", 
    conn
)
    print(dataframe.to_string(index=False))

def inputStudent(db_cursor, id, name):
    if (id == None):
        print("Error: id cannot be NULL\nIt is a primary key. ")
        return
    if (name == None):
        print("Error: name field is  required\n")
        return

    db_cursor.execute(f"INSERT INTO students values({id}, '{name}')")

def outputStudents(conn):
    #Intial version Output Console
    # uses parameter db_cursor 
    
    #OUTPUT Using Pandas
    dataframe=pd.read_sql_query("select * from students",conn)
    print(dataframe.to_string(index=False))


def closeDB(db_connect, db_cursor):
    db_connect.commit()
    db_cursor.close()
    db_connect.close()


