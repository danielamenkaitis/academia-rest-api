from fastapi import APIRouter
from app.models.aluno import Aluno
from app.services.aluno_service import addService, deleteService, findService, findAllService, updateService
from app.utils.utils import responseFill

router = APIRouter()

@router.get("/{id}")
def findRouter(id: int):
    result = findService(id)
    return responseFill(result, f"Aluno com id {id} não encontrado")
    
@router.get("/")
def allRouter():
    result = findAllService()
    return responseFill(result, f"Alunos não encontrado")

@router.post("/")
def addRouter(aluno: Aluno):
    id = addService(aluno)
    return responseFill(f"Aluno {aluno.nome} inserido com sucesso Id: {id}", "Erro ao tentar inserir aluno")

@router.put("/{id}")
def updateRouter(id: int, aluno: Aluno):
    id = updateService(id, aluno)
    return responseFill(f"Aluno atualizado com sucesso, id: {id}", "Erro ao tentar atualizar aluno")

@router.delete("/{id}")
def deleteRouter(id: int):
    id = deleteService(id)
    return responseFill(f"Aluno desativado com sucesso", "Erro ao tentar desativar aluno")
