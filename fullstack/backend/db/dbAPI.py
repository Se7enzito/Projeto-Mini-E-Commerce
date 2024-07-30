import sqlite3 as sql

class Gerenciamento():
    def __init__(self) -> None:
        self.database = "fullstack/backend/db/database.db"
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sql.connect(self.database)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

    def criar_tabelas(self) -> None:
        with self:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS compradores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                sobrenome TEXT NOT NULL,
                dinheiro REAL NOT NULL,
                cpf TEXT UNIQUE NOT NULL,
                carrinho TEXT
            )''')
            
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS vendedores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                sobrenome TEXT NOT NULL,
                cnpj TEXT UNIQUE NOT NULL
                )''')
            
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                vendedor_nome INTEGER,
                FOREIGN KEY(vendedor_nome) REFERENCES vendedores(nome)
                )''')

    def criarComprador(self, nome: str, sobrenome: str, dinheiro: float, cpf: str) -> None:
        with self:
            self.cursor.execute("INSERT INTO compradores (nome, sobrenome, dinheiro, cpf) VALUES (?,?,?,?)", 
                                (nome, sobrenome, dinheiro, cpf))

    def criarVendedor(self, nome: str, sobrenome: str, cnpj: str) -> None:
        with self:
            self.cursor.execute("INSERT INTO vendedores (nome, sobrenome, cnpj) VALUES (?,?,?)", 
                                (nome, sobrenome, cnpj))

    def criarItem(self, nome: str, preco: float, vendedor: str) -> None:
        with self:
            self.cursor.execute("INSERT INTO itens (nome, preco, vendedor_nome) VALUES (?,?,?)", 
                                (nome, preco, vendedor))

    def getCompradores(self) -> list:
        with self:
            self.cursor.execute("SELECT * FROM compradores")
            return self.cursor.fetchall()
    
    def getVendedores(self) -> list:
        with self:
            self.cursor.execute("SELECT * FROM vendedores")
            return self.cursor.fetchall()
    
    def getItens(self) -> list:
        with self:
            self.cursor.execute("SELECT * FROM itens")
            return self.cursor.fetchall()
    
    def getVendedoresNome(self) -> list:
        with self:
            self.cursor.execute("SELECT nome FROM vendedores")
            return [vendedor[0] for vendedor in self.cursor.fetchall()]
    
    def getCompradoresNome(self) -> list:
        with self:
            self.cursor.execute("SELECT nome FROM compradores")
            return [comprador[0] for comprador in self.cursor.fetchall()]
    
    def getItensNome(self) -> list:
        with self:
            self.cursor.execute("SELECT nome FROM itens")
            return [item[0] for item in self.cursor.fetchall()]
    
    def getCompradorDinheiro(self, nome: str) -> float:
        with self:
            self.cursor.execute("SELECT dinheiro FROM compradores WHERE nome=?", (nome,))
            dinheiro = self.cursor.fetchone()
            return dinheiro[0] if dinheiro else 0
        
    def getItemPreco(self, nome: str) -> float:
        with self:
            self.cursor.execute("SELECT preco FROM itens WHERE nome=?", (nome,))
            preco = self.cursor.fetchone()
            return preco[0] if preco else 0
        
    def setCompradorDinheiro(self, nome: str, dinheiro: float) -> None:
        with self:
            self.cursor.execute("UPDATE compradores SET dinheiro=? WHERE nome=?", (dinheiro, nome))
    
    def getItensCarrinho(self, nome: str) -> list:
        with self:
            self.cursor.execute("SELECT carrinho FROM compradores WHERE nome=?", (nome,))
            carrinho = self.cursor.fetchone()
            return carrinho[0] if carrinho else ""

    def setItemCarrinho(self, nome: str, carrinho: str) -> None:
        with self:
            self.cursor.execute("UPDATE compradores SET carrinho=? WHERE nome=?", (carrinho, nome))

if __name__ == '__main__':
    pass