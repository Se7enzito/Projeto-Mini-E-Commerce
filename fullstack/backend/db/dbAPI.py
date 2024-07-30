import sqlite3 as sql

class Gerenciamento():
    def __init__(self) -> None:
        self.database = "fullstack/backend/db/database.db"
        self.connection = None
        self.cursor = None

    def conectar(self) -> None:
        self.connection = sql.connect(self.database)
        self.cursor = self.connection.cursor()

    def desconectar(self) -> None:
        self.connection.close()
        
    def criar_tabelas(self) -> None:
        self.conectar()
        
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
        
        self.connection.commit()
        
        self.desconectar()
        
    def criarComprador(self, nome: str, sobrenome: str, dinheiro: float, cpf: str) -> None:
        self.conectar()
        
        self.cursor.execute("INSERT INTO compradores (nome, sobrenome, dinheiro, cpf) VALUES (?,?,?,?)", (nome, sobrenome, dinheiro, cpf))
        
        self.connection.commit()
        
        self.desconectar()
        
    def criarVendedor(self, nome: str, sobrenome: str, cnpj: str) -> None:
        self.conectar()
        
        self.cursor.execute("INSERT INTO vendedores (nome, sobrenome, cnpj) VALUES (?,?,?)", (nome, sobrenome, cnpj))
        
        self.connection.commit()
        
        self.desconectar()
        
    def criarItem(self, nome: str, preco: float, vendedor: str) -> None:
        self.conectar()
        
        self.cursor.execute("INSERT INTO itens (nome, preco, vendedor_nome) VALUES (?,?,?)", (nome, preco, vendedor))
        
        self.connection.commit()
        
        self.desconectar()
        
    def getCompradores(self) -> list:
        self.conectar()
        
        self.cursor.execute("SELECT * FROM compradores")
        compradores = self.cursor.fetchall()
        
        self.desconectar()
        
        return compradores
    
    def getVendedores(self) -> list:
        self.conectar()
        
        self.cursor.execute("SELECT * FROM vendedores")
        vendedores = self.cursor.fetchall()
        
        self.desconectar()
        
        return vendedores
    
    def getItens(self) -> list:
        self.conectar()
        
        self.cursor.execute("SELECT * FROM itens")
        itens = self.cursor.fetchall()
        
        self.desconectar()
        
        return itens
        
if __name__ == '__main__':
    pass