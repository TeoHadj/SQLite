import sqlite3 as sqlite

conn = sqlite.connect('db.sqlite')

c = conn.cursor()
# customer_query = """
# SELECT Artist.Name, COUNT(Album.AlbumId)
# FROM Artist
# INNER JOIN Album ON Artist.ArtistId = Album.ArtistId
# GROUP BY Artist.ArtistId
# ORDER BY COUNT(Album.AlbumId) DESC;
# """
#
# c.execute(customer_query)
#
# query_response = c.fetchall()
#
# for line in query_response:
#     print(line)



# customer_query = """
# SELECT Name, Composer
# FROM Track
# WHERE LOWER(Name) LIKE "% love %"
# OR LOWER(Name) LIKE "love %"
# OR LOWER(Name) LIKE "% love"
# OR LOWER(Name) LIKE "love"
# """
#
# c.execute(customer_query)
#
# query_response = c.fetchall()
#
# for line in query_response:
#     print(line)


# customer_query = """
# SELECT Track.Name, Composer
# FROM Track
# INNER JOIN Genre ON Track.GenreId = Genre.GenreId
# WHERE Genre.Name = "Rock"
# """
#
# c.execute(customer_query)
#
# query_response = c.fetchall()
#
# for line in query_response:
#     print(line)


customer_query = """ 
SELECT Album.Title, COUNT(Track.Name) as TrackNo
FROM Album
INNER JOIN Track
ON Album.AlbumId = Track.AlbumId
GROUP BY Album.AlbumId
ORDER BY TrackNo DESC
"""

c.execute(customer_query)

query_response = c.fetchone()

for line in query_response:
    print(line)