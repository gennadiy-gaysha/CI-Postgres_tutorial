# Table, Column, Float, ForeignKey, Integer, String, and MetaData are used to
# define the structure of the database tables and columns.
from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
# db = create_engine("postgresql:///chinook")

# In this code, the connection string should be provided as an argument to
# the create_engine function. Based on the code you shared previously, you
# should modify the create_engine line as follows:
# connection_string = "postgresql://username:password@localhost:5433/database"
# engine = create_engine(connection_string)
# Here is the actual connection string for your PostgreSQL database:
db = create_engine("postgresql://postgres:123@localhost:5433/chinook")
#  db variable represents the database engine
# The database engine is responsible for establishing a connection to the
# database and providing an interface for executing SQL queries.
# By creating an instance of the database engine (db), We can connect to the
# specified database using the connection string and perform various operations
# such as executing queries, creating tables, and interacting with the database
# schema.

# Create a MetaData object:
# The MetaData object represents the collection of database objects (tables,
# columns, etc.) and is bound to the database engine (db).
# meta is an instance of the MetaData class. It is created by calling the MetaData()
# constructor with the db engine as an argument:
meta = MetaData(db)
# This line creates a new MetaData object and associates it with the specified
# database engine (db). The MetaData object serves as a container for storing
# metadata information about database tables, columns, constraints, and relationships.


# create variable for "Artist" table
# The Table function is used to create a table object for the "Artist" table.
# Columns are defined using the Column function, specifying the column name,
# data type, and any additional constraints.

# Once the MetaData object is created, you can define tables and other database
# objects under this metadata object using SQLAlchemy's Table and related classes.
# The MetaData object provides methods and attributes to manage and interact with
# the defined objects and their associated metadata.
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
# The with db.connect() as connection statement establishes a connection
# to the database and assigns it to the connection variable.
# The with statement ensures that the connection is properly closed after
# executing the code block.
with db.connect() as connection:
    # In the line with db.connect() as connection:, connect() is a method provided
    # by the SQLAlchemy Engine object (db in your code) to establish a connection
    # to the database. It returns a Connection object, which represents a connection
    # to the database.

    # Query 1 - select all records from the "Artist" table
    #  select_query = artist_table.select()

    # Query 2 - select only "Name" column from "Artist" table
    #  (select "Name" from "Artist";)
    #  select_query = artist_table.select().with_only_columns([
    #      artist_table.c.Name])

    # Query 3 - select only "Queen" from the "Artist" table
    #  (select * from "Artist" where "Name"='Queen';)
   #  select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only by "ArtistId" #51 from the "Artist" table
    # (select * from "Artist" where "ArtistId"=51;)
   #  select_query = artist_table.select().where(artist_table.c.ArtistId == 52)

    # Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
   #  (select * from "Album" where "ArtistId"=52;)
    select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is "Queen" from the "Track" table
   #  (select * from "Track" where "Composer"='Queen';)
   #  select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)
