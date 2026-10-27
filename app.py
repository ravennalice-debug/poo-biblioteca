from cpbiblioteca import Biblioteca
from cs01aluno import Aluno
from cs02livro import Livro


# Criando a biblioteca
biblioteca = Biblioteca("Biblioteca Central")


# Criando os livros
livro1 = Livro(
    1,
    "Dom Casmurro",
    "Machado de Assis",
    "978-85-359-0277-5",
    1899
)

livro2 = Livro(
    2,
    "O Cortiço",
    "Aluísio Azevedo",
    "978-85-7232-741-1",
    1890
)


# Criando o aluno
aluno1 = Aluno(
    "João",
    "123.456.789-00",
    1,
    2026001,
    "Análise e Desenvolvimento de Sistemas"
)


# =========================
# CADASTROS
# =========================

print("\n===== CADASTRO DOS LIVROS =====")

livro1.cadastrar()
livro2.cadastrar()

biblioteca.adicionarLivro(livro1)
biblioteca.adicionarLivro(livro2)


print("\n===== CADASTRO DO ALUNO =====")

aluno1.cadastrar()
biblioteca.cadastrarAluno(aluno1)


# =========================
# LISTAGENS
# =========================

biblioteca.listarLivros()

biblioteca.listarAlunos()


# =========================
# APRESENTAÇÃO DO ALUNO
# =========================

print("\n===== ALUNO =====")

aluno1.apresentar()


# =========================
# BUSCA DE LIVRO
# =========================

print("\n===== BUSCA DE LIVRO =====")

biblioteca.buscarLivro("Dom Casmurro")


# =========================
# EMPRÉSTIMO
# =========================

print("\n===== EMPRÉSTIMO =====")

biblioteca.emprestarLivro(livro1, aluno1)


# Verificando situação do livro
livro1.consultar()


# =========================
# TENTANDO EMPRESTAR NOVAMENTE
# =========================

print("\n===== NOVO EMPRÉSTIMO =====")

biblioteca.emprestarLivro(livro1, aluno1)


# =========================
# DEVOLUÇÃO
# =========================

print("\n===== DEVOLUÇÃO =====")

biblioteca.devolverLivro(livro1)


# Verificando situação do livro
livro1.consultar()
