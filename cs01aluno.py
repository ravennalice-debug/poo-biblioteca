class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def cadastrar(self):
        print(f"Pessoa {self.nome} cadastrada com sucesso!")

    def editar(self, nome=None, cpf=None):
        if nome:
            self.nome = nome

        if cpf:
            self.cpf = cpf

        print(f"Dados de {self.nome} atualizados!")

    def excluir(self):
        print(f"Pessoa {self.nome} excluída.")

    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")


class Aluno(Pessoa):
    def __init__(self, nome, cpf, idCliente, matricula, curso):
        super().__init__(nome, cpf)

        self.idCliente = idCliente
        self.matricula = matricula
        self.curso = curso

    def cadastrar(self):
        print(f"Aluno {self.nome} cadastrado com sucesso!")

    def editar(self, nome=None, cpf=None, matricula=None, curso=None):
        if nome:
            self.nome = nome

        if cpf:
            self.cpf = cpf

        if matricula:
            self.matricula = matricula

        if curso:
            self.curso = curso

        print(f"Aluno {self.nome} atualizado com sucesso!")

    def excluir(self):
        print(f"Aluno {self.nome} excluído.")

    def apresentar(self):
        print("\n--- Dados do Aluno ---")
        print(f"ID Cliente: {self.idCliente}")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Matrícula: {self.matricula}")
        print(f"Curso: {self.curso}")

    def pegarEmprestimo(self, livro):
        if livro.emprestar():
            print(
                f"O aluno {self.nome} pegou o livro "
                f"'{livro.titulo}' emprestado."
            )
            return True

        return False
