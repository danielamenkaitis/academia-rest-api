
def fill(lista, classe):
    (data, filed) = lista
    return [classe(**dict(zip(filed, item))) for item in data] if data else []


def responseFill(sucesso, erro):
    if sucesso:
       return {"mensagem": sucesso}
   
    return {"mensagem": erro}

