import sqlite3
from faker import Faker
import random

fake = Faker('en_GB')

conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()

cursor.execute("DROP table IF EXISTS students")

create_students_table = """ 
CREATE TABLE IF NOT EXISTS students ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  firstname TEXT NOT NULL, 
  lastname TEXT NOT NULL, 
  age INTEGER, 
  gender TEXT 
); 
"""
cursor.execute(create_students_table)

parameterised_insert_query = """ 
INSERT INTO  
    students (firstname, lastname, age, gender) 
VALUES 
    (?, ?, ?, ?); 
"""


fake.random.seed(4321)
random.seed(4321)
for _ in range(10):
    f_name = fake.first_name()
    l_name = fake.last_name()
    age = random.randint(11, 18)
    gender = random.choice(('male', 'female'))
    cursor.execute(parameterised_insert_query,
                   (f_name, l_name, age, gender))


print_query = """
SELECT * FROM students;
"""
cursor.execute(print_query)

query_response=cursor.fetchall()
for line in query_response:
    print(line)