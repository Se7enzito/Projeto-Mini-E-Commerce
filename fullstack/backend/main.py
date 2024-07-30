from flask import Flask, render_template, request, url_for, redirect
from db.dbAPI import Gerenciamento
import re, ast

app = Flask(__name__, template_folder="../frontend/templates")

app.static_folder = '../frontend/src'
app.static_url_path = '/static'

geren = Gerenciamento()

def parse_carrinho(carrinho_str):
    carrinho_str = carrinho_str.replace(" ", "")
    carrinho_str = carrinho_str.replace("[[", "[").replace("]]", "]")

    items = re.findall(r'\[([^\]]+)\]', carrinho_str)
    
    result = []
    for item in items:
        result.append(item.split(','))
    
    return result

@app.route('/')
def index():
    carrinho = request.args.get('carrinho', '')
    return render_template('index.html', compradores=geren.getCompradores(), vendedores=geren.getVendedores(), itens=geren.getItens(), carrinho=carrinho)

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
            return redirect(url_for('index'))
    
    geren.criarComprador(nome, sobrenome, dinheiro, cpf)
    
    return render_template('index.html', message='Comprador criado com sucesso', compradores=geren.getCompradores(), vendedores=geren.getVendedores(), itens=geren.getItens())

@app.route('/criar_vendedor', methods=['POST'])
def criar_vendedor():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        cnpj = request.form.get('cnpj')
        
        geren.criarVendedor(nome, sobrenome, cnpj)
        
        return redirect(url_for('index'))

@app.route('/criar_item', methods=['POST'])
def criar_item():
    if request.method == 'POST':
        nome = request.form.get('nome')
        preco = request.form.get('preco')
        vendedor = request.form.get('vendedor')
        
        try:
            preco = float(preco)
        except:
            return redirect(url_for('index'))
        
        vendedores = geren.getVendedoresNome()
        
        if vendedor not in vendedores:
            return redirect(url_for('index'))
        
        geren.criarItem(nome, preco, vendedor)
        
        return redirect(url_for('index'))

@app.route('/adicionar_item', methods=['POST'])
def adicionar_item():
    if request.method == 'POST':
        comprador = request.form.get('comprador')
        item = request.form.get('item')
        
        try:
            item_tuple = ast.literal_eval(item)
            item_list = list(item_tuple)
        except (ValueError, SyntaxError) as e:
            item_list = []
        
        itemList = geren.getItensCarrinho(comprador)
        
        try:
            carrinho_list = parse_carrinho(itemList)
        except Exception as e:
            carrinho_list = []
        
        carrinho_list.append(item_list)
        
        geren.setItemCarrinho(comprador, str(carrinho_list))
        
        return redirect(url_for('index'))

@app.route('/remover_item', methods=['POST'])
def remover_item():
    if request.method == 'POST':
        comprador = request.form.get('comprador')
        item = request.form.get('item')
        
        try:
            item_tuple = ast.literal_eval(item)
            item_list = list(item_tuple)
        except (ValueError, SyntaxError) as e:
            item_list = []
        
        itemList = geren.getItensCarrinho(comprador)
        
        try:
            carrinho_list = parse_carrinho(itemList)
        except Exception as e:
            carrinho_list = []
            
        if item_list in carrinho_list:
            carrinho_list.remove(item_list)
        else:
            return redirect(url_for('index'))
        
        geren.setItemCarrinho(comprador, str(carrinho_list))
        
        return redirect(url_for('index'))

@app.route('/ver_carrinho', methods=['POST'])
def ver_carrinho():
    if request.method == 'POST':
        comprador = request.form.get('comprador')
        
        carrinho = geren.getItensCarrinho(comprador)
        
        try:
            carrinho_list = parse_carrinho(carrinho)
        except Exception as e:
            carrinho_list = []
        
        return render_template('index.html', carrinho=carrinho_list, compradores=geren.getCompradores(), vendedores=geren.getVendedores(), itens=geren.getItens())

if __name__ == '__main__':
    geren.criar_tabelas()
    
    app.run(host='127.0.0.1', port=8000, debug=True)