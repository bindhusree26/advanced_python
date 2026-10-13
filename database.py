# a database is a place where data is stored in an orgainzed manner
#connecting to the db with error handling
import sqlite3
try:
    connection = sqlite3.connect("student.db")# student.db is a db being created
    print("connected")
except:
    print("connection failed")
finally:
    connection.close()

# executing SQL queries
import sqlite3
connection = sqlite3.connect("student.db")# opens the database student.db
cursor = connection.cursor()# cursor() specifies the pointer to add the data
# execute() is used to execute the given sql query
cursor.execute("""
CREATE TABLE IF NOT EXISTS student
(id INTEGER,
name TEXT,
age INTEGER)
""")# creating the heading for the table
connection.commit()
connection.close()

# inserting the data for the created table
import sqlite3
connection = sqlite3.connect("student.db")# opens the database student.db
cursor = connection.cursor()
cursor.execute("INSERT INTO student VALUES(1,'ABC',75)")
connection.commit()
connection.close()

# reading the data 
import sqlite3
conn = sqlite3.connect("student.db")# opens the database student.db
cursor = conn.cursor()
cursor.execute("SELECT * FROM student")
print(cursor.fetchall())
conn.close()