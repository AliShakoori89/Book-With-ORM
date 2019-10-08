import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String ,ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///bank.db', echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base = declarative_base()

class Publisher(Base):
    __tablename__ ="Publisher"
    ID=Column(Integer, primary_key=True)
    Name=Column(String(200))
    LastName=Column(String(200))
    Address=Column(String(500))
    Phone=Column(Integer)
    URL=Column(String)
    children=relationship('Book',back_populates="parent")

class Author(Base):
    __tablename__="Author"
    ID=Column(Integer,primary_key=True)
    Name=Column(String(200))
    LastName=Column(String(300))
    Address=Column(String(500))
    URL=Column(String(100))
    
class Book(Base):
    __tablename__="Book"
    ID=Column(Integer,primary_key=True)
    Publisher_ID=Column(Integer,ForeignKey('Publisher.ID'))
    ISBN=Column(Integer)
    Publisher_LastName=Column(String)
    Author_LastName=Column(String)
    Author_Address=Column(String)
    Year=Column(Integer)
    Title=Column(String)
    Price=Column(Integer)
    parent=relationship('Publisher',back_populates='children')
    def insert(self):
        Base.metadata.create_all(engine)
        Bo=Book(ID='1',Publisher_ID='1',ISBN=213122,Publisher_LastName='Shakoori',Author_LastName='Lesani',Author_Address='Rasht',\
                                    Year=1345,Title="kosesherhaye sooroosh",Price=25000)
        Pub=Publisher(ID='1',Name="Ali",LastName='Shakoori',Address='meydan gorgan',Phone="09381083275",URL='Alishakoori89@gmail.com')
        Aut=Author(ID='1',Name="Amir",LastName='Lesani',Address='Rasht',URL='Amirlesani@gmail.com')
        bo_au=Book_Author(ID='1',Book_ID='1',Author_ID='1')
        session.add(Bo)
        session.add(Pub)
        session.add(Aut)
        session.add(bo_au)
        session.commit()

class Book_Author(Base):
    __tablename__="Book_Author"
    ID=Column(Integer,primary_key=True)
    Book_ID=Column(Integer,ForeignKey('Book.ID'),primary_key=True)
    Author_ID=Column(Integer,ForeignKey('Author.ID'),primary_key=True)

    book=relationship('Book',backref='Book_Author')
    author=relationship('Author',backref='Book_Author')



obj2=Book()
obj2.insert()