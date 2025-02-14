import sqlite3 as sqlite

conn = sqlite.connect('db.sqlite')

c = conn.cursor()

customer_query = """ 
SELECT COUNT(TrackId)
FROM Track
"""

c.execute(customer_query)

query_response = c.fetchone()

print(query_response[0])


