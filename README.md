# Secure7Stego Pro

Secure7Stego Pro é um aplicativo Flask para criptografar e decriptografar imagens.

## Pré-requisitos

- Python 3.8 ou superior
- Docker (opcional)

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/SecureLogic7/Secure7Stego/
    cd Secure7Stego
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/Mac
    venv\Scripts\activate  # No Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Executando o Aplicativo

1. Execute o aplicativo Flask:

    ```bash
    python app.py
    ```

2. Acesse o aplicativo no navegador:

    ```bash
    http://localhost:5000 #127.0.0.1:5000
    ```

## Usando Docker

1. Construa a imagem Docker:

    ```bash
    docker build -t secure7stego-pro .
    ```

2. Execute o contêiner Docker:

    ```bash
    docker run -p 5000:5000 secure7stego-pro
    ```

## Estrutura do Projeto

A estrutura do seu projeto
PROJETOSECURE7PRO/
├── app.py
├── config.py
├── criptografia.py
├── decriptografia.py
├── Dockerfile
├── requirements.txt
├── routes.py
├── static/
├── templates/
├── uploads/
└── README.md

# Secure7Stego Pro

Secure7Stego Pro é um aplicativo Flask para criptografar e decriptografar imagens.

## Pré-requisitos

- Python 3.8 ou superior
- Docker (opcional)

"""
name='Secure7Stego_pro',
version='1.02',
author='Nelsomar Barros','Securelogic7'
author_email='',
changes='Versão 1.02: Melhoria de segurança e encriptação com uso de interface gráfica web.',
"""
