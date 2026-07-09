import sqlite3

db = sqlite3.connect('database.db')

# db.execute("INSERT INTO students VALUES('1','LARRYSON','1')")
'''
db.commit()
db.execute("INSERT INTO students VALUES('2','LARRY','2')")

db.commit()
db.execute("INSERT INTO students VALUES('3','JOHN','3')")

db.commit()
db.execute("INSERT INTO students VALUES('4','MERCY','4')")

db.commit()

'''
db.execute("INSERT INTO students(name,course_id) VALUES('John','7')")

db.commit()

# db.execute("INSERT INTO courses VALUES('1','PYTHON')")

# db.commit()

# db.execute("INSERT INTO courses VALUES('2','SQL')")

# db.commit()

# db.execute("INSERT INTO courses VALUES('3','JAVASCRIPT')")

# db.commit()
# db.execute("INSERT INTO courses VALUES('4','JAVASCRIPT')")

# db.commit()



