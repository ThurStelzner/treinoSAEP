from funcoes import conexao, descriptografarDado

def login():
    conn = conexao()
    cursor = conexao.cursor()

    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")