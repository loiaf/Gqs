from pessoa import Pessoa


class CadastroPessoas:
    def __init__(self):
        self.__pessoas = []

    def cadastrar(self, nome, idade, email):
        pessoa = Pessoa(nome, idade, email)
        self.__pessoas.append(pessoa)

    def buscar(self, nome):
        pos = 0
        while pos < len(self.__pessoas):
            if self.__pessoas[pos].nome == nome:
                return pos
            pos = pos + 1
        return -1

    def consultar(self, nome):
        pos = self.buscar(nome)
        if pos == -1:
            return None
        return self.__pessoas[pos]

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        pos = self.buscar(nome)
        if pos == -1:
            return False

        self.__pessoas[pos].nome = novo_nome
        self.__pessoas[pos].idade = nova_idade
        self.__pessoas[pos].email = novo_email
        return True

    def listar(self):
        return self.__pessoas