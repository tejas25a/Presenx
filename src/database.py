from pathlib import Path 
import sqlite3

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

def inputStudent(db_cursor, id, name):
    if (id == None):
        print("Error: id cannot be NULL\nIt is a primary key. ")
        return
    if (name == None):
        print("Error: name field is  required\n")
        return

    db_cursor.execute(f"INSERT INTO students values({id}, '{name}')")

def outputStudents(db_cursor):
    db_cursor.execute("SELECT * FROM students")
    output = db_cursor.fetchall()
    return output



def closeDB(db_connect, db_cursor):
    db_connect.commit()
    db_cursor.close()


