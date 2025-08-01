import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta_aqui'
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limite de 16MB

"""
name='Secure7Stego_pro',
version='1.02',
author='Nelsomar Barros','Securelogic7'
author_email='nelsom.one8@gmail.com',
changes='Versão 1.02: Melhoria de segurança e encriptação com uso de interface gráfica web.',
"""