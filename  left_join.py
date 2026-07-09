import sqlite3

db = sqlite3.connect('database.db')

left_joins = db.execute('''
SELECT *
FROM students

LEFT JOIN courses

ON students.course_id=courses.id;
           ''').fetchall()

db.commit()
for left_join in left_joins:
    print(left_join)