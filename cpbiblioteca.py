from cs02livro import Livro
from cs01aluno import Aluno


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        self.alunos = []

    def adicionarLivro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def removerLivro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f"Livro '{livro.titulo}' removido da biblioteca.")
        else:
            print("Livro não encontrado.")

    def listarLivros(self):
        print("\n===== LIVROS DA BIBLIOTECA =====")

        if not self.livros:
            print("Nenhum livro cadastrado.")
            return

        for livro in self.livros:
            livro.imprimir()

    def buscarLivro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                print("\nLivro encontrado:")
                livro.consultar()
                return livro

        print("Livro não encontrado.")
        return None

    def cadastrarAluno(self, aluno):
        self.alunos.append(aluno)
        print(f"Aluno '{aluno.nome}' cadastrado na biblioteca.")

    def listarAlunos(self):
        print("\n===== ALUNOS DA BIBLIOTECA =====")

        if not self.alunos:
            print("Nenhum aluno cadastrado.")
            return

        for aluno in self.alunos:
            print(
                f"ID: {aluno.idCliente} | "
                f"Nome: {aluno.nome} | "
                f"Matrícula: {aluno.matricula} | "
                f"Curso: {aluno.curso}"
            )

    def emprestarLivro(self, livro, aluno):
        if livro not in self.livros:
            print("Esse livro não pertence à biblioteca.")
            return

        if aluno not in self.alunos:
            print("Esse aluno não está cadastrado na biblioteca.")
            return

        if livro.emprestar():
            print(
                f"Empréstimo realizado para o aluno "
                f"{aluno.nome}."
            )

    def devolverLivro(self, livro):
        if livro in self.livros:
            livro.devolver()
        else:
            print("Esse livro não pertence à biblioteca.")
