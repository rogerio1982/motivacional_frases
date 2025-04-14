# Usar uma imagem base com Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos do projeto para dentro do container
COPY . /app

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta em que a aplicação Flask irá rodar
EXPOSE 5000

# Definir o comando para rodar a aplicação
CMD ["python", "app.py"]
