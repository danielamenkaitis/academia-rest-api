from fastapi import APIRouter
from app.models.exercicio import Exercicio
from app.services.exercicio_service import addService, deleteService, findAllService, findService, updateService
from app.utils.utils import responseFill


router = APIRouter()


@router.get("/{id}")
def findRouter(id: int):
    result = findService(id)
    return responseFill(result, f"Exercicio id: {id} não encontrado")
    

@router.get("/")
def allRouter():
    result = findAllService()
    return responseFill(result, f"Exercicio não encontrado")
    

@router.post("/")
def addRouter(exercicio: Exercicio):
    id = addService(exercicio)
    return responseFill(f"Exercicio {exercicio.nomeexercicio} inserido com sucesso Id: {id}", "Erro ao tentar inserir exercicio")



@router.put("/{id}")
def upadateRouter(id: int, exercicio: Exercicio):
    id = updateService(id, exercicio)
    return responseFill(f"Exercicio atualizado com sucesso, id: {id}", "Erro ao tentar atualizar exercicio")
    


@router.delete("/{id}")
def deleteRouter(id: int):
    id = deleteService(id)
    return responseFill(f"Exercicio desativado com sucesso", "Erro ao tentar desativar exercicio")