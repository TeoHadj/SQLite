import sqlite3
from faker import Faker
import random

connection = sqlite3.connect('space.db')

cursor = connection.cursor()

start = '''
DROP TABLE IF EXISTS Planets;
'''
cursor.execute(start)

create_table_planets = '''

CREATE TABLE IF NOT EXISTS Planets(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
name TEXT NOT NULL, 
diameter REAL NOT NULL, 
galaxy TEXT NOT NULL, 
moons INTEGER NOT NULL, 
aliens INTEGER NOT NULL
);

'''

cursor.execute(create_table_planets)

add_planets = '''
INSERT INTO Planets(name, diameter, galaxy, moons, aliens) 
VALUES("Earth",12756, "Milky Way", 1, 0);
'''
cursor.execute(add_planets)

insert_data = '''
INSERT INTO Planets(name, diameter, galaxy, moons, aliens) 
VALUES(?,?,?,?,?)
'''
cursor.execute(insert_data, ("Venus", 12104, "Milky Way", 0, 0))

insert_data2 = """
INSERT INTO Planets(name, diameter, galaxy, moons, aliens) 
VALUES(?,?,?,?,?)
"""
cursor.execute(insert_data2, ("Saturn", 74897, "Milky Way", 146, 1))



fake = Faker('en_GB')



cursor.execute("DROP table IF EXISTS Persons")

create_persons_table = """ 
CREATE TABLE IF NOT EXISTS Persons ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  firstname TEXT NOT NULL, 
  lastname TEXT NOT NULL, 
  age INTEGER, 
  gender TEXT,
  id_planets INTEGER NOT NULL, FOREIGN KEY(id_planets) REFERENCES Planets(id)
); 
"""
cursor.execute(create_persons_table)

parameterised_insert_query = """ 
INSERT INTO  
    Persons (firstname, lastname, age, gender, id_planets) 
VALUES 
    (?, ?, ?, ?, ?); 
"""


fake.random.seed(2560)
random.seed(2560)
for _ in range(10):

    l_name = fake.last_name()
    age = random.randint(11, 18)
    gender = random.choice(('male', 'female'))
    planets_id = random.randint(1, 3)
    if gender == 'male':
        f_name = fake.first_name_male()
    else:
        f_name = fake.first_name_female()
    cursor.execute(parameterised_insert_query,
                   (f_name, l_name, age, gender, planets_id))






final_query = """
SELECT Persons.firstname, Persons.lastname, Planets.name
FROM Persons
LEFT JOIN Planets ON Persons.id_planets = Planets.id
"""

cursor.execute(final_query)
query_result = cursor.fetchall()
for line in query_result:
    print(line)

connection.commit()
connection.close()