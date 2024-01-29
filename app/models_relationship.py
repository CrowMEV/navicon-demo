from datetime import datetime

import sqlalchemy as sa
from base_db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Artist(Base):
    __tablename__ = "artist"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    albums: Mapped[list["Album"]] = relationship(back_populates="artist")


class Album(Base):
    __tablename__ = "album"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    published: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    id_artist: Mapped[int] = mapped_column(sa.ForeignKey("artist.id"))
    artist: Mapped["Artist"] = relationship(back_populates="albums")
    tracks: Mapped[list["Track"]] = relationship(back_populates="album")


class Genre(Base):
    __tablename__ = "genre"
    id: Mapped[int] = mapped_column(primary_key=True)
    tracks: Mapped[list["Track"]] = relationship(
        secondary="track_to_genre", back_populates="genres"
    )


track_to_genre = sa.Table(
    "track_to_genre",
    Base.metadata,
    sa.Column("genre_id", sa.Integer, sa.ForeignKey("genre.id")),
    sa.Column("track_id", sa.Integer, sa.ForeignKey("track.id")),
)


class Track(Base):
    __tablename__ = "track"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    duration: Mapped[int]

    id_album: Mapped[int] = mapped_column(sa.ForeignKey("album.id"))
    genres: Mapped[list[Genre]] = relationship(
        secondary=track_to_genre, back_populates="tracks"
    )
    album: Mapped["Album"] = relationship(back_populates="tracks")
