
class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getEmail(self):
        return self.email
