# Dockerfile
FROM python:3.10-slim

# Security best practices
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Install dependencies as root
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

USER root

# Copy application files
COPY app/ .

CMD ["python", "main.py"]
