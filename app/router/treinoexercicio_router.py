from fastapi import APIRouter
from app.models.treinoexercicio import TreinoExercicio
from app.services.treinoexercicio_service import deleteService, findAllService, findService, addService, updateService
from app.utils.utils import responseFill

router = APIRouter()

@router.get("/{id}")
def findRouter(id: int):
    result = findService(id)
    return responseFill(result, f"TreinoExercicio id: {id} não encontrado")

@router.get("/")
def allRouter():
    result = findAllService()
    return responseFill(result, f"TreinoExercicio id: {id} não encontrado")

@router.post("/")
def addRouter(treinoexercicio: TreinoExercicio):
    id = addService(treinoexercicio)
    return responseFill(f"TreinoExercicio Id: {id} inserido com sucesso!!!", "Erro ao tentar inserir treino")

@router.put("/{id}")
def upadateRouter(id: int, treinoexercicio: TreinoExercicio):
    id = updateService(id, treinoexercicio)
    return responseFill(f"TreinoExercicio Id: {id} atualizado com sucesso!!!", "Erro ao tentar atualizar treino")

@router.delete("/{id}")
def deleteRouter(id: int):
    id = deleteService(id)
    return responseFill(f"TreinoExercicio id: {id} desativado com sucesso!!!", "Erro ao tentar desativar Treino")