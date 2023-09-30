from fastapi import APIRouter
from config.db import conn
from model.users import Usuario
from pydantic import BaseModel
from model import crud
from model.users import Base
from config.db import engine, localSession
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends

Base.metadata.create_all(bind=engine)
user = APIRouter()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()


class Usuario(BaseModel):
    codigo: int
    nombre: str

@user.get("/")
def root():
    return {"message": "Hi, Soy FastApi con un router"}


@user.post("/usuarios")
def insertar_datos(usuario: Usuario, db: Session = Depends(get_db)):
    return crud.create_user(db=db, usuario=usuario)



