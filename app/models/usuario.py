from app.models.baseGym import BaseGym


class Usuario(BaseGym): 
    usuario: str
    senha: str
    tipo: str
    