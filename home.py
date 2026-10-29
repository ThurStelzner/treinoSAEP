from cadastro import cadastrar
from login import login

def home():
    while True:
        print("===Treino SAEP===")
        print("1. Cadastro")
        print("2. Login")
        print("0. Sair")
        print("=================")

        r = input("Qual opção deseja: ").strip()

        match r:
            case "0":
                print("Saindo...")
                break
            case "1":
                cadastrar()
            case "2":
                login()
            case _:
                print("Opção não é válida...")

if __name__ == "__main__":
    home()