'''SQL using Python SQLITE3'''
''' The Primarykey is a unique key that identies each record in a table'''

import sqlite3

connection = sqlite3.connect('result.db')
crsr = connection.cursor()

# ensure a fresh table when creating
crsr.execute("DROP TABLE IF EXISTS student")
sql_command = """
CREATE TABLE student (
id INTEGER PRIMARY KEY,
first_name VARCHAR(20),
last_name VARCHAR (20),
gender CHAR (1),
joining_date DATE


);
"""
crsr.execute(sql_command)


sql_command = """
INSERT INTO student VALUES(1, "James", "Theif", "M","2000-04-25")

"""

crsr.execute(sql_command)


sql_command = """
INSERT INTO student VALUES(2, "John", "Theif", "M","2000-04-25")

"""

crsr.execute(sql_command)


sql_command = """
INSERT INTO student VALUES(11, "Jude", "Larry", "M","2000-04-25")

"""

crsr.execute(sql_command)


sql_command = """
INSERT INTO student VALUES(301, "James", "Titus", "M","2022-04-25")

"""

crsr.execute(sql_command)


sql_command = """
INSERT INTO student VALUES(401, "Jake", "Blake", "M","2002-04-25")

"""

crsr.execute(sql_command)


connection.commit()    # To save changes made


#Closing connect

connection.close()

