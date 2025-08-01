from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import numpy as np
import os

def encriptar_imagem(texto, imagem_chave_path):
    """
    Encripta um texto usando uma imagem como chave e salva o texto encriptado em um arquivo.

    Args:
        texto (str): O texto a ser encriptado.
        imagem_chave_path (str): O caminho para a imagem chave usada para gerar a chave de encriptação.

    Returns:
        str: Uma mensagem indicando o sucesso ou falha da operação.
    """
    try:
        imagem_chave = Image.open(imagem_chave_path)
        imagem_chave_array = np.array(imagem_chave)
        chave = imagem_chave_array.tobytes()[:32]
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(chave, AES.MODE_CFB, iv)
        texto_criptografado = iv + cipher.encrypt(texto.encode('utf-8'))

        # Corrigido o caminho para salvar o arquivo criptografado
        with open(os.path.join('static', 'uploads', 'texto_criptografado.bin'), 'wb') as f:
            f.write(texto_criptografado)

        return "Texto criptografado e salvo com sucesso."
    except Exception as e:
        return f"Erro durante a criptografia: {str(e)}"

"""
name='Secure7Stego_pro',
version='1.02',
author='Nelsomar Barros','Securelogic7'
author_email='nelsom.one8@gmail.com',
changes='Versão 1.02: Melhoria de segurança e encriptação com uso de interface gráfica web.',
"""