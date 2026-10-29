from funcoes import conexao, criptografarDados

def login():
    try: 
        conn = conexao()
        cursor = conn.cursor(dictionary=True)

        apelido = input("Digite seu apelido: ").strip()
        senha = input("Digite sua senha: ").strip()
        senhaCripto = criptografarDados(senha) 

        sql = "SELECT * FROM tb_usuario WHERE apelido = %s"

        cursor.execute(sql, (apelido,))
        usuario = cursor.fetchone()

        if usuario and senhaCripto == usuario['senha']:
            print("Logado!")
        else:
            print("Usuário ou senha incorretos...")        

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    login()