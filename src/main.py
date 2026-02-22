import database as db

conn, cur = db.initDB()
print(cur)

def testCode():
    #input students
    name = input("Enter name: ")
    id = int(input("Enter id:"))
    db.inputStudent(cur, id, name)

    #ouput students
    op = db.outputStudents(cur)
    for i in op:
        print(i)

    db.closeDB(conn, cur)
