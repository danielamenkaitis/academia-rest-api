from fastapi import APIRouter
from app.models.usuario import Usuario
from app.services.usuario_service import addService, deleteService, findAllService, findService, updateService
from app.utils.utils import responseFill

router = APIRouter()


@router.get("/{id}")
def findRouter(id: int):
    result = findService(id)
    return responseFill(result, f"Usuário id: {id} não encontrado")

@router.get("/")
def allRouter():
    result = findAllService()
    return responseFill(result, f"Usuário não encontrado")

@router.post("/")
def addRouter(usuario: Usuario):
    id = addService(usuario)
    return responseFill(f"Usuário {usuario.usuario} inserido com sucesso Id: {id}", "Erro ao tentar inserir usuário")

@router.put("/{id}")
def upadateRouter(id: int, usuario: Usuario):
    id = updateService(id, usuario)
    return responseFill(f"Usuário atualizado com sucesso, id: {id}", "Erro ao tentar atualizar usuário")

@router.delete("/{id}")
def deleteRouter(id: int):
    id = deleteService(id)
    return responseFill(f"Usuário desativado com sucesso", "Erro ao tentar desativar usuário")