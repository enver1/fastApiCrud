
from model.users import Usuario 
from schema.user_schema import UserSchema
from sqlalchemy.orm import Session

def create_user(db: Session, usuario: Usuario):
    new_user = Usuario(codigo=usuario.codigo, nombre=usuario.nombre)
    db.add(new_user)
    db.commit()
    db.flush(new_user)
    return new_user