from flask import render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from .criptografia import encriptar_imagem
from .decriptografia import decriptar_imagem
from . import app
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        texto = request.form.get('texto')
        imagem_chave = request.files['imagem_chave']

        if texto and imagem_chave:
            filename = secure_filename(imagem_chave.filename)
            imagem_chave_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            imagem_chave.save(imagem_chave_path)

            resultado = encriptar_imagem(texto, imagem_chave_path)
            flash(resultado)
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        imagem_saida = request.files['imagem_saida']
        imagem_chave = request.files['imagem_chave']

        if imagem_saida and imagem_chave:
            filename_saida = secure_filename(imagem_saida.filename)
            imagem_saida_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename_saida)
            imagem_saida.save(imagem_saida_path)

            filename_chave = secure_filename(imagem_chave.filename)
            imagem_chave_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename_chave)
            imagem_chave.save(imagem_chave_path)

            resultado = decriptar_imagem(imagem_saida_path, imagem_chave_path)
            flash(resultado)
            return redirect(url_for('index'))

    return render_template('index.html')


"""
name='Secure7Stego_pro',
version='1.02',
author='Nelsomar Barros','Securelogic7'
author_email='nelsom.one8@gmail.com',
changes='Versão 1.02: Melhoria de segurança e encriptação com uso de interface gráfica web.',
"""