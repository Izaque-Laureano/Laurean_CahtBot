FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos do projeto para o contêiner
COPY . /app/

# Exponha a porta em que o Streamlit irá rodar
EXPOSE 8501

# Comando para rodar o chatbot
CMD ["streamlit", "run", "chatbot.py"]
