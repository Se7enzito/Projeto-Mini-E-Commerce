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
        pass

@app.route('/criar_item', methods=['POST'])
def criar_item():
    if request.method == 'POST':
        pass

@app.route('/adicionar_item', methods=['POST'])
def adicionar_item():
    if request.method == 'POST':
        pass

@app.route('/remover_item', methods=['POST'])
def remover_item():
    if request.method == 'POST':
        pass
    
@app.route('/ver_carrinho', methods=['POST'])
def ver_carrinho():
    if request.method == 'POST':
        pass

if __name__ == '__main__':
    geren.criar_tabelas()
    
    app.run(host='127.0.0.1', port=8000, debug=True)