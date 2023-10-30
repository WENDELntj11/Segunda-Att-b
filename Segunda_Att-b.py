lista_pessoas = []
nome_tipo_sanguineo = {}
nome_arquivo = "lista_tipos_sanguineos.txt"


def adicionar_nome_e_tipo_sanguineo():
    nome = input("Digite um Nome da pessoa: ")
    tipo_sanguineo = input(f"Digite o tipo sanguíneo de {nome}: ")
    pessoa = {
        "Nome": nome,
        "Tipo Sanguíneo": tipo_sanguineo
    }
    lista_pessoas.append(pessoa)
    print(f"Dados de {nome} ({tipo_sanguineo}) foram adicionados com sucesso! ")


def visualizar_lista():
    if not lista_pessoas:
        print("A lista está vazia! ")
    else:
        print("Lista de nomes e tipos sanguíneos:")
        for pessoa in lista_pessoas:
            print(
                f"Nome: {pessoa['Nome']}, Tipo Sanguíneo: {pessoa['Tipo Sanguíneo']}")
    print()


def salvar_dados():
    with open(nome_arquivo, "w") as arquivo:
        for pessoa in lista_pessoas:
            arquivo.write(
                f"Nome: {pessoa['Nome']}, Tipo Sanguíneo: {pessoa['Tipo Sanguíneo']}\n")
        print(" Os dados foram salvos com sucesso no arquivo 'lista_tipos_sanguineos.txt'! ")
    print()


def carregar_dados():
    try:
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(", ")
                nome = dados[0].split(": ")[1]
                tipo_sanguineo = dados[1].split(": ")[1]
                pessoa = {
                    "Nome": nome,
                    "Tipo Sanguíneo": tipo_sanguineo
                }
                lista_pessoas.append(pessoa)
            print("Dados foram carregados com sucesso! \n")

    except FileNotFoundError:
        print(
            f"Erro! \nO arquivo {nome_arquivo} não foi encontrado. Certifique-se de que o arquivo existe ou crie um arquivo 'lista_tipos_sanguineos.txt'. \n")


carregar_dados()

while True:
    print("\nOpções: ")
    print("1. Adicione  algum novo nome e um tipo sanguíneo à lista")
    print("2. Visualizar a lista atual de nomes e tipos sanguíneos")
    print("3. Salvar a lista em um arquivo de texto")
    print("4. Finalizar")

    opc = input()
    if opc == "1":
        adicionar_nome_e_tipo_sanguineo()
    elif opc == "2":
        visualizar_lista()
    elif opc == "3":
        salvar_dados()
    elif opc == "4":
        break
    else:
        print("Essa opção e inválida! ")