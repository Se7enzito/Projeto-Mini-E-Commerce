from flask import Flask, render_template, request, url_for, redirect
from db.dbAPI import Gerenciamento

app = Flask(__name__, template_folder="../frontend/templates")

app.static_folder = '../frontend/src'
app.static_url_path = '/static'

geren = Gerenciamento()

@app.route('/')
def index():
    message = ''
    return render_template('index.html', message = message, compradores = geren.getCompradores(), vendedores = geren.getVendedores(), itens = geren.getItens())

@app.route('/criar_comprador', methods=['POST'])
def criar_comprador():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        dinheiro = request.form.get('dinheiro')
        cpf = request.form.get('cpf')
        
        try:
            dinheiro = float(dinheiro)
        except:
            return redirect(url_for('index', message = 'Digite apenas números no campo de Dinheiro'))
    
    geren.criarComprador(nome, sobrenome, dinheiro, cpf)
    
    return redirect(url_for('index', message = 'Comprador criado com sucesso'))

@app.route('/criar_vendedor', methods=['POST'])
def criar_vendedor():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        cnpj = request.form.get('cnpj')
        
        geren.criarVendedor(nome, sobrenome, cnpj)
        
        return redirect(url_for('index', message = 'Vendedor criado com sucesso'))

@app.route('/criar_item', methods=['POST'])
def criar_item():
    if request.method == 'POST':
        nome = request.form.get('nome')
        preco = request.form.get('preco')
        vendedor = request.form.get('vendedor')
        
        try:
            preco = float(preco)
        except:
            return redirect(url_for('index', message = 'Digite apenas números no campo de Preço'))
        
        vendedores = geren.getVendedoresNome()
        
        if vendedor not in vendedores:
            return redirect(url_for('index', message = 'Vendedor não encontrado'))
        
        geren.criarItem(nome, preco, vendedor)
        
        return redirect(url_for('index', message = 'Item criado com sucesso'))

@app.route('/adicionar_item', methods=['POST'])
def adicionar_item():
    if request.method == 'POST':
        comprador = request.form.get('comprador')
        item = request.form.get('item')
        
        compradores = geren.getCompradoresNome()
        
        if comprador not in compradores:
            return redirect(url_for('index', message = 'Comprador não encontrado'))
        
        itens = geren.getItensNome()
        
        if item not in itens:
            return redirect(url_for('index', message = 'Item não encontrado'))
        
        dinheiro = geren.getCompradorDinheiro(comprador)
        preco = geren.getItemPreco(comprador)
        
        if dinheiro < preco:
            return redirect(url_for('index', message = 'Dinheiro insuficiente'))
        
        geren.setCompradorDinheiro(comprador, dinheiro - preco)
        geren.adicionarItemCarrinho(comprador, item)
        
        return redirect(url_for('index', message = 'Item adicionado ao carrinho com sucesso'))

@app.route('/remover_item', methods=['POST'])
def remover_item():
    if request.method == 'POST':
        comprador = request.form.get('comprador')
        item = request.form.get('item')
        
        compradores = geren.getCompradoresNome()
        
        if comprador not in compradores:
            return redirect(url_for('index', message = 'Comprador não encontrado'))
        
        itens = geren.getItensCarrinho(comprador)
        
        if item not in itens:
            return redirect(url_for('index', message = 'Item não encontrado no carrinho'))
        
        listaItens = itens.split(' ')
        itensAtua = ""
        
        for i in listaItens:
            if i == item:
                listaItens.remove(i)
            else:
                itensAtua = itensAtua + " " + i
                
        geren.setItemCarrinho(comprador, itensAtua)
        
        return redirect(url_for('index', message = 'Item removido do carrinho com sucesso'))
                
@app.route('/ver_carrinho', methods=['POST'])
def ver_carrinho():
    if request.method == 'POST':
        comprador = request.form.get('comprador')
        
        compradores = geren.getCompradoresNome()
        
        if comprador not in compradores:
            return redirect(url_for('index', message = 'Comprador não encontrado'))
        
        carrinho = geren.getItensCarrinho(comprador)
        
        return redirect(url_for('index', carrinho = carrinho))

if __name__ == '__main__':
    geren.criar_tabelas()
    
    app.run(host='127.0.0.1', port=8000, debug=True)