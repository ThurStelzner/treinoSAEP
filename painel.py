from funcoes import conexao, sessao

def painel():
    conn = None
    cursor = None

    if sessao['id'] == None:
        print("Você precisa estar logado para acessar o painel!")
        return
    
    try: 
        conn = conexao()
        cursor = conn.cursor()

        sql = "SELECT nome, apelido FROM tb_usuario"
        cursor.execute(sql)
        lista = cursor.fetchall()
        print(lista)
    except Exception as e:
        print(f"Erro: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    painel()