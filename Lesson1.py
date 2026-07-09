'''

What does CRUD mean?

Expected answers:

Create → INSERT
Read → SELECT
Update → UPDATE
Delete → DELETE
'''

'''
INSERT INTO students(name, age)
VALUES('John',20);

SELECT * FROM students;

UPDATE students
SET age=21
WHERE id=1;

DELETE FROM students
WHERE id=1;


''' 

'''
Database Relationships 
What is a Relationship?

A relationship shows how two
 or more tables are connected.


 What is a Relationship?

A relationship shows how two or more 
tables are connected.

Example:

Instead of putting everything inside one table,

Student
-------
John
Mary
James
Course
-------
Python
Java
SQL

connect them.

One-to-One Relationship

One student has one ID card.

Student
--------
1 John

ID Card
--------
1 CARD-001

One student ↔ One ID card

One-to-Many Relationship

One teacher teaches many students.

Teacher
--------
Mr Peter

Students
---------
John
Mary
James

One teacher → Many students

This is the most common relationship.

Many-to-Many Relationship

Many students take many courses.

Students
---------
John
Mary

Courses
--------
Python
SQL

Enrollment
-----------
John -> Python
John -> SQL
Mary -> SQL

Students and courses are connected 
using a third table.



SQL JOIN 
Why JOIN?

Suppose we have two tables.

Students
id	name	course_id
1	John	1
2	Mary	2
Courses
id	course_name
1	Python
2	SQL

How do we display

John Python
Mary SQL

Use JOIN.

INNER JOIN
SELECT students.name,
courses.course_name

FROM students

JOIN courses

ON students.course_id = courses.id;

Result

John Python

Mary SQL

Explain:

SQL starts from students.

Looks inside courses.

Matches

course_id

=

id

Returns matching rows.

LEFT JOIN

Returns every record from the left table.

Even if no match exists.

SELECT *
FROM students

LEFT JOIN courses

ON students.course_id=courses.id;
RIGHT JOIN

SQLite does not support RIGHT JOIN.

Mention this so students know.

CROSS JOIN

Returns every possible combination.

2 students

×

3 courses

=

6 rows

Example:

SELECT *

FROM students

CROSS JOIN courses;



ROLLBACK

Undo changes.

connection.rollback()

Example

import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

try:

    cursor.execute(
        "INSERT INTO students(name,age) VALUES(?,?)",
        ("Peter",20)
    )

    connection.commit()

except:

    connection.rollback()

connection.close()

Explain:

If an error occurs,

everything returns to its previous state.


'''