from sqlalchemy import (
    create_engine, Column, Integer, String, Float, ForeignKey
)
# declarative_base function is used to create a base class for declarative models.
from sqlalchemy.ext.declarative import declarative_base
# When you import declarative_base from sqlalchemy.ext.declarative, you are importing
# a function that returns a base class. This base class acts as a foundation for your
# declarative models. You can create your own model classes by subclassing this base class.
from sqlalchemy.orm import sessionmaker

# executing the instructions from our localhost "chinook" db
# This tells the application that we're using the Postgres server, on a local host
# in order to connect to our Chinook database.
db = create_engine("postgresql://postgres:123@localhost:5433/chinook")
#  a variable called 'base', is set to the declarative_base() class
base = declarative_base()

# create a class-based model for the "Artist" table


class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
# create a class-based model for the "Album" table


class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)


# create a class-based model for the "Track" table
# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# Query 1 - select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select only "Name" column from "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - select only "Queen" from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     if artist.Name == "Queen":
#         print(artist.ArtistId, artist.Name, sep=' | ')

# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=' | ')

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=' | ')

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId)

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
