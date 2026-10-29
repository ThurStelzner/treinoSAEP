import mysql.connector as mysql
import base64

def conexao():
    try:
        return mysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'pythondb'
        )
        print("Conectado!")
    except Exception as e:
        print(f"Erro de conexão: {e}")

def criptorafarDado(dado):
    return base64.b64encode(dado.encode('utf-8')).decode('utf-8')

def descriptografarDado(dado):
    try:
        return base64.b64decode(dado).decode('utf-8')
    except:
        return dado