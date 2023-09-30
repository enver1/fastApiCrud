from pydantic import BaseModel
class UserSchema(BaseModel):
    codigo: int
    nombre: str
    

    