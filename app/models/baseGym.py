from datetime import datetime
from pydantic import BaseModel

class BaseGym(BaseModel):
    id: int
    datacadastro: datetime
    ativo: str
    idusuario: int    