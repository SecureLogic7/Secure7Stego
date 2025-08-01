from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

from . import routes

"""
name='Secure7Stego_pro',
version='1.02',
author='Nelsomar Barros','Securelogic7'
author_email='nelsom.one8@gmail.com',
changes='Versão 1.02: Melhoria de segurança e encriptação com uso de interface gráfica web.',
"""
