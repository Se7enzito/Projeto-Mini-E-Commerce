from libs.classes import Comprador, Vendedor, Item

compradores = {}
vendedores = []
itens = {}

def criarComprador(nome: str, sobrenome: str, dinheiro: float, cpf: str) -> None:
    comp = Comprador(nome, sobrenome, dinheiro, cpf)
    compradores[comp] = []

def getComprador(nome: str) -> Comprador:
    for comprador in compradores.keys():
        if comprador.nome == nome:
            return comprador
    return None

def getCarrinho(nome: str) -> list:
    comprador = getComprador(nome)
    
    if comprador:
        return compradores[comprador]
    else:
        return None

def criarVendedor(nome: str, sobrenome: str, cnpj: str) -> None:
    vendedor = Vendedor(nome, sobrenome, cnpj)
    vendedores.append(vendedor)

def getVendedor(nome: str) -> Vendedor:
    for vendedor in vendedores:
        if vendedor.nome == nome:
            return vendedor
    return None

def criarItem(nome: str, preco: float, nome_vendedor: str) -> None:
    vendedor = getVendedor(nome_vendedor)
    item = Item(nome, preco, nome_vendedor)
    
    if vendedor not in itens:
       itens[vendedor] = [item]
    elif item not in itens[vendedor]:
        itens[vendedor] = itens[vendedor].append(item)

def getItem(nome: str) -> Item:
    for item_list in itens.values():
        for item in item_list:
            if item.nome == nome:
                return item
    return None

def addItem(comprador: Comprador, item: Item) -> None:
    dinheiro = comprador.dinheiro
    valor = item.preco
    
    listaComprador = compradores[comprador]
    compradores.pop(comprador)
    
    if (dinheiro >= valor):
        listaComprador.append(item)
        compradores[comprador] = listaComprador
        print("Produto adicionado com sucesso")
    else:
        print("Você não possui dinheiro suficiente para o produto")
    
if __name__ == '__main__':
    condicao = True
    
    while condicao:
        print("\nMenu:")
        print("1 - Criar comprador")
        print("2 - Criar vendedor")
        print("3 - Criar item")
        print("4 - Adicionar item ao carrinho de um comprador")
        print("5 - Mostrar carrinho de um comprador")
        print("6 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        try:
            opcao = int(opcao)
        except:
            print("Digite um número!")
            continue
        
        if opcao == 1:
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            
            cond = True
            while cond:
                dinheiro = input("Dinheiro: ")
                
                try:
                    dinheiro = float(dinheiro)
                    
                    break
                except:
                    cont = input("Deseja tentar novamente? (S/N)")
                    
                    if cont.upper() == "N":
                        cond = False
                    else:
                        cond = True
                    
                    print("Digite um número!")
                    
            if cond == False:
                continue
            
            cpf = input("CPF: ")
            
            criarComprador(nome, sobrenome, dinheiro, cpf)
            
        elif opcao == 2:
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            cnpj = input("CNPJ: ")
            
            criarVendedor(nome, sobrenome, cnpj)
            
        elif opcao == 3:
            contador = 0
            cond = True
            
            for vendedor in vendedores:
                contador += 1
            
            if contador == 0:
                print("É necessário ter um vendedor para criar um item.")
                continue
            
            nome = input("Nome: ")
    
            cond = True
            while cond:
                preco = input("Preço: ")
                
                try:
                    preco = float(preco)
                    
                    break
                except:
                    cont = input("Deseja tentar novamente? (S/N)")
                    
                    if cont.upper() == "N":
                        cond = False
                    else:
                        cond = True
                    
                    print("Digite um número!")
                    
            if cond == False:
                continue

            nome_vendedor = input("Nome do vendedor: ")
            
            criarItem(nome, preco, nome_vendedor)
        
        elif opcao == 4:
            comprador = input("Comprador: ")
            
            if getComprador(comprador) == None:
                print("Comprador não encontrado.")
                continue
            
            comprador = getComprador(comprador)
            
            item = input("Nome do item: ")
            
            if getItem(item) == None:
                print("Item não encontrado.")
                continue
            
            item = getItem(item)
                
            addItem(comprador, item)
            
        elif opcao == 5:
            comprador = input("Comprador: ")
            
            if getComprador(comprador) == None:
                print("Comprador não encontrado.")
                continue
            
            carrinho = getCarrinho(comprador)
            print(carrinho)
        
        elif opcao == 6:
            condicao = False
            
        else:
            print("Escolha uma opção válida...")