
from app.database.db import executeCommand, executeCommandSelect, executeSelect

from app.models.treinoaluno import TreinoAluno
from app.utils.utils import fill


def findService(id: int): 
    sql = f"SELECT id,idtreino,idaluno,datacadastro,ativo,idusuario FROM treinoaluno WHERE ativo = 'S' and id = {id}"
    return fill(executeSelect(sql),TreinoAluno)

def findAllService(): 
    sql = f"SELECT id,idtreino,idaluno,datacadastro,ativo,idusuario FROM treinoaluno WHERE ativo = 'S'"
    return fill(executeSelect(sql),TreinoAluno)

def addService(treinoaluno: TreinoAluno):
    sql = f"""insert into treinoaluno (idtreino, idaluno, idusuario)
              values({treinoaluno.idtreino}, {treinoaluno.idaluno}, {treinoaluno.idusuario})RETURNING id"""
    result = executeCommandSelect(sql)
    (id, ) = result[0]
    return id

def updateService(id: int, treinoaluno: TreinoAluno):
    sql = f"""UPDATE treinoaluno SET idtreino = {treinoaluno.idtreino}, idaluno = {treinoaluno.idaluno}
              WHERE id = {id} AND ativo = 'S'"""
    return executeCommand(sql)

def deleteService (id: int):
    sql = f"UPDATE treinoaluno SET ativo = 'N' WHERE id = {id}"
    return executeCommand(sql)