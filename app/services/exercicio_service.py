from app.database.db import executeCommand, executeCommandSelect, executeSelect
from app.models.exercicio import Exercicio
from app.utils.utils import fill


def findService(id: int): 
    sql = f"SELECT id,nomeexercicio,instrucao,url,datacadastro,ativo,idusuario FROM exercicio WHERE ativo = 'S' and id = {id}"
    return fill(executeSelect(sql),Exercicio)

def findAllService(): 
    sql = f"SELECT id,nomeexercicio,instrucao,url,datacadastro,ativo,idusuario FROM exercicio WHERE ativo = 'S'"
    return fill(executeSelect(sql),Exercicio)

def addService(exercicio: Exercicio):
    sql = f"""insert into exercicio (nomeexercicio, instrucao, url, idusuario)
              values('{exercicio.nomeexercicio}', '{exercicio.instrucao}', '{exercicio.url}', {exercicio.idusuario})RETURNING id"""
    result = executeCommandSelect(sql)
    (id, ) = result[0]
    return id

def updateService(id: int, exercicio: Exercicio):
    sql = f"""UPDATE exercicio SET nomeexercicio = '{exercicio.nomeexercicio}', instrucao = '{exercicio.instrucao}', url = '{exercicio.url}'
              WHERE id = {id} AND ativo = 'S'"""
    return executeCommand(sql)

def deleteService (id: int):
    sql = f"UPDATE exercicio SET ativo = 'N' WHERE id = {id}"
    return executeCommand(sql)