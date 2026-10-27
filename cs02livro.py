class Livro:
    def __init__(self, idLivro, titulo, autor, isbn, ano):
        self.idLivro = idLivro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano = ano
        self.disponivel = True

    def cadastrar(self):
        print(f"Livro '{self.titulo}' cadastrado com sucesso!")

    def editar(self, titulo=None, autor=None, isbn=None, ano=None):
        if titulo:
            self.titulo = titulo

        if autor:
            self.autor = autor

        if isbn:
            self.isbn = isbn

        if ano:
            self.ano = ano

        print(f"Livro '{self.titulo}' atualizado com sucesso!")

    def excluir(self):
        print(f"Livro '{self.titulo}' excluído.")

    def consultar(self):
        print("\n--- Dados do Livro ---")
        print(f"ID: {self.idLivro}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Ano: {self.ano}")
        print(f"Disponível: {'Sim' if self.disponivel else 'Não'}")

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
            return True
        else:
            print(f"O livro '{self.titulo}' não está disponível.")
            return False

    def devolver(self):
        self.disponivel = True
        print(f"O livro '{self.titulo}' foi devolvido.")

    def imprimir(self):
        print(
            f"{self.idLivro} - {self.titulo} - "
            f"{self.autor} - {self.ano}"
        )
