from fastapi import FastAPI
from app.router.treinoexercicio_router import router as treinoexercicio_router
from app.router.treinoaluno_router import router as treinoaluno_router
from app.router.usuario_router import router as usuario_router
from app.router.treino_router import router as treino_router
from app.router.exercicio_router import router as exercicio_router
from app.router.aluno_router import router as aluno_router


app = FastAPI()
SITE = "/academia"
app.include_router(aluno_router, prefix=f"{SITE}/aluno/v1", tags=["Aluno"])
app.include_router(exercicio_router, prefix=f"{SITE}/exercicio/v1", tags=["Exercicio"])
app.include_router(treino_router, prefix=f"{SITE}/treino/v1", tags=["Treino"])
app.include_router(treinoaluno_router, prefix=f"{SITE}/treinoaluno/v1", tags=["Treinoaluno"])
app.include_router(treinoexercicio_router, prefix=f"{SITE}/treinoexercicio/v1", tags=["Treinoexercicio"])
app.include_router(usuario_router, prefix=f"{SITE}/usuario/v1", tags=["Usuario"])