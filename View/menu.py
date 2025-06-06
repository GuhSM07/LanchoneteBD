from Controller.PessoaController import inserir_pessoa, listar_pessoas
from Model.Pessoa import Pessoa

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Cadastrar Pessoa")
        print("2. Listar Pessoas")
        print("0. Sair")
        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            celular = input("Celular: ")
            p = Pessoa(nome=nome, celular=celular)
            inserir_pessoa(p)
            print("Pessoa cadastrada com sucesso.")
        elif op == "2":
            pessoas = listar_pessoas()
            for p in pessoas:
                print(f"ID: {p[0]} | Nome: {p[1]} | Celular: {p[2]}")
        elif op == "0":
            break
        else:
            print("Opção inválida.")
