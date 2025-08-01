from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from criptografia import encriptar_imagem
from decriptografia import decriptar_imagem

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limite de 16MB

# Garantir que a pasta de uploads exista
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Extensões de arquivo permitidas
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Função para verificar se a extensão do arquivo é permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        # Receber um arquivo de texto em vez de texto direto
        arquivo_texto = request.files['arquivo_texto']
        imagem_chave = request.files['imagem_chave']

        # Verifica se os arquivos foram enviados e se têm extensões permitidas
        if arquivo_texto and allowed_file(arquivo_texto.filename) and imagem_chave and allowed_file(imagem_chave.filename):
            filename_texto = secure_filename(arquivo_texto.filename)
            arquivo_texto_path = os.path.join(app.config['UPLOAD_FOLDER'], filename_texto)
            arquivo_texto.save(arquivo_texto_path)

            filename_chave = secure_filename(imagem_chave.filename)
            imagem_chave_path = os.path.join(app.config['UPLOAD_FOLDER'], filename_chave)
            imagem_chave.save(imagem_chave_path)

            # Ler o conteúdo do arquivo de texto
            with open(arquivo_texto_path, 'r') as file:
                texto = file.read()

            # Chamar a função de encriptação e obter a imagem de saída
            imagem_saida_path = encriptar_imagem(texto, imagem_chave_path)

            # Salvar a imagem de saída com um nome diferente
            filename_saida = 'encrypted_' + filename_chave
            imagem_saida_final_path = os.path.join(app.config['UPLOAD_FOLDER'], filename_saida)
            os.rename(imagem_saida_path, imagem_saida_final_path)

            flash('Arquivo encriptado com sucesso!')
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        imagem_saida = request.files['imagem_saida']
        imagem_chave = request.files['imagem_chave']

        # Verifica se os arquivos foram enviados e se têm extensões permitidas
        if imagem_saida and allowed_file(imagem_saida.filename) and imagem_chave and allowed_file(imagem_chave.filename):
            filename_saida = secure_filename(imagem_saida.filename)
            imagem_saida_path = os.path.join(app.config['UPLOAD_FOLDER'], filename_saida)
            imagem_saida.save(imagem_saida_path)

            filename_chave = secure_filename(imagem_chave.filename)
            imagem_chave_path = os.path.join(app.config['UPLOAD_FOLDER'], filename_chave)
            imagem_chave.save(imagem_chave_path)

            # Chamar a função de decriptação
            resultado = decriptar_imagem(imagem_saida_path, imagem_chave_path)

            flash(resultado)
            return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

"""
name='Secure7Stego_pro',
version='1.02',
author='Nelsomar Barros','Securelogic7'
author_email='nelsom.one8@gmail.com',
changes='Versão 1.02: Melhoria de segurança e encriptação com uso de interface gráfica web.',
"""