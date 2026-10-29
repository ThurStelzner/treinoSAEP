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

def cadastrar():
    try:          
        conn = conexao()
        cursor = conn.cursor(dictionary=True)

        nome = input("Digite seu nome: ")
        apelido = input("Digite como gostaria de ser chamado: ")
        senha = input("Digite sua senha: ")

        sql = "INSERT INTO tb_usuario (nome, senha, apelido) VALUES (%s, %s, %s)"

        cursor.execute(sql, (nome, senha, apelido))
        conn.commit()
        print("Cadastrado com sucesso!")

    except Exception as e:
        print(f"Erro inesperado! {e}")

    finally:
        cursor.close()
        conn.close()