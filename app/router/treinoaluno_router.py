from fastapi import APIRouter
from app.services.treinoaluno_service import addService, deleteService, findAllService, findService, updateService
from app.models.treinoaluno import TreinoAluno
from app.utils.utils import responseFill


router = APIRouter()


@router.get("/{id}")
def findRouter(id: int):
    result = findService(id)
    return responseFill(result, f"TreinoAluno id: {id} não encontrado")

@router.get("/")
def allRouter():
    result = findAllService()
    return responseFill(result, f"TreinoAluno não encontrado")

@router.post("/")
def addRouter(treinoaluno: TreinoAluno):
    id = addService(treinoaluno)
    return responseFill(f"TreinoAluno inserido com sucesso Id: {id}", "Erro ao tentar inserir treino")

@router.put("/{id}")
def upadateRouter(id: int, treinoaluno: TreinoAluno):
    id = updateService(id, treinoaluno)
    return responseFill(f"TreinoAluno atualizado com sucesso, id: {id}", "Erro ao tentar atualizar treino")

@router.delete("/{id}")
def deleteRouter(id: int):
    id = deleteService(id)
    return responseFill(f"TreinoAluno id: {id} desativado com sucesso", "Erro ao tentar desativar Treino")