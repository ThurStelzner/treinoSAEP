import mysql.connector as mysql

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

def cadastrar():
    conn = conexao()
    cursor = conn.cursor(dictionary=True)

    