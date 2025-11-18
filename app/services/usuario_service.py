from app.database.db import executeCommand, executeCommandSelect, executeSelect
from app.models.usuario import Usuario
from app.utils.utils import fill


def findService(id: int): 
    sql = f"SELECT id,usuario,senha,tipo,datacadastro,ativo,idusuario FROM usuario WHERE ativo = 'S' and id = {id}"
    return fill(executeSelect(sql),Usuario)

def findAllService(): 
    sql = f"SELECT id,usuario,senha,tipo,datacadastro,ativo,idusuario FROM usuario WHERE ativo = 'S'"
    return fill(executeSelect(sql),Usuario)

def addService(usuario: Usuario):
    sql = f"""insert into usuario (usuario, senha, tipo, idusuario)
              values('{usuario.usuario}', '{usuario.senha}', '{usuario.tipo}', {usuario.idusuario}) RETURNING id"""
    result = executeCommandSelect(sql)
    (id, ) = result[0]
    return id

def updateService(id: int, usuario: Usuario):
    sql = f"""UPDATE usuario SET usuario = '{usuario.usuario}', senha = '{usuario.senha}', tipo = '{usuario.tipo}', idusuario = {usuario.idusuario}
              WHERE id = {id}"""
    return executeCommand(sql)

def deleteService (id: int):
    sql = f"UPDATE usuario SET ativo = 'N' WHERE id = {id}"
    return executeCommand(sql)