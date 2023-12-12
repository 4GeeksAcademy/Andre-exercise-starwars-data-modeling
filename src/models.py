import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)

class Planet(Base): 
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    population = Column(Integer)

class Favorite_Planets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True) 
    planets = Column(Integer, ForeignKey('planet.id'))
    planet_id = relationship(Planet)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Vehicle(Base): 
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100))

class Favorite_Vehicles(Base):
    __tablename__ = 'favorite_vehicles'
    id = Column(Integer, primary_key=True) 
    vehicles = Column(Integer, ForeignKey('vehicle.id'))
    vehicle_id = relationship(Vehicle)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Character(Base): 
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    height = Column(String(100))
    planet = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class Favorite_Characters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True) 
    characters = Column(Integer, ForeignKey('character.id'))
    character_id = relationship(Character)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Vehicle_Pilots(Base):
    __tablename__ = 'vehicle_pilots'
    id = Column(Integer, primary_key=True) 
    characters = Column(Integer, ForeignKey('character.id'))
    character_id = relationship(Character)
    vehicles = Column(Integer, ForeignKey('vehicle.id'))
    vehicle_id = relationship(Vehicle)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
