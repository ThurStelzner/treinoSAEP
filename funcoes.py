import mysql.connector as mysql
import base64

def conexao():
    return mysql.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'pythondb'
    )

def criptografarDados(dado):
    return base64.b64encode(dado.encode('utf-8')).decode('utf-8')

def descriptografarDado(dado):
    try:
        return base64.b64decode(dado).decode('utf-8')
    except:
        return dado