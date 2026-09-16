"""Sistema de cadastro e analise de pessoas."""


def buscar_pessoa(nomes, procurado):
    """Localiza uma pessoa pelo nome."""
    for i, nome in enumerate(nomes):
        if nome == procurado:
            return i
    return -1


def classificar_faixa_etaria(idade):
    """Classifica a pessoa conforme a idade."""
    if idade < 12:
        return "Crianca"
    if idade < 18:
        return "Adolescente"
    if idade < 30:
        return "Adulto Jovem"
    if idade < 60:
        return "Adulto"
    return "Idoso"


def avaliar_email(email):
    """Verifica se o e-mail esta ausente, invalido ou utilizavel."""
    if email == "":
        return "Sem E-mail"
    if "@" not in email:
        return "Invalido"
    return "Utilizavel"


def identificar_provedor(email):
    """Identifica o provedor do e-mail."""
    if email.endswith("@gmail.com"):
        return "Gmail"
    if email.endswith("@outlook.com"):
        return "Outlook"
    if email.endswith("@hotmail.com"):
        return "Hotmail"
    if email.endswith("@utfpr.edu.br"):
        return "Utfpr"
    return "Outro"


def definir_condicao_contato(idade, email):
    """Define a condicao da pessoa para contato."""
    if idade >= 18 and email != "":
        return "Cadastro apto para contato"
    if idade >= 18:
        return "Maior de Idade sem contato"
    if email != "":
        return "Menor de Idade com contato"
    return "Menor de idade sem contato"


def analisar_pessoa(nomes, idades, emails):
    """Realiza a analise de uma pessoa cadastrada."""
    procurado = input("Nome pra Analise: ")
    pos = buscar_pessoa(nomes, procurado)

    if pos == -1:
        print("Pessoa nao encontrada")
        return

    idade = idades[pos]
    email = emails[pos]

    faixa = classificar_faixa_etaria(idade)
    situacao_email = avaliar_email(email)
    condicao = definir_condicao_contato(idade, email)

    print("Faixa Etaria: " + faixa)

    if situacao_email == "Sem E-mail":
        print("Cadastro Incompleto: Sem E-mail")
    elif situacao_email == "Invalido":
        print("E-mail invalido")
    else:
        provedor = identificar_provedor(email)
        print("Provedor: " + provedor)

    print(condicao)


def cadastrar_pessoa(nomes, idades, emails):
    """Cadastra uma nova pessoa."""
    if len(nomes) >= 3:
        print("Cadastro cheio")
        return

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("E-mail: ")

    nomes.append(nome)
    idades.append(idade)
    emails.append(email)

    print("Pessoa cadastrada!")
    print("Nome: " + nome)
    print("Idade: " + str(idade))
    print("E-mail: " + email)

    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")


def consultar_pessoa(nomes, idades, emails):
    """Consulta uma pessoa pelo nome."""
    procurado = input("Nome para consultar: ")
    pos = buscar_pessoa(nomes, procurado)

    if pos == -1:
        print("Nao encontrado")
        return

    print("Nome: " + nomes[pos])
    print("Idade: " + str(idades[pos]))
    print("E-mail: " + emails[pos])

    if idades[pos] >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")


def alterar_pessoa(nomes, idades, emails):
    """Altera os dados de uma pessoa."""
    procurado = input("Nome para alterar: ")
    pos = buscar_pessoa(nomes, procurado)

    if pos == -1:
        print("Nao encontrado")
        return

    print("Dados atuais:")
    print("Nome: " + nomes[pos])
    print("Idade: " + str(idades[pos]))
    print("E-mail: " + emails[pos])

    nome = input("Novo nome: ")
    idade = int(input("Nova idade: "))
    email = input("Novo e-mail: ")

    nomes[pos] = nome
    idades[pos] = idade
    emails[pos] = email

    print("Alterado!")


def listar_pessoas(nomes, idades, emails):
    """Lista todas as pessoas cadastradas."""
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada")

    for i, nome in enumerate(nomes):
        print("Nome: " + nome)
        print("Idade: " + str(idades[i]))
        print("E-mail: " + emails[i])
        print("-------------------------")

    print("Total: " + str(len(nomes)))


lista_nomes = []
lista_idades = []
lista_emails = []
op = 0

while op != 6:
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Analisar Pessoa")
    print("6 - Sair")

    op = int(input("Escolha uma opcao: "))

    if op == 1:
        cadastrar_pessoa(lista_nomes, lista_idades, lista_emails)
    elif op == 2:
        consultar_pessoa(lista_nomes, lista_idades, lista_emails)
    elif op == 3:
        alterar_pessoa(lista_nomes, lista_idades, lista_emails)
    elif op == 4:
        listar_pessoas(lista_nomes, lista_idades, lista_emails)
    elif op == 5:
        analisar_pessoa(lista_nomes, lista_idades, lista_emails)
    elif op == 6:
        print("Saindo...")
    else:
        print("Opcao invalida")

print("Fim do programa")
