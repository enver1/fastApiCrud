from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine("mysql+pymysql://danilo:1234@localhost:3306/cursos")
conn = engine.connect()
localSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base() 