
from app.database.db import executeCommand, executeCommandSelect, executeSelect

from app.models.treino import Treino
from app.utils.utils import fill


def findService(id: int): 
    sql = f"SELECT id,treino,instrucao,datacadastro,ativo,idusuario FROM treino WHERE ativo = 'S' and id = {id}"
    return fill(executeSelect(sql),Treino)

def findAllService(): 
    sql = f"SELECT id,treino,instrucao,datacadastro,ativo,idusuario FROM treino WHERE ativo = 'S'"
    return fill(executeSelect(sql),Treino)

def addService(treino: Treino):
    sql = f"""insert into treino (treino, instrucao, idusuario)
              values('{treino.treino}', '{treino.instrucao}', {treino.idusuario})RETURNING id"""
    result = executeCommandSelect(sql)
    (id, ) = result[0]
    return id

def updateService(id: int, treino: Treino):
    sql = f"""UPDATE treino SET treino = '{treino.treino}', instrucao = '{treino.instrucao}'
              WHERE id = {id} AND ativo = 'S'"""
    return executeCommand(sql)

def deleteService (id: int):
    sql = f"UPDATE treino SET ativo = 'N' WHERE id = {id}"
    return executeCommand(sql)