# Use a imagem oficial do Python com o tag slim
FROM python:3.11

WORKDIR /app

# Instale o Poetry
RUN pip install poetry

# Copie os arquivos de definição de dependências
COPY pyproject.toml poetry.lock ./

# Instale as dependências usando o Poetry
RUN poetry install --no-root --no-dev

# Copie o restante dos arquivos do seu projeto
COPY . .

# Comando de execução do seu aplicativo
CMD ["python", "run.py"]
