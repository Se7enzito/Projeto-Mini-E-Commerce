class Comprador():
    def __init__(self, nome, sobrenome, dinheiro, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dinheiro = dinheiro
        self.cpf = cpf

    def __repr__(self):
        return f"Comprador(nome={self.nome}, sobrenome={self.sobrenome}, dinheiro={self.dinheiro}, cpf={self.cpf})"

    def __hash__(self):
        return hash((self.nome, self.sobrenome, self.cpf))

    def __eq__(self, other):
        if isinstance(other, Comprador):
            return (self.nome, self.sobrenome, self.cpf) == (other.nome, other.sobrenome, other.cpf)
        return False
    
class Vendedor():
    def __init__(self, nome: str, sobrenome: str, cnpj: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cnpj = cnpj  

    def __repr__(self):
        return f"Vendedor(nome={self.nome}, sobrenome={self.sobrenome}, cnpj={self.cnpj})"

    def __hash__(self):
        return hash((self.nome, self.sobrenome, self.cnpj))

    def __eq__(self, other):
        if isinstance(other, Vendedor):
            return (self.nome, self.sobrenome, self.cnpj) == (other.nome, other.sobrenome, other.cnpj)
        return False          

class Item():
    def __init__(self, nome: str, preco: float, vendedor: str):
        self.nome = nome
        self.preco = preco
        self.vendedor = vendedor

    def __repr__(self):
        return f"Comprador(nome={self.nome}, preco={self.preco}, vendedor={self.vendedor})"

    def __hash__(self):
        return hash((self.nome, self.preco, self.vendedor))

    def __eq__(self, other):
        if isinstance(other, Item):
            return (self.nome, self.preco, self.vendedor) == (other.nome, other.preco, other.vendedor)
        return False
        
if __name__ == '__main__':
    pass