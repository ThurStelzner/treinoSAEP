from funcoes import conexao, criptografarDados
import mysql.connector as mysql

def cadastrar():
    conn = None
    cursor = None

    try:
        conn = conexao()
        cursor = conn.cursor(dictionary=True)

        nome = input("Digite seu nome: ").strip()
        apelido = input("Digite como gostaria de ser chamado: ").strip()
        senha = input("Digite sua senha: ").strip()

        senhaCripto = criptografarDados(senha)

        sql = "INSERT INTO tb_usuario (nome, senha, apelido) VALUES (%s, %s, %s)"

        cursor.execute(sql, (nome, senhaCripto, apelido))
        conn.commit()
        print("Cadastrado com sucesso!")

    except mysql.IntegrityError:
        print("Apelido já cadastrado")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    cadastrar()