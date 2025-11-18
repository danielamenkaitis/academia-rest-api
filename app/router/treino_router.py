from fastapi import APIRouter
from app.models.treino import Treino
from app.services.treino_service import addService, deleteService, findAllService, findService, updateService
from app.utils.utils import responseFill


router = APIRouter()


@router.get("/{id}")
def findRouter(id: int):
    result = findService(id)
    return responseFill(result, f"Treino id: {id} não encontrado")

@router.get("/")
def allRouter():
    result = findAllService()
    return responseFill(result, f"Treino não encontrado")

@router.post("/")
def addRouter(treino: Treino):
    id = addService(treino)
    return responseFill(f"Treino {treino.treino} inserido com sucesso Id: {id}", "Erro ao tentar inserir treino")

@router.put("/{id}")
def upadateRouter(id: int, treino: Treino):
    id = updateService(id, treino)
    return responseFill(f"Treino atualizado com sucesso, id: {id}", "Erro ao tentar atualizar treino")

@router.delete("/{id}")
def deleteRouter(id: int):
    id = deleteService(id)
    return responseFill(f"Treino desativado com sucesso", "Erro ao tentar desativar Treino")