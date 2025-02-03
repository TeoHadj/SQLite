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

insert_data2 = """
INSERT INTO planets(name, diameter, galaxy, moons, aliens) 
VALUES(?,?,?,?,?)
"""
cursor.execute(insert_data2, ("Saturn", 74897, "Milky Way", 146, 1))

my_query = '''
SELECT * FROM PLANETS
'''
cursor.execute(my_query)
#for item in cursor.execute(my_query):
    #print(item)

#query_response = cursor.fetchall()
#query_response = cursor.fetchone()
query_response = cursor.fetchmany(size = 3)

for line in query_response:
    print(line)


query2 = """
SELECT diameter,galaxy FROM PLANETS WHERE id = 2
"""
cursor.execute(query2)
query_response2 = cursor.fetchone()
for line in query_response2:
    print(line)

update = """
UPDATE PLANETS SET aliens = 0 WHERE id = 3
"""
cursor.execute(update)

cursor.execute(my_query)
query_response3 = cursor.fetchall()
for line in query_response3:
    print(line)

delete = """
DELETE FROM PLANETS WHERE id = 2
"""
cursor.execute(delete)
cursor.execute(my_query)
query_response4 = cursor.fetchall()
for line in query_response4:
    print(line)

connection.commit()
connection.close()