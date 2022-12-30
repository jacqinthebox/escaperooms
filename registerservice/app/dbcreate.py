import pyodbc
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine to the database
engine = create_engine('mssql+pyodbc://sa:123Tralala^@localhost/master?driver=ODBC+Driver+17+for+SQL+Server')



# Define a model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.fullname}', password='{self.password}')>"


# Create the table in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user to the table
new_user = User(name='newuser', fullname='New User', password='password')
session.add(new_user)
session.commit()

# Query the users table
users = session.query(User).all()
print(users)
# Output: [<User(name='newuser', fullname='New User', password='password')>]
