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
    
    def getVendedoresNome(self) -> list:
        self.conectar()
        
        self.cursor.execute("SELECT nome FROM vendedores")
        vendedores_nome = self.cursor.fetchall()
        
        self.desconectar()
        
        return [vendedor[0] for vendedor in vendedores_nome]
    
    def getCompradoresNome(self) -> list:
        self.conectar()
        
        self.cursor.execute("SELECT nome FROM compradores")
        compradores_nome = self.cursor.fetchall()
        
        self.desconectar()
        
        return [comprador[0] for comprador in compradores_nome]
    
    def getItensNome(self) -> list:
        self.conectar()
        
        self.cursor.execute("SELECT nome FROM itens")
        itens_nome = self.cursor.fetchall()
        
        self.desconectar()
        
        return [item[0] for item in itens_nome]
    
    def getCompradorDinheiro(self, nome: str) -> float:
        self.conectar()
        
        self.cursor.execute("SELECT dinheiro FROM compradores WHERE nome=?", (nome,))
        dinheiro = self.cursor.fetchone()
        
        self.desconectar()
        
        if dinheiro:
            return dinheiro[0]
        else:
            return 0
        
    def getItemPreco(self, nome: str) -> float:
        self.conectar()
        
        self.cursor.execute("SELECT preco FROM itens WHERE nome=?", (nome,))
        preco = self.cursor.fetchone()
        
        self.desconectar()
        
        if preco:
            return preco[0]
        else:
            return 0
        
    def setCompradorDinheiro(self, nome: str, dinheiro: float) -> float:
        self.conectar()
        
        self.cursor.execute("UPDATE compradores SET dinheiro=? WHERE nome=?", (self.getCompradorDinheiro(nome) - dinheiro, nome))
        self.connection.commit()
        
        self.desconectar()
        
        return self.getCompradorDinheiro(nome)
    
    def getItensCarrinho(self, nome: str) -> str:
        self.conectar()
        
        self.cursor.execute("SELECT carrinho FROM compradores WHERE nome=?", (nome,))
        carrinho = self.cursor.fetchone()
        
        self.desconectar()
        
        if carrinho:
            return carrinho[0]
        else:
            return ""
        
    def adicionarItemCarrinho(self, nome: str, item: str) -> None:
        carrinho = self.getItensCarrinho(nome)
        
        carrinho = carrinho + " " + item
        
        self.conectar()
        
        self.cursor.execute("UPDATE compradores SET carrinho=? WHERE nome=?", (carrinho, nome))
        self.connection.commit()
        
        self.desconectar()
        
    def setItemCarrinho(self, nome: str, carrinho: str) -> None:
        self.conectar()
        
        self.cursor.execute("UPDATE compradores SET carrinho=? WHERE nome=?", (carrinho, nome))
        self.connection.commit()
        
        self.desconectar()
    
if __name__ == '__main__':
    pass