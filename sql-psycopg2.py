import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook", password='123')

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# We need to use a Python string placeholder, and then define the desired string within a list.
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [52])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [52])

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])
# cursor.execute('select * from "Track" where "AlbumId" = %s', [5])
# cursor.execute('select * from "Track" where "Composer" = %s', ["AC/DC"])
# terminal: SELECT * FROM "Track" WHERE "Composer" = 'AC/DC';
cursor.execute('select * from "Track" where "Composer" = %s', ["Test"])


# Query 7 - select only tracks with the length more than 2950000 sec.
# cursor.execute('SELECT * FROM "Track" WHERE "Milliseconds" > 2950000')

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
