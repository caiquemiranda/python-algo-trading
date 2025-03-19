FROM python:3.9-slim

WORKDIR /app

# Copiar os arquivos de requisitos para o container
COPY requirements.txt .

# Instalar pacotes necessários para a compilação
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Instalar wine para possibilitar a execução do MetaTrader 5
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    wine \
    wine32 \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos os arquivos do projeto para o container
COPY . .

# Instruções para instalação do MetaTrader 5
RUN mkdir -p /mt5_installer && \
    cd /mt5_installer && \
    wget https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/mt5setup.exe && \
    wine mt5setup.exe /auto

# Criar um volume para persistir dados
VOLUME ["/app/data"]

# Porta padrão para Jupyter Notebook
EXPOSE 8888

# Comando para iniciar o Jupyter Notebook ao executar o container
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"] 