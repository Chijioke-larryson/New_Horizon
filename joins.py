import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

query = """
SELECT students.name,
courses.course_name

FROM students

JOIN courses

ON students.course_id = courses.id
"""

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()