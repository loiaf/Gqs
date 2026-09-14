
# Sistema de Cadastro de Pessoas - versao refatorada

def buscar_pessoa(nomes, procurado):
    for i in range(len(nomes)):
        if nomes[i] == procurado:
            return i
    return -1


def classificar_faixa_etaria(idade):
    if idade < 12:
        return "Crianca"
    elif idade < 18:
        return "Adolescente"
    elif idade < 30:
        return "Adulto Jovem"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"


def avaliar_email(email):
    if email == "":
        return "Sem E-mail"
    elif "@" not in email:
        return "Invalido"
    else:
        return "Utilizavel"


def identificar_provedor(email):
    if email.endswith("@gmail.com"):
        return "Gmail"
    elif email.endswith("@outlook.com"):
        return "Outlook"
    elif email.endswith("@hotmail.com"):
        return "Hotmail"
    elif email.endswith("@utfpr.edu.br"):
        return "Utfpr"
    else:
        return "Outro"


def definir_condicao_contato(idade, email):
    if idade >= 18 and email != "":
        return "Cadastro apto para contato"
    elif idade >= 18 and email == "":
        return "Maior de Idade sem contato"
    elif idade < 18 and email != "":
        return "Menor de Idade com contato"
    else:
        return "Menor de idade sem contato"


def analisar_pessoa(nomes, idades, emails):
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
    if len(nomes) == 3:
        print("Cadastro cheio")
    else:
        n = input("Nome: ")
        i = int(input("Idade: "))
        e = input("E-mail: ")

        nomes.append(n)
        idades.append(i)
        emails.append(e)

        print("Pessoa cadastrada!")
        print("Nome: " + n)
        print("Idade: " + str(i))
        print("E-mail: " + e)

        if i >= 18:
            print("Situacao: Maior de idade")
        else:
            print("Situacao: Menor de idade")


def consultar_pessoa(nomes, idades, emails):
    procurado = input("Nome para consultar: ")
    pos = buscar_pessoa(nomes, procurado)

    if pos == -1:
        print("Nao encontrado")
    else:
        print("Nome: " + nomes[pos])
        print("Idade: " + str(idades[pos]))
        print("E-mail: " + emails[pos])

        if idades[pos] >= 18:
            print("Situacao: Maior de idade")
        else:
            print("Situacao: Menor de idade")


def alterar_pessoa(nomes, idades, emails):
    procurado = input("Nome para alterar: ")
    pos = buscar_pessoa(nomes, procurado)

    if pos == -1:
        print("Nao encontrado")
    else:
        print("Dados atuais:")
        print("Nome: " + nomes[pos])
        print("Idade: " + str(idades[pos]))
        print("E-mail: " + emails[pos])

        n = input("Novo nome: ")
        i = int(input("Nova idade: "))
        e = input("Novo e-mail: ")

        nomes[pos] = n
        idades[pos] = i
        emails[pos] = e

        print("Alterado!")


def listar_pessoas(nomes, idades, emails):
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada")

    for i in range(len(nomes)):
        print("Nome: " + nomes[i])
        print("Idade: " + str(idades[i]))
        print("E-mail: " + emails[i])
        print("-------------------------")

    print("Total: " + str(len(nomes)))


nomes = []
idades = []
emails = []
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
        cadastrar_pessoa(nomes, idades, emails)

    elif op == 2:
        consultar_pessoa(nomes, idades, emails)

    elif op == 3:
        alterar_pessoa(nomes, idades, emails)

    elif op == 4:
        listar_pessoas(nomes, idades, emails)

    elif op == 5:
        analisar_pessoa(nomes, idades, emails)

    elif op == 6:
        print("Saindo...")

    else:
        print("Opcao invalida")

print("Fim do programa")