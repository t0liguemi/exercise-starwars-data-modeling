import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorite = relationship('Favorite')


class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    fav_character_id = Column(Integer, ForeignKey("character.id"))
    fav_planet_id = Column(Integer, ForeignKey("planet.id"))
    fav_starship_id = Column(Integer, ForeignKey("starship.id"))
    fav_film_id = Column(Integer, ForeignKey("film.id"))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(Integer)
    gender = Column(String(250))
    homeworld = Column(ForeignKey('planet.id'))
    film = relationship('film')
    favorite = relationship('Favorite')


class Planet(Base):
    __tablename__='planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(250))
    gravity = Column(Integer)
    terrain = Column(String(250))
    population = Column(Integer)
    film = relationship('Film')
    favorite = relationship('Favorite')

class Starship(Base):
    __tablename__='starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)   
    model = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atm_speed = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    starship_class = Column(String(250))
    favorite = relationship('Favorite')
    film = relationship('Film')

class Film(Base):
    __tablename__='film'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    director = Column(String(250))
    producer = Column(String(250))
    release_date = Column(Integer)
    character_id = Column(ForeignKey('character.id'))
    starship_id = Column(ForeignKey('starship.id'))
    planet_id = Column(ForeignKey('planet.id'))
    favorite = relationship('Favorite')


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
