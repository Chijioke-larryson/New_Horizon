import sqlite3
Connection = sqlite3.connect("result.db")


crsr = Connection.cursor()

crsr.execute("SELECT * FROM student WHERE first_name == 'James' AND last_name == 'Titus'")

data = crsr.fetchall()
print(data)

