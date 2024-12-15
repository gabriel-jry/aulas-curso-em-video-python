def cadastrar_pessoa():
    print("\nCadastro de Pessoa\n" + "-"*20)
    nome = input("Digite o nome da pessoa: ")
    idade = input("Digite a idade da pessoa: ")

    with open("pessoas.txt", "a") as file:
        file.write(f"{nome},{idade}\n")
    
    print(f"\n{nome} cadastrado com sucesso!")

def ver_pessoas():
    try:
        with open("pessoas.txt", "r") as file:
            pessoas = file.readlines()

        if not pessoas:
            print("\nNenhuma pessoa cadastrada.")
        else:
            print("\nLista de pessoas cadastradas:")
            print("-" * 30)
            for pessoa in pessoas:
                nome, idade = pessoa.strip().split(',')
                print(f"Nome: {nome.ljust(20)} Idade: {idade}")
            print("-" * 30)
    except FileNotFoundError:
        print("\nNenhuma pessoa cadastrada.")

while True:
    print("\nMenu Principal\n" + "-"*15)
    print("1. Cadastrar Pessoa")
    print("2. Ver Pessoas Cadastradas")
    print("3. Sair")

    escolha = input("Escolha uma opção (1, 2 ou 3): ")

    match escolha:
        case '1':
            cadastrar_pessoa()
        case '2':
            ver_pessoas()
        case '3':
            print("\nSaindo do sistema. Até logo!")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")
