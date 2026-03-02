import database as db





def testCode():
    conn, cur = db.initDB()
    import pandas as pd
    import numpy as np
    #input students

    name = input("Enter name: ")
    id = int(input("Enter id:"))
    db.inputStudent(cur, id, name)

    #ouput students
    db.outputStudents(conn)
    db.createMonthTable(cur, 3, 2026)
    db.outputTables(conn)
    

    db.closeDB(conn, cur)
