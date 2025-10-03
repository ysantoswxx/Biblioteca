import sqlite3

conexao = sqlite3.connect("Biblioteca.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo TEXT NOT NULL,
    Autor TEXT NOT NULL,                              
    Ano INTERGER,            
    Disponivel TEXT NOT NULL           
)
""")


def inserir_livros (Titulo,Autor,Ano):
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()
        cursor.execute("""
        INSERT INTO livros (Titulo,Autor,Ano,Disponivel)
        VALUES (?,?,?,?)                   
        """,
        (Titulo,Autor,Ano,"sim")
        )
        conexao.commit()  
    except Exception as erro:
        print(f"erro ao inserir o livro {erro}")
    finally:
        if conexao:
            conexao.close()
Titulo  = input("Digite o Titulo do livro: ").lower()
Autor = input("Digite o Autor do livro: ").lower()
Ano = int(input("Digite a Ano do livro: "))
inserir_livros(Titulo,Autor,Ano)

