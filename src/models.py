from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    planet_climate = Column(String(250))
    planet_terrain = Column(String(250), nullable=False)
    planet_population = Column(Integer)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    character_eyes_color = Column(String(250))
    character_hair_color = Column(String(250), nullable=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    favorite_planet_id = Column(Integer, ForeignKey('planet.id'))
    favorite_planet = relationship(Planet)
    favorite_character_id = Column(Integer, ForeignKey('character.id'))
    favorite_character = relationship(Character)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship((User))
    


    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')
