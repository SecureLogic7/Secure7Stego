# Use uma imagem oficial do Python como base
FROM python:3.9

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie todos os arquivos do projeto para o contêiner
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõem a porta em que o aplicativo Flask será executado
EXPOSE 5000

# Comando para executar o aplicativo
CMD ["python", "app.py"]

