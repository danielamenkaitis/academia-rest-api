from app.models.baseGym import BaseGym


class Exercicio(BaseGym):
    nomeexercicio: str
    instrucao: str
    url: str
    