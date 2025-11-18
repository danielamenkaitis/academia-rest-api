from app.database.db import executeCommand, executeCommandSelect, executeSelect
from app.models.treinoexercicio import TreinoExercicio
from app.utils.utils import fill


def findService(id: int):
    sql = f"SELECT id,idtreino,idexercicio,datacadastro,ativo,idusuario FROM treinoexercicio WHERE ATIVO = 'S' AND id = {id}"
    return fill(executeSelect(sql), TreinoExercicio)

def findAllService():
    sql = f"SELECT id,idtreino,idexercicio,datacadastro,ativo,idusuario FROM treinoexercicio WHERE ATIVO = 'S'"
    return fill(executeSelect(sql), TreinoExercicio)

def addService(treinoexercicio: TreinoExercicio):
    sql = f"""insert into treinoexercicio (idtreino, idexercicio, idusuario)
              values({treinoexercicio.idtreino}, {treinoexercicio.idexercicio}, {treinoexercicio.idusuario}) RETURNING id"""
    result = executeCommandSelect(sql)
    (id, ) = result[0]
    return id

def updateService(id: int, treinoexercicio: TreinoExercicio):
    sql = f"""UPDATE treinoexercicio SET idtreino = {treinoexercicio.idtreino}, idexercicio = {treinoexercicio.idexercicio}
              WHERE id = {id} AND ativo = 'S'"""
    return executeCommand(sql)

def deleteService (id: int):
    sql = f"UPDATE treinoexercicio SET ativo = 'N' WHERE id = {id}"
    return executeCommand(sql)