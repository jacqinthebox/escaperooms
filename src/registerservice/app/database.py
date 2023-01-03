from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mssql+pyodbc://sa:123Tralala^@localhost/master?driver=ODBC+Driver+17+for+SQL+Server')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
	import models
	Base.metadata.create_all(bind=engine)



