
import os
from urllib.parse import urlparse
import psycopg2


def connect():
    
    # Pega a variável de ambiente
    DATABASE_URL = os.getenv("DATABASE_URL")

    # Faz o parse da URL
    url = urlparse(DATABASE_URL)

    # Conecta usando os campos separados
    connection = psycopg2.connect(
        host=url.hostname,
        port=url.port,
        database=url.path[1:],  # remove a barra inicial
        user=url.username,
        password=url.password
    )
        
    #connection = psycopg2.connect(dbname="gym", user="ahfneto", password="", host="meu-postgres", port="5432")
    return connection

def executeCommand(sql):
    try:
        connection = connect()
        command = connection.cursor()
        command.execute(sql)
        connection.commit()
        rowcount = command.rowcount
        command.close()
        connection.close()
        return rowcount
    except Exception as ex:
        print(f"\033[91mErro: {ex} ao executar comando: {sql}\033[0m")
        return False 

def executeCommandSelect(sql):
    try:
        connection = connect()
        command = connection.cursor()
        command.execute(sql)
        data = command.fetchall()
        connection.commit()
        command.close()
        connection.close()
        return data 
    except Exception as ex:
        print(f"\033[91mErro: {ex} ao executar comando: {sql}\033[0m")
        return [], []
    
def executeSelect(sql):
    try:
        connection = connect()
        command = connection.cursor()
        command.execute(sql)
        data = command.fetchall()
        filed = [desc[0] for desc in command.description]  # nomes das colunas
        connection.commit()
        command.close()
        connection.close()
        return (data, filed) ## retorna uma tupla
    except Exception as ex:
        print(f"\033[91mErro: {ex} ao executar comando: {sql}\033[0m")
        return [], []


