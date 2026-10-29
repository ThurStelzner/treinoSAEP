from funcoes import conexao, criptorafarDado

def cadastrar():
    try:          
        conn = conexao()
        cursor = conn.cursor(dictionary=True)

        nome = input("Digite seu nome: ")
        apelido = input("Digite como gostaria de ser chamado: ")
        senha = input("Digite sua senha: ")

        senhaCripto = criptorafarDado(senha)

        sql = "INSERT INTO tb_usuario (nome, senha, apelido) VALUES (%s, %s, %s)"

        cursor.execute(sql, (nome, senhaCripto, apelido))
        conn.commit()
        print("Cadastrado com sucesso!")

    except Exception as e:
        print(f"Erro inesperado! {e}")

    finally:
        cursor.close()
        conn.close()

cadastrar()