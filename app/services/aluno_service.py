from app.database.db import executeCommand, executeCommandSelect, executeSelect
from app.models.aluno import Aluno
from app.models.baseGym import BaseGym
from app.utils.utils import fill


def findService(id: int):
    sql = f"SELECT a.id, a.nome, a.email, a.whatsapp, a.observacao, a.datacadastro, a.ativo, a.idusuario FROM ALUNO as a WHERE ativo= 'S' and a.id = {id}"
    return fill(executeSelect(sql),Aluno)

def findAllService():
    sql = f"SELECT a.id, a.nome, a.email, a.whatsapp, a.observacao, a.datacadastro, a.ativo, a.idusuario FROM ALUNO as a WHERE ativo= 'S'"
    return fill(executeSelect(sql),Aluno)

def addService(aluno: Aluno):
    sql = f"""INSERT INTO aluno (nome, email, whatsapp, observacao, idUsuario) 
             VALUES ('{aluno.nome}', '{aluno.email}', '{aluno.whatsapp}', '{aluno.observacao}',{aluno.idusuario}) RETURNING id"""
    result= executeCommandSelect(sql)
    (id, ) = result[0]
    return id

def updateService(id: int, aluno: Aluno):
    sql = f"UPDATE aluno SET nome = '{aluno.nome}', email = '{aluno.email}', whatsapp = '{aluno.whatsapp}'  WHERE id = {id} and ativo= 'S'"
    return executeCommand(sql)

def deleteService (id: int):
    sql = f"UPDATE aluno SET ativo = 'N' WHERE id = {id}"
    return executeCommand(sql)