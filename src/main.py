from cadastro import CadastroPessoas


def exibir_menu():
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    return int(input("Escolha uma opcao: "))


def exibir_pessoa(pessoa):
    print("Nome: " + pessoa.nome)
    print("Idade: " + str(pessoa.idade))
    print("E-mail: " + pessoa.email)
    if pessoa.idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")


cadastro = CadastroPessoas()

qtd = 0
op = 0

while op != 5:
    op = exibir_menu()

    if op == 1:
        nome = input("Informe o nome: ")
        idade = int(input("Informe a idade: "))
        email = input("Informe o email: ")
        cadastro.cadastrar(nome, idade, email)

        if idade >= 18:
            print("Situacao: Maior de idade")
        else:
            print("Situacao: Menor de idade")

    elif op == 2:
        procurado = input("Nome para consultar: ")
        pessoa = cadastro.consultar(procurado)

        if pessoa is None:
            print("Nao encontrado")
        else:
            exibir_pessoa(pessoa)

    elif op == 3:
        procurado = input("Nome para alterar: ")
        pessoa = cadastro.consultar(procurado)

        if pessoa is None:
            print("Nao encontrado")
        else:
            novo_nome = input("Novo nome: ")
            nova_idade = int(input("Nova idade: "))
            novo_email = input("Novo e-mail: ")
            cadastro.alterar(procurado, novo_nome, nova_idade, novo_email)
            print("Pessoa alterada!")
            exibir_pessoa(cadastro.consultar(novo_nome))

    elif op == 4:
        pessoas = cadastro.listar()

        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada")

        pos = 0
        while pos < len(pessoas):
            exibir_pessoa(pessoas[pos])
            print("-------------------------")
            pos = pos + 1

        print("Total: " + str(len(pessoas)))

    elif op == 5:
        print("Saindo...")
    else:
        print("Opcao invalida")

print("Fim do programa")