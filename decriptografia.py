from Crypto.Cipher import AES
from PIL import Image
import numpy as np

def decriptar_imagem(imagem_saida_path, imagem_chave_path):
    """
    Descriptografa um texto usando uma imagem como chave e retorna o texto descriptografado.

    Args:
        imagem_saida_path (str): O caminho para o arquivo que contém o texto criptografado.
        imagem_chave_path (str): O caminho para a imagem chave usada para gerar a chave de decriptação.

    Returns:
        str: O texto descriptografado ou uma mensagem de erro em caso de falha.
    """
    try:
        imagem_chave = Image.open(imagem_chave_path)
        imagem_chave_array = np.array(imagem_chave)
        chave = imagem_chave_array.tobytes()[:32]

        with open(imagem_saida_path, 'rb') as f:
            texto_criptografado = f.read()

        iv = texto_criptografado[:AES.block_size]
        cipher = AES.new(chave, AES.MODE_CFB, iv)
        texto_descriptografado = cipher.decrypt(texto_criptografado[AES.block_size:]).decode('utf-8')

        return f"Texto descriptografado: {texto_descriptografado}"
    except Exception as e:
        return f"Erro durante a descriptografia: {str(e)}"

"""
name='Secure7Stego_pro',
version='1.02',
author='Nelsomar Barros','Securelogic7'
author_email='nelsom.one8@gmail.com',
changes='Versão 1.02: Melhoria de segurança e encriptação com uso de interface gráfica web.',
"""
