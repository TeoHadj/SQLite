import sqlite3

connection = sqlite3.connect('space.db')

cursor = connection.cursor()

start = '''
DROP TABLE IF EXISTS planets;
'''
cursor.execute(start)

create_table_planets = '''

CREATE TABLE IF NOT EXISTS planets(
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
INSERT INTO planets(name, diameter, galaxy, moons, aliens) 
VALUES("Earth",12756, "Milky Way", 1, 0);
'''
cursor.execute(add_planets)

insert_data = '''
INSERT INTO planets(name, diameter, galaxy, moons, aliens) 
VALUES(?,?,?,?,?)
'''
cursor.execute(insert_data, ("Venus", 12104, "Milky Way", 0, 0))

my_query = '''
SELECT * FROM PLANETS
'''

for item in cursor.execute(my_query):
    print(item)

connection.commit()
connection.close()