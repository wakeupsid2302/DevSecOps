# Dockerfile
FROM python:3.10-slim

# Security best practices
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Ensure the pip cache directory is writable
ENV PIP_CACHE_DIR=/tmp/.pip-cache
RUN mkdir -p $PIP_CACHE_DIR && chmod -R 777 $PIP_CACHE_DIR

# Switch to non-root user
USER appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --cache-dir=$PIP_CACHE_DIR

COPY app/ .

CMD ["python", "main.py"]
