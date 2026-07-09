import sqlite3
db = sqlite3.connect('database.db')

joins = db.execute('''
SELECT students.name,
courses.course_name

FROM students

JOIN courses

ON students.course_id = courses.id;
           ''').fetchall()
db.commit()
for join in joins: 

    print(join)