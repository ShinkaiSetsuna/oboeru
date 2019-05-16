import sys
#for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String
#for configuration and class code
from sqlalchemy.ext.declarative import declarative_base
#for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship
#for configuration
from sqlalchemy import create_engine

#create declarative_base instance
Base = declarative_base()

class Sentence(Base):
   __tablename__ = 'sentences'
   id = Column(Integer, primary_key=True)
   sentence = Column(String(250), nullable=False)

#creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///sentences.sqlite3')

Base.metadata.create_all(engine)