from flask import Flask, render_template, request

app = Flask(__name__)

# Rota Principal
@app.route('/')
def home():
    return render_template('index.html')

# Rota para o formulário / registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Captura os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        
        # Exibe no terminal
        print(f"Novo usuário cadastrado: {nome} - {email}")
        
        return f"Usuário {nome} cadastrado com sucesso!"

    # Exibe a página do formulário se for requisição GET
    return render_template('registro.html')

if __name__ == '__main__':
    
    app.run(debug=True)