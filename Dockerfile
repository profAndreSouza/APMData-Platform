# Dockerfile para a aplicação InduData Platform
FROM python:3.11-slim

# Evita gravar bytecode no container e garante log em tempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências de build necessárias para psycopg2, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação, testes e documentação
COPY app/ ./app/
COPY tests/ ./tests/
COPY README.md ./README.md

# Expõe a porta padrão do Flask
EXPOSE 5000

# Variável de ambiente PYTHONPATH para que o Flask encontre o módulo 'core'
ENV PYTHONPATH=/app/app

# Comando de inicialização
CMD ["python", "app/main.py"]

